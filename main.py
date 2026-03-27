#!/usr/bin/env python3
# ============================================
# JARVIS Pro - Main Entry Point
# ============================================

"""
JARVIS Pro - Asistente Autonomouso y Proactivo
================================================

Uso:
    python main.py                    # Modo interactivo (texto)
    python main.py --voice            # Modo voz (requiere micro)
    python main.py --test              # Modo test (sin LLM real)
    python main.py --setup             # Cargar datos de ejemplo

Requirements:
    - MongoDB corriendo (local o Docker)
    - Ollama corriendo con modelo (llama3.1:8b o mistral:7b)
    - Python 3.9+
"""

import sys
import os
import argparse
import signal
from pathlib import Path
from loguru import logger

# Agregar proyecto al path
sys.path.insert(0, str(Path(__file__).parent))

# ============================================
# LOGGING
# ============================================

from config import LOG_LEVEL, LOG_FILE

logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
    level=LOG_LEVEL
)
logger.add(
    LOG_FILE,
    rotation="10 MB",
    retention="7 days",
    level=LOG_LEVEL,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}"
)

# ============================================
# MAIN
# ============================================

def parse_args():
    """Parsear argumentos de línea de comando."""
    parser = argparse.ArgumentParser(
        description="JARVIS Pro - Asistente AI Proactivo",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--voice", "-v",
        action="store_true",
        help="Activar modo voz (requiere micrófono)"
    )
    
    parser.add_argument(
        "--test", "-t",
        action="store_true",
        help="Modo test (respuestas simuladas, sin LLM)"
    )
    
    parser.add_argument(
        "--setup", "-s",
        action="store_true",
        help="Cargar datos de ejemplo en MongoDB"
    )
    
    parser.add_argument(
        "--user-id",
        default="default_user",
        help="ID del usuario (default: default_user)"
    )
    
    parser.add_argument(
        "--no-scheduler",
        action="store_true",
        help="Desactivar scheduler proactivo"
    )
    
    return parser.parse_args()


def main():
    """Función principal."""
    args = parse_args()
    
    logger.info("="*50)
    logger.info("🚀 JARVIS Pro - Asistente AI Proactivo")
    logger.info("="*50)
    
    # SETUP MODE
    if args.setup:
        logger.info("📦 Modo Setup - Cargando datos de ejemplo...")
        from scripts.sample_data import load_sample_data
        load_sample_data()
        return
    
    # IMPORTAR SERVICIOS
    from services.db_service import DBService
    from services.llm_service import LLMService
    from services.memory_retrieval import MemoryRetrieval
    from services.stt import STTService
    from services.tts import TTSService
    from agent import JarvisBrain, ProactiveScheduler, set_services
    
    # INICIALIZAR SERVICIOS
    logger.info("📦 Inicializando servicios...")
    
    db = DBService()
    logger.info("✅ MongoDB conectado")
    
    llm = LLMService()
    
    if not args.test:
        model_info = llm.get_model_info()
        if not model_info.get("available"):
            logger.warning(f"⚠️ Ollama no disponible: {model_info.get('error')}")
            logger.warning("   Usá --test para modo simulado")
            logger.warning("   O iniciá Ollama: ollama serve")
    
    memory = MemoryRetrieval(db, llm)
    logger.info("✅ Memory RAG listo")
    
    try:
        stt = STTService()
        if stt.is_available():
            logger.info("✅ Whisper STT listo")
        else:
            logger.warning("⚠️ Whisper no disponible - modo texto solo")
            stt = None
    except Exception as e:
        logger.warning(f"⚠️ Error inicializando STT: {e}")
        stt = None
    
    try:
        tts = TTSService()
        if tts.is_available():
            logger.info("✅ Piper TTS listo")
        else:
            logger.warning("⚠️ Piper TTS no disponible")
            tts = None
    except Exception as e:
        logger.warning(f"⚠️ Error inicializando TTS: {e}")
        tts = None
    
    # CEREBRO
    brain = JarvisBrain(
        llm_service=llm,
        memory_retrieval=memory,
        db_service=db,
        user_id=args.user_id
    )
    set_services(db=db)
    logger.info("✅ JARVIS Brain listo")
    
    # SCHEDULER PROACTIVO
    scheduler = None
    if not args.no_scheduler and not args.test:
        try:
            scheduler = ProactiveScheduler(brain=brain, db_service=db)
            scheduler.start()
            logger.info("✅ Scheduler proactivo iniciado")
        except Exception as e:
            logger.warning(f"⚠️ Error iniciando scheduler: {e}")
    
    # SIGNAL HANDLER
    def signal_handler(sig, frame):
        logger.info("\n🛑 Deteniendo JARVIS...")
        if scheduler:
            scheduler.stop()
        logger.info("👋 ¡Hasta luego!")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    
    # LOOP PRINCIPAL
    logger.info("")
    logger.info("🎤 JARVIS LISTO")
    logger.info("="*50)
    logger.info("Escribí tu mensaje o")
    if args.voice and stt:
        logger.info("Decí 'JARVIS' para activar modo voz")
    logger.info("Escribí 'salir' para terminar")
    logger.info("="*50)
    
    if args.test:
        logger.warning("⚠️ MODO TEST - Respuestas simuladas")
    
    while True:
        try:
            if args.voice and stt:
                print("\n🎤 Escuchando... (hablá o escribí)")
                user_input = input("\nVos: ")
            else:
                user_input = input("\nVos: ")
            
            if user_input.lower() in ["salir", "exit", "quit", "chao", "adiós"]:
                logger.info("👋 ¡Hasta luego!")
                break
            
            if args.test:
                response = f"[TEST] Recibí: {user_input}"
                logger.info(f"JARVIS: {response}")
                if tts:
                    tts.speak_and_play(response)
                continue
            
            response = brain.process(user_input)
            logger.info(f"JARVIS: {response}")
            
            if tts and response:
                tts.speak_and_play(response)
            
            alert = brain.process_proactive_alerts()
            if alert:
                logger.info(f"🔔 {alert}")
                if tts:
                    tts.speak_and_play(alert)
        
        except KeyboardInterrupt:
            logger.info("\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            logger.error(f"❌ Error: {e}")
            if args.verbose:
                import traceback
                traceback.print_exc()
    
    if scheduler:
        scheduler.stop()


if __name__ == "__main__":
    main()
