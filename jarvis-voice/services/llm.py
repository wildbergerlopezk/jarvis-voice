# services/llm.py
import ollama
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import OLLAMA_MODEL

class LLMService:
    def __init__(self):
        self.model = OLLAMA_MODEL
        print(f"🧠 Conectado a Ollama (modelo: {self.model})")

    def generate(self, prompt):
        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Eres Jarvis. Responde SIEMPRE en español. Sé extremadamente breve (máximo 10 palabras). No saludes si ya has saludado antes. Responde DIRECTAMENTE."},
                    {"role": "user", "content": prompt}
                ],
                options={
                    "num_predict": 20,
                    "temperature": 0.3,
                    "top_p": 0.9
                }
            )
            return response['message']['content']
        except Exception as e:
            return f"Error al generar respuesta de Ollama: {e}"
