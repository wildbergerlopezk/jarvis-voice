# agent/conversation_loop.py
from agent.brain import JarvisBrain
from agent.utils import jarvis_context
import time

def main():
    brain = JarvisBrain()
    
    # Iniciar el sistema solo una vez (con "jarvis")
    print("🎙️ Escucha activa: di 'Jarvis' para comenzar.")
    
    while True:
        try:
            if jarvis_context.is_active and not jarvis_context.audio_queue.empty():
                user_input = jarvis_context.audio_queue.get()
                
                # Procesar comando
                result = brain.process_command(user_input)
                
                # Si hay acción, ejecutarla (ej. abrir navegador)
                if result["success"]:
                    print(f"✅ Acción ejecutada: {result['message']}")
                    
                    # Aquí puedes conectar con herramientas reales (por ejemplo, abrir el navegador)
                else:
                    print(result["message"])
        except KeyboardInterrupt:
            print("\n❌ Saliendo del sistema.")
            break

if __name__ == "__main__":
    main()
