#!/bin/bash

# Variables de entorno
export DJANGO_ENV=production
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Verificar que estamos en el directorio correcto
cd $(dirname "$0")/..

# Ejecutar el script de inicio
python scripts/init.py --env production --skip-deps --skip-static
