# agent/brain.py
import os
from services import llm, db_service, rag_service
from agent.utils import jarvis_context
import re

class JarvisBrain:
    def __init__(self):
        self.tool_registry = {
            "abrir google": "services/google/calendar_service.py",
            "enviar correo": "services/google/gmail_service.py",
            "abrir archivo": "services/file_service.py",
            "recuerdame": "services/reminder_service.py"
        }
    
    def process_command(self, user_input):
        """
        Procesa un comando del usuario:
        - Detecta si es una acción conocida
        - Usa RAG para recuperar contexto previo (contactos, preferencias)
        - Propone auto-modificación si la acción no está disponible
        """
        # Paso 1: Normalizar entrada
        cleaned_input = user_input.lower().strip()
        
        # Verificar si es una acción conocida
        for action in self.tool_registry.keys():
            if action in cleaned_input:
                return {
                    "action": action,
                    "success": True,
                    "message": f"✅ Ejecutando: {action}"
                }
        
        # Paso 2: Si no hay acción directa, proponer auto-modificación
        proposed_actions = self.propose_self_improvement(cleaned_input)
        
        if proposed_actions:
            return {
                "action": None,
                "success": False,
                "message": f"""
                Lo siento, señor. No puedo hacer eso ahora.
                
                ✅ Pero puedo añadirlo a mi sistema:
                
                {proposed_actions}
                
                ¿Quieres que lo agregue ahora? (responde con 'sí' o 'no')
                """
            }
        
        return {
            "action": None,
            "success": False,
            "message": f"❌ No entiendo bien tu solicitud. Podría ayudarte si me dices más detalladamente."
        }

    def propose_self_improvement(self, user_input):
        """Propone un nuevo módulo de código para nuevas acciones."""
        
        # Ejemplo: buscar clientes en Google Maps
        if "cliente" in user_input or "google maps" in user_input:
            return self._generate_google_maps_code()
        
        elif "informe" in user_input and ("busca" in user_input or "listar" in user_input):
            return self._generate_report_code()
        
        else:
            return None

    def _generate_google_maps_code(self):
        """Propone código para buscar clientes en Google Maps."""
        code = """
# 📂 Nuevo módulo: google_maps_search.py
import requests
from geopy.geocoders import Nominatim
import time
import json

class GoogleMapsSearch:
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()
    
    def search_clients(self, query="empresa", radius=10000, limit=100):
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        params = {
            'query': f"{query} en Mexico",
            'radius': radius,
            'key': self.api_key
        }
        
        try:
            response = self.session.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                results = [item['name'] for item in data['results']]
                return {"count": len(results), "clients": results}
            else:
                return {"error": f"Error: {response.status_code}"}
        except Exception as e:
            return {"error": str(e)}

# Uso sugerido en el loop de conversación
# search = GoogleMapsSearch("API_KEY")
# result = search.search_clients("panadería", limit=100)
"""
        return code

    def _generate_report_code(self):
        """Propone código para generar un informe."""
        code = """
# 📂 Nuevo módulo: generate_report.py
import pandas as pd
from datetime import datetime

def create_client_report(clients_data, output_file="informe.txt"):
    df = pd.DataFrame(clients_data)
    df.to_csv(output_file, index=False)
    
    with open(output_file, 'r') as f:
        content = f.read()
        
    return f"✅ Informe generado: {output_file}\n{content[:200]}..."
"""
        return code
