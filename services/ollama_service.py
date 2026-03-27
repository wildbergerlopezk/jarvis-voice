import ollama
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.llm_config import LLM_MODEL, TEMPERATURE, SYSTEM_PROMPT

class OllamaService:
    def __init__(self):
        self.model = LLM_MODEL

    def generate_response(self, user_input, context=None):
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        if context:
            # Añadir contexto del RAG/Historial
            messages.append({"role": "system", "content": f"Contexto extraído: {context}"})
            
        messages.append({"role": "user", "content": user_input})
        
        try:
            response = ollama.chat(model=self.model, messages=messages, options={"temperature": TEMPERATURE})
            return response['message']['content']
        except Exception as e:
            return f"Error al generar respuesta: {e}"

    def plan_task(self, user_input):
        # Prompt específico para planificación (paso intermedio si es necesario)
        planning_prompt = f"Analiza esta petición y decide si necesitas buscar información extra o ejecutar una acción: {user_input}"
        # Implementación simple por ahora
        return self.generate_response(planning_prompt)
