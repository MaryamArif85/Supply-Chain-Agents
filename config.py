import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# APPLICATION CONFIGURATION
# ==========================================

APP_NAME = "SupplyChain Sentinel"
APP_SUBTITLE = "AI-Powered Crisis Management"

PAGE_TITLE = "SupplyChain Sentinel | Control Tower"
PAGE_ICON = "📦"

# ==========================================
# GOOGLE GEMINI CONFIGURATION
# ==========================================

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.6-flash"
)

GOOGLE_API_KEYS = [
    os.getenv(f"GOOGLE_API_KEY_{i}")
    for i in range(1, 4)
]

# Keep only configured keys
GOOGLE_API_KEYS = [
    key.strip()
    for key in GOOGLE_API_KEYS
    if key and key.strip()
]

# ==========================================
# LANGSMITH CONFIGURATION
# ==========================================

LANGSMITH_TRACING = (
    os.getenv("LANGSMITH_TRACING", "true").lower() == "true"
)

LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

LANGSMITH_PROJECT = os.getenv(
    "LANGSMITH_PROJECT",
    "SupplyChain-Sentinel"
)

LANGSMITH_ENDPOINT = os.getenv(
    "LANGSMITH_ENDPOINT",
    "https://api.smith.langchain.com"
)

# ==========================================
# CONFIGURATION VALIDATION
# ==========================================

def validate_gemini_config():
    if not GOOGLE_API_KEYS:
        raise ValueError(
            "No Gemini API keys configured. "
            "Add GOOGLE_API_KEY_1, GOOGLE_API_KEY_2 "
            "or GOOGLE_API_KEY_3 to your .env file."
        )

    if not GEMINI_MODEL:
        raise ValueError("GEMINI_MODEL is missing.")

    return True


def validate_langsmith_config():
    if LANGSMITH_TRACING and not LANGSMITH_API_KEY:
        return False

    return True


# ==========================================
# AGENT DEFINITIONS
# ==========================================

AGENTS = [
    {
        "name": "Disruption Analyst",
        "role": "Supply Chain Risk Detector",
        "description": "Identifies and classifies supply chain disruptions.",
        "icon": "🚨"
    },
    {
        "name": "Inventory Analyst",
        "role": "Inventory Intelligence Specialist",
        "description": "Analyzes stock levels, demand and inventory shortages.",
        "icon": "📦"
    },
    {
        "name": "Supplier Intelligence",
        "role": "Supplier Evaluation Specialist",
        "description": "Evaluates suppliers and identifies alternatives.",
        "icon": "🏭"
    },
    {
        "name": "Logistics Optimizer",
        "role": "Transportation Optimization Specialist",
        "description": "Evaluates routes, delivery time and transport costs.",
        "icon": "🚚"
    },
    {
        "name": "Risk Analyst",
        "role": "Operational Risk Specialist",
        "description": "Calculates financial and operational risks.",
        "icon": "🛡️"
    },
    {
        "name": "Recovery Coordinator",
        "role": "Supply Chain Recovery Manager",
        "description": "Creates the final coordinated recovery strategy.",
        "icon": "🧠"
    }
]

# ==========================================
# NAVIGATION
# ==========================================

NAVIGATION = [
    "Overview",
    "Crisis Simulation",
    "Agent Execution",
    "Recovery Plans",
    "Supply Chain Data"
]

