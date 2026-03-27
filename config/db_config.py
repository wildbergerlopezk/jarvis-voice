# ============================================
# Configuración de MongoDB
# ============================================

import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "jarvis_pro")

COLLECTION_USER_PROFILE = "user_profile"
COLLECTION_CONTACTS = "contacts"
COLLECTION_CONVERSATIONS = "conversations"
COLLECTION_MEMORY_CHUNKS = "memory_chunks"
COLLECTION_TASKS = "tasks"
COLLECTION_MEMORIES = "memories"
COLLECTION_REMINDERS = "reminders"
COLLECTION_ALERTS = "alerts"

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
EMBEDDING_DIMENSIONS = 768
MEMORY_CACHE_TTL = 3600
