from pymongo import MongoClient
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.db_config import MONGO_URI, DB_NAME, COLLECTION_CONTACTS

def seed_data():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    
    contacts = [
        {"name": "Fernando", "email": "fernando@example.com", "phone": "123456789"},
        {"name": "Maria", "email": "maria@example.com", "phone": "987654321"},
        {"name": "Kevin", "email": "kevin@example.com", "phone": "555555555"}
    ]
    
    db[COLLECTION_CONTACTS].delete_many({}) # Limpiar
    db[COLLECTION_CONTACTS].insert_many(contacts)
    print(f"✅ Se han cargado {len(contacts)} contactos de prueba.")

if __name__ == "__main__":
    seed_data()
