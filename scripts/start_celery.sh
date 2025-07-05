#!/bin/bash

# Variables de entorno
export DJANGO_ENV=${DJANGO_ENV:-development}
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Función para mostrar mensaje de error y salir
error_exit() {
    echo "Error: $1" >&2
    exit 1
}

# Verificar que estamos en el directorio correcto
cd $(dirname "$0")/..

# Verificar dependencias
celery --version >/dev/null 2>&1 || error_exit "Celery no está instalado"

# Verificar configuración de celery
if [ ! -f "celery.py" ]; then
    error_exit "No se encontró archivo celery.py"
fi

# Iniciar celery worker
if [ "$DJANGO_ENV" = "production" ]; then
    echo "Iniciando Celery worker en producción..."
    celery -A core worker --loglevel=INFO --concurrency=4 -Q default
else
    echo "Iniciando Celery worker en desarrollo..."
    celery -A core worker --loglevel=DEBUG -Q default
fi
