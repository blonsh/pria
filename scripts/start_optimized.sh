#!/bin/bash

# Variables de entorno
export DJANGO_ENV=development
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Desactivar autoreload para mejorar rendimiento
export DJANGO_AUTO_RELOAD=false

# Verificar y activar el entorno virtual
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✅ Entorno virtual activado"
fi

# Verificar el archivo .env
if [ ! -f ".env" ]; then
    cp -n .env.example .env  # -n evita sobrescribir si existe
    echo "✅ Archivo .env creado"
fi

# Ejecutar el servidor con configuraciones optimizadas
python manage.py runserver --noreload 0.0.0.0:8000
