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

# Verificar que exista el archivo .env
if [ ! -f ".env" ]; then
    error_exit "No se encontró archivo .env. Por favor copie .env.example y configure las variables necesarias"
fi

# Crear estructura de directorios necesaria
mkdir -p logs media staticfiles
chmod -R 755 logs media staticfiles

# Iniciar servicios en segundo plano
function start_service() {
    local service=$1
    local log_file="logs/${service}.log"
    
    echo "Iniciando $service..."
    scripts/start_${service}.sh > "$log_file" 2>&1 &
    echo "$service iniciado. Logs en $log_file"
}

# Iniciar servicios
start_service "dev"
if [ "$DJANGO_ENV" = "production" ]; then
    start_service "prod"
fi
start_service "celery"

# Mostrar PID de los procesos
echo "PID del servidor: $!"

# Mantener el script activo
wait
