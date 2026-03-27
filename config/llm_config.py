# ============================================
# Configuración de Ollama (LLM)
# ============================================

import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
LLM_MODEL = os.getenv("LLM_MODEL", "llama3.1:8b")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")

TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2048"))
TOP_P = float(os.getenv("TOP_P", "0.9"))
FREQUENCY_PENALTY = float(os.getenv("FREQUENCY_PENALTY", "0.0"))
PRESENCE_PENALTY = float(os.getenv("PRESENCE_PENALTY", "0.0"))

TOOL_CALLING_ENABLED = os.getenv("TOOL_CALLING_ENABLED", "true").lower() == "true"
MAX_TOOL_CALLS = int(os.getenv("MAX_TOOL_CALLS", "10"))

MAX_CONTEXT_MESSAGES = int(os.getenv("MAX_CONTEXT_MESSAGES", "50"))
CONVERSATION_SUMMARY_TRIGGER = int(os.getenv("CONVERSATION_SUMMARY_TRIGGER", "20"))
