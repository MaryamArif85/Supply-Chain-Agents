
import logging
import threading
import time

from google import genai
from google.genai import errors, types

import config


# ==========================================
# LOGGING
# ==========================================

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("SupplyChainSentinel.Gemini")


# ==========================================
# CUSTOM EXCEPTION
# ==========================================

class GeminiServiceError(Exception):
    """Raised when Gemini requests cannot be completed."""
    pass


# ==========================================
# GEMINI KEY MANAGER
# ==========================================

class GeminiKeyManager:

    def __init__(self, api_keys):

        if not api_keys:
            raise ValueError("No Gemini API keys provided.")

        self.api_keys = api_keys
        self.current_index = 0
        self.cooldowns = {}
        self.lock = threading.Lock()

    def get_available_key(self):

        with self.lock:

            now = time.monotonic()

            for offset in range(len(self.api_keys)):

                index = (
                    self.current_index + offset
                ) % len(self.api_keys)

                if now >= self.cooldowns.get(index, 0):

                    self.current_index = (
                        index + 1
                    ) % len(self.api_keys)

                    return index, self.api_keys[index]

            return None, None

    def mark_unavailable(self, index, seconds=60):

        with self.lock:
            self.cooldowns[index] = (
                time.monotonic() + seconds
            )

    def mark_available(self, index):

        with self.lock:
            self.cooldowns.pop(index, None)


# ==========================================
# GEMINI SERVICE
# ==========================================

class GeminiService:

    def __init__(self):

        config.validate_gemini_config()

        self.model = config.GEMINI_MODEL

        self.key_manager = GeminiKeyManager(
            config.GOOGLE_API_KEYS
        )

        # Reuse clients instead of creating one
        # for every request.
        self.clients = []

        http_options = types.HttpOptions(
            timeout=45_000,
            retry_options=types.HttpRetryOptions(
                attempts=1
            )
        )

        for key in config.GOOGLE_API_KEYS:

            self.clients.append(
                genai.Client(
                    api_key=key,
                    http_options=http_options
                )
            )

        logger.info(
            "Gemini service initialized with %s projects.",
            len(self.clients)
        )

    # --------------------------------------
    # Classify errors
    # --------------------------------------

    @staticmethod
    def classify_error(error):

        code = getattr(error, "code", None)
        message = str(error).lower()

        if code == 429 or any(
            word in message
            for word in [
                "resource_exhausted",
                "quota exceeded",
                "rate limit",
                "too many requests"
            ]
        ):
            return "quota"

        if code in (401, 403):
            return "authentication"

        if code in (500, 502, 503, 504):
            return "server"

        return "other"

    # --------------------------------------
    # Generate text
    # --------------------------------------

    def generate_text(
        self,
        prompt,
        system_instruction=None,
        max_output_tokens=1000
    ):

        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        failures = []

        for attempt in range(len(self.clients)):

            index, api_key = (
                self.key_manager.get_available_key()
            )

            if index is None:

                raise GeminiServiceError(
                    "All Gemini projects are temporarily "
                    "unavailable. Please retry later. "
                    + " | ".join(failures)
                )

            client = self.clients[index]
            project = f"Project {index + 1}"

            logger.info(
                "Sending request using %s (attempt %s).",
                project,
                attempt + 1
            )

            generation_config = types.GenerateContentConfig(
                max_output_tokens=max_output_tokens,
                temperature=0.3,
                system_instruction=system_instruction,
                automatic_continuation=False,
                automatic_function_calling=(
                    types.AutomaticFunctionCallingConfig(
                        disable=True
                    )
                )
            )

            start_time = time.perf_counter()

            try:

                response = client.models.generate_content(
                    model=self.model,
                    contents=prompt,
                    config=generation_config
                )

                elapsed = time.perf_counter() - start_time

                if not response.text:
                    raise GeminiServiceError(
                        "Gemini returned an empty response."
                    )

                self.key_manager.mark_available(index)

                logger.info(
                    "%s succeeded in %.2f seconds.",
                    project,
                    elapsed
                )

                return response.text

            except errors.APIError as error:

                elapsed = time.perf_counter() - start_time
                error_type = self.classify_error(error)

                logger.error(
                    "%s failed after %.2f seconds: %s",
                    project,
                    elapsed,
                    error
                )

                failures.append(
                    f"{project}: {error_type}"
                )

                if error_type == "quota":

                    self.key_manager.mark_unavailable(
                        index,
                        seconds=60
                    )

                    continue

                if error_type == "authentication":

                    self.key_manager.mark_unavailable(
                        index,
                        seconds=300
                    )

                    continue

                if error_type == "server":

                    self.key_manager.mark_unavailable(
                        index,
                        seconds=30
                    )

                    continue

                raise GeminiServiceError(
                    f"Non-retryable Gemini error: {error}"
                ) from error

            except TimeoutError as error:

                elapsed = time.perf_counter() - start_time

                logger.error(
                    "%s timed out after %.2f seconds.",
                    project,
                    elapsed
                )

                failures.append(
                    f"{project}: request timed out"
                )

                self.key_manager.mark_unavailable(
                    index,
                    seconds=30
                )

                continue

            except GeminiServiceError:
                raise

            except Exception as error:

                logger.exception(
                    "Unexpected error using %s.",
                    project
                )

                failures.append(
                    f"{project}: {type(error).__name__}"
                )

                self.key_manager.mark_unavailable(
                    index,
                    seconds=30
                )

        raise GeminiServiceError(
            "All Gemini projects failed. "
            + " | ".join(failures)
        )


# ==========================================
# SHARED SERVICE INSTANCE
# ==========================================

gemini_service = GeminiService()

