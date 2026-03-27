# download_model.py
from huggingface_hub import snapshot_download
import sys
import os

# Importamos el modelo desde config.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import WHISPER_MODEL

def download():
    # Mapeo de nombres de faster-whisper a HuggingFace
    models = {
        "tiny": "Systran/faster-whisper-tiny",
        "base": "Systran/faster-whisper-base",
        "small": "Systran/faster-whisper-small",
        "medium": "Systran/faster-whisper-medium",
        "large-v3": "Systran/faster-whisper-large-v3"
    }
    
    repo_id = models.get(WHISPER_MODEL, f"Systran/faster-whisper-{WHISPER_MODEL}")
    
    print(f"📥 Descargando modelo '{WHISPER_MODEL}' desde {repo_id}...")
    print("Esto puede tardar unos minutos dependiendo de tu conexión.")
    
    try:
        # snapshot_download muestra una barra de progreso de tqdm por defecto
        snapshot_download(
            repo_id=repo_id,
            allow_patterns=["model.bin", "config.json", "vocabulary.txt", "tokenizer.json"]
        )
        print(f"\n✅ Modelo '{WHISPER_MODEL}' descargado correctamente.")
    except Exception as e:
        print(f"\n❌ Error al descargar: {e}")

if __name__ == "__main__":
    download()
