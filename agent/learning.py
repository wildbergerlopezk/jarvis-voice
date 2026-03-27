import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.mongo_service import MongoService

class LearningModule:
    def __init__(self, mongo: MongoService):
        self.mongo = mongo

    def extract_preferences(self, user_id, conversation_history):
        """
        Analiza el historial reciente para extraer hechos o preferencias.
        """
        # TODO: Usar LLM para extraer 'facts'
        # Por ahora simulamos la extracción de una preferencia detectada
        extracted_fact = "Al usuario le gusta recibir correos en formato HTML."
        
        if extracted_fact:
            self.mongo.add_memory(user_id, extracted_fact)
            return f"Aprendido: {extracted_fact}"
        return None
        
    def analyze_context(self, text):
        # Lógica para detectar intenciones o temas recurrentes
        pass
