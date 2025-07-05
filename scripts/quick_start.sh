#!/bin/bash

# Variables de entorno
export DJANGO_ENV=development
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Función para mostrar mensaje de error y salir
error_exit() {
    echo "Error: $1" >&2
    exit 1
}

# Verificar que estamos en el directorio correcto
cd $(dirname "$0")/..

# Verificar que exista el archivo .env
if [ ! -f ".env" ]; then
    cp .env.example .env
fi

# Crear estructura de directorios necesaria
mkdir -p logs media staticfiles

# Instalar dependencias
pip install -r requirements.txt || error_exit "Error instalando dependencias"

# Ejecutar el script de inicio
python scripts/init.py --env development --skip-deps --skip-static
