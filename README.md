# JARVIS Pro - Asistente AI Autonomouso y Proactivo

**100% Local** - Tu propio JARVIS sin servicios cloud.

---

## 🚀 Quick Start

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Configurar (.env)
cp .env.example .env  # Editar según tu setup

# 3. Iniciar servicios (MongoDB + Ollama)
docker compose up -d mongodb
ollama serve

# 4. Descargar modelo LLM
ollama pull llama3.1:8b

# 5. Correr
python main.py --setup   # Cargar datos de ejemplo
python main.py           # Iniciar
```

---

## 📁 Estructura del Proyecto

```
jarvis-core/
├── agent/                     # 🧠 El cerebro autonomouso
│   ├── brain.py              # Planner + Executor + Tool Runner
│   ├── tool_registry.py     # 15+ herramientas disponibles
│   ├── proactive_scheduler.py # Monitor proactivo
│   └── learning.py          # Extrae prefs del usuario
├── services/                  # 🔧 Servicios externos
│   ├── db_service.py        # MongoDB
│   ├── llm_service.py        # Ollama con tool calling
│   ├── memory_retrieval.py   # RAG con embeddings
│   ├── stt.py                # Whisper (STT)
│   ├── tts.py                # Piper (TTS)
│   └── google/               # Gmail, Calendar, Contacts
├── config/                    # ⚙️ Configuración
├── scripts/                   # 🛠️ Setup y datos de ejemplo
└── main.py                   # 🚀 Entry point
```

---

## 🎯 Características Principales

### 🤖 Agente Autonomouso
- **Tool Calling**: El LLM decide qué herramientas usar
- **Planning**: Planifica acciones multi-paso
- **RAG**: Recupera contexto relevante de MongoDB

### ⏰ Proactivo
- **Scheduler**: Monitorea recordatorios, eventos, emails
- **Learning**: Aprende preferencias del usuario
- **Alertas**: Notifica proactivamente

### 🔗 Integraciones
- **Gmail**: Leer y enviar emails
- **Google Calendar**: Eventos y schedule
- **Google Contacts**: Buscar contactos
- **Sistema**: Abrir apps, ejecutar comandos

---

## 🔧 Hardware Recomendado

| Componente | Mínimo | Recomendado |
|------------|--------|-------------|
| GPU | 4GB VRAM | **RX 5700 8GB** |
| RAM | 8GB | 16GB |
| CPU | 4 cores | 6+ cores |

### Modelos para RX 5700 8GB
- `llama3.1:8b` (q4) → ~5GB VRAM
- `mistral:7b` → similar
- `whisper-medium` → ~3GB VRAM

---

## 📦 Dependencies

```
ollama, pymongo, google-api-python-client,
faster-whisper, piper-tts, loguru, python-dotenv
```

Ver `requirements.txt` completo.

---

## 📝 Licencia

MIT
