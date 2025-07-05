#!/bin/bash

# Variables de entorno
export DJANGO_ENV=development
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Verificar que estamos en el directorio correcto
cd $(dirname "$0")/..

# Crear estructura de directorios necesaria
mkdir -p logs media staticfiles

# Iniciar el servidor de desarrollo
python manage.py runserver 0.0.0.0:8000
