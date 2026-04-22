# 🤖 Jarvis — Asistente de Voz Local con IA

Asistente de voz conversacional que corre **100% offline** en tu máquina. Sin APIs externas, sin costos, sin internet.

Hablás → Whisper transcribe → Ollama responde → Piper lo dice en voz alta.

---

## ⚙️ Stack

| Componente | Tecnología |
|---|---|
| Speech-to-Text | [Faster-Whisper](https://github.com/SYSTRAN/faster-whisper) (modelo `tiny`) |
| LLM | [Ollama](https://ollama.com/) con `tinyllama` |
| Text-to-Speech | [Piper TTS](https://github.com/rhasspy/piper) (voz `es_ES-davefx-medium`) |
| Audio | `sounddevice` + `aplay` |

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/wildbergerlopezk/jarvis
cd jarvis
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Descargar el modelo de Whisper

```bash
python download_model.py
```

### 4. Instalar Ollama y bajar el modelo LLM

```bash
# Instalar Ollama desde https://ollama.com/download
ollama pull tinyllama
```

### 5. Descargar Piper TTS

Descargá el binario de Piper para tu OS desde [github.com/rhasspy/piper/releases](https://github.com/rhasspy/piper/releases) y extraelo en la carpeta `piper/`.

Descargá el modelo de voz `es_ES-davefx-medium` y colocalo en la raíz del proyecto.

### 6. Configurar el micrófono

```bash
python utils/audio_utils.py
```

Buscá el índice de tu micrófono en la lista y actualizá `DEVICE_INDEX` en `config.py`.

---

## ▶️ Uso

```bash
python main.py
```

Jarvis grabará 3 segundos de audio, procesará tu voz y responderá en español.

Para salir: `Ctrl + C`

---

## 📁 Estructura del proyecto

```
jarvis/
├── main.py               # Entry point
├── config.py             # Configuración centralizada
├── download_model.py     # Script para descargar Whisper
├── requirements.txt
├── services/
│   ├── stt.py            # Speech-to-Text (Faster-Whisper)
│   ├── llm.py            # LLM (Ollama)
│   └── tts.py            # Text-to-Speech (Piper)
└── utils/
    └── audio_utils.py    # Listado de dispositivos de audio
```

---

## 🔧 Configuración (`config.py`)

| Variable | Descripción | Default |
|---|---|---|
| `DEVICE_INDEX` | Índice del micrófono | `16` |
| `WHISPER_MODEL` | Tamaño del modelo STT | `tiny` |
| `RECORD_SECONDS` | Duración de grabación | `3` |
| `OLLAMA_MODEL` | Modelo LLM local | `tinyllama:latest` |

---

## 🗺️ Roadmap

- [ ] Memoria de conversación (contexto entre mensajes)
- [ ] Detección de palabra clave para activación ("Hey Jarvis")
- [ ] Soporte para comandos del sistema (abrir apps, buscar en web)
- [ ] Interfaz web básica con historial

---

## 📋 Requisitos del sistema

- Python 3.9+
- Linux (usa `aplay` para reproducir audio) — Windows requiere adaptar el TTS
- Ollama instalado y corriendo localmente
- ~500MB de espacio para modelos
