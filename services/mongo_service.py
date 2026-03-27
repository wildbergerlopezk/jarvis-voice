from pymongo import MongoClient
import sys
import os

# Añadir el path raíz para importaciones
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.db_config import MONGO_URI, DB_NAME, COLLECTION_CONVERSATIONS, COLLECTION_CONTACTS, COLLECTION_MEMORY

class MongoService:
    def __init__(self):
        try:
            self.client = MongoClient(MONGO_URI)
            self.db = self.client[DB_NAME]
            # Verificar conexión
            self.client.admin.command('ping')
            print("✅ Conexión a MongoDB exitosa.")
        except Exception as e:
            print(f"❌ Error al conectar a MongoDB: {e}")
            self.client = None

    def save_conversation(self, user_id, message, role="user"):
        if self.client:
            self.db[COLLECTION_CONVERSATIONS].insert_one({
                "user_id": user_id,
                "role": role,
                "content": message,
                "timestamp": os.getpid() # Placeholder for timestamp, should use datetime
            })

    def get_context(self, user_id, limit=5):
        if self.client:
            return list(self.db[COLLECTION_CONVERSATIONS].find({"user_id": user_id}).sort("_id", -1).limit(limit))
        return []

    def get_contacts(self, query=None):
        if self.client:
            if query:
                return list(self.db[COLLECTION_CONTACTS].find(query))
            return list(self.db[COLLECTION_CONTACTS].find())
        return []

    def add_memory(self, user_id, chunk):
        if self.client:
            self.db[COLLECTION_MEMORY].insert_one({
                "user_id": user_id,
                "text": chunk,
                "embedding_id": None # Reservado para RAG vectorial si se añade
            })
