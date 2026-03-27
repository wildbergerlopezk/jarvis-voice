#!/bin/bash

echo "🚀 Arrancando JARVIS-Core..."

# 1. Levantar MongoDB con Docker
echo "🍃 Iniciando MongoDB..."
docker-compose up -d

# 2. Verificar si Ollama está corriendo
if ! curl -s http://localhost:11434/api/tags > /dev/null; then
    echo "❌ Ollama no parece estar corriendo. Por favor, inícialo primero."
    exit 1
fi

# 3. Arrancar la aplicación (loop principal)
echo "🎙️ Iniciando loop de conversación..."
source venv/bin/activate
python3 -m core.conversation_loop
