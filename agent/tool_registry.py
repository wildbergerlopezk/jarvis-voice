import logging
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ToolRegistry:
    def __init__(self):
        self.tools = {
            "send_email": self._send_email,
            "check_calendar": self._check_calendar,
            "search_web": self._search_web,
            "open_app": self._open_app
        }

    def list_tools(self):
        return list(self.tools.keys())

    def execute(self, tool_name, **params):
        if tool_name in self.tools:
            try:
                print(f"🛠️ Ejecutando herramienta: {tool_name} con parámetros: {params}")
                return self.tools[tool_name](**params)
            except Exception as e:
                return f"Error al ejecutar {tool_name}: {str(e)}"
        return "Herramienta no encontrada."

    # --- Implementaciones mock/reales ---
    
    def _send_email(self, to, subject, body):
        # Aquí se llamará a gmail_service.py mas adelante
        return f"Simulado: Correo enviado a {to} con asunto '{subject}'"

    def _check_calendar(self):
        # Aquí se llamará a calendar_service.py mas adelante
        return "Simulado: Tienes una reunión a las 3 PM con Fernando."

    def _search_web(self, query):
        return f"Simulado: El clima en tu area es de 22 grados (resultado para: {query})"

    def _open_app(self, app_name):
        return f"Simulado: Iniciando {app_name}..."
