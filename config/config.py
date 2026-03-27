# ============================================
# Configuración General de Jarvis Pro
# ============================================

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
LOGS_DIR = PROJECT_ROOT / "logs"
DATA_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "JARVIS")
WAKE_WORD = os.getenv("WAKE_WORD", "jarvis")
LANGUAGE = os.getenv("LANGUAGE", "es")
TIMEZONE = os.getenv("TIMEZONE", "America/Asuncion")

DEBUG = os.getenv("DEBUG", "false").lower() == "true"
VERBOSE = os.getenv("VERBOSE", "false").lower() == "true"

AUDIO_SAMPLE_RATE = 16000
AUDIO_CHUNK_SIZE = 1024
AUDIO_DEVICE_INDEX = int(os.getenv("AUDIO_DEVICE_INDEX", "-1"))

PROACTIVE_CHECK_INTERVAL = int(os.getenv("PROACTIVE_CHECK_INTERVAL", "300"))
PROACTIVE_EVENTS_AHEAD_MINUTES = int(os.getenv("PROACTIVE_EVENTS_AHEAD_MINUTES", "30"))
PROACTIVE_EMAIL_CHECK = os.getenv("PROACTIVE_EMAIL_CHECK", "true").lower() == "true"

WHISPER_MODEL = os.getenv("WHISPER_MODEL", "medium")
PIPER_MODEL = os.getenv("PIPER_MODEL", "es_ES-lowbias")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = LOGS_DIR / "jarvis.log"
