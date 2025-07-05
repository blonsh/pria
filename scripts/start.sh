#!/bin/bash

# Verificar el archivo .env
if [ ! -f ".env" ]; then
    echo "No se encontró archivo .env. Copiando desde .env.example..."
    cp .env.example .env
fi

# Verificar y activar el entorno virtual
if [ -d "venv" ]; then
    source venv/bin/activate
elif [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Ejecutar el servidor
python manage.py runserver 0.0.0.0:8000
