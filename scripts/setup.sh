#!/bin/bash

echo "🚀 Iniciando configuración de JARVIS-Core..."

# 1. Crear entorno virtual
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

# 2. Instalar dependencias
echo "📥 Instalando dependencias de Python..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 3. Descargar modelo de Ollama
echo "🧠 Descargando modelo Llama 3.1 8B en Ollama..."
ollama pull llama3.1:8b-instruct-q4_K_M

# 4. Asegurar permisos de los scripts
chmod +x scripts/*.sh

echo "✅ Configuración completada. Usa './scripts/start_all.sh' para arrancar."
