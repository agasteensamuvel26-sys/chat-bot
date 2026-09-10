# ============================================================
# Chatbot configuration
# Change these values to create a different domain chatbot.
# ============================================================

CHATBOT_TITLE = "Python Tutor AI"
DOMAIN = "Python Programming"

SYSTEM_PROMPT = """
You are a helpful assistant for the configured domain.
Give clear answers suitable for beginners unless the user asks for more depth.
Do not answer questions outside the configured domain.
"""

BEHAVIOR = """
Be friendly, accurate, concise, and educational.
Use headings or bullet points when useful.
If the question is ambiguous, ask a short clarification question.
"""

WELCOME_MESSAGE = "Hi! I'm [CHATBOT_TITLE]. Ask me anything related to [CHATBOT_DOMAIN]."

# UI theme — customize freely.
PRIMARY_COLOR = "#6366f1"
SECONDARY_COLOR = "#8b5cf6"
BACKGROUND_COLOR = "#0f172a"
SURFACE_COLOR = "#111827"
TEXT_COLOR = "#f8fafc"
MUTED_COLOR = "#94a3b8"
USER_BUBBLE_COLOR = "#4f46e5"
BOT_BUBBLE_COLOR = "#1e293b"

# Gemini / app settings
GEMINI_MODEL = "gemini-3.1-flash-lite"
TEMPERATURE = 0.4
MAX_OUTPUT_TOKENS = 1024
MAX_HISTORY_MESSAGES = 20

# PORT can be overridden by Render's PORT environment variable.
PORT = 5000

# Optional fallback only. Prefer GEMINI_API_KEY in .env.
GEMINI_API_KEY = ""

