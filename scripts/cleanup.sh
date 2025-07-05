#!/bin/bash

# Función para mostrar mensaje de progreso
echo_progress() {
    echo "\n$1"
    echo "$(printf '%0.s=' {1..70})"
}

# Variables de entorno
export DJANGO_ENV=development
export PYTHONPATH=$PYTHONPATH:$(pwd)

# 1. Limpiar archivos .pyc
echo_progress "Limpiando archivos .pyc..."
find . -name "*.pyc" -delete
find . -name "__pycache__" -delete

# 2. Limpiar caché de Django
echo_progress "Limpiando caché de Django..."
python manage.py clearsessions

# 3. Limpiar archivos temporales
echo_progress "Limpiando archivos temporales..."
rm -rf .pytest_cache
rm -rf .coverage
rm -rf htmlcov

# 4. Limpiar archivos de log
echo_progress "Limpiando archivos de log..."
find . -name "*.log" -delete

# 5. Limpiar archivos de Django
echo_progress "Limpiando archivos de Django..."
python manage.py collectstatic --noinput --clear

# 6. Limpiar caché de Tailwind
echo_progress "Limpiando caché de Tailwind..."
rm -rf .tailwind-cache

# Mensaje final
echo "\n✅ Limpieza completada. El proyecto debería estar más ligero y rápido."
