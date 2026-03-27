# services/rag_service.py
from pymongo import MongoClient

def retrieve_context(query):
    """
    Busca en MongoDB si hay información previa sobre el usuario o contactos.
    Ej: ¿cuál es el email de Fernando?
    """
    client = MongoClient("mongodb://localhost:27017")
    db = client["jarvis_db"]
    collection = db["conversations"]

    # Buscar historial relacionado
    results = list(collection.find({
        "$text": {"$search": query}
    }, {"_id": 0, "texto": 1}))

    if results:
        return "\n".join([r['texto'] for r in results])
    else:
        return "No hay contexto previo sobre eso."
