
import config
from crewai import LLM


def get_crewai_llm():

    config.validate_gemini_config()

    # Use the first configured API key as the primary key.
    primary_api_key = config.GOOGLE_API_KEYS[0]

    llm = LLM(
        model=f"gemini/{config.GEMINI_MODEL}",
        api_key=primary_api_key,
        temperature=0.2,
        timeout=90,
        max_tokens=1500
    )

    return llm
