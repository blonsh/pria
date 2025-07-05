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
    echo "No se encontró archivo .env. Creando uno nuevo..."
    cp .env.example .env
fi

# Crear estructura de directorios necesaria
mkdir -p logs media staticfiles

# Instalar dependencias
pip install -r requirements.txt || error_exit "Error instalando dependencias"

# Crear superusuario si no existe
python manage.py migrate || error_exit "Error en migraciones"

# Verificar si existe superusuario
if ! python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(is_superuser=True).exists()"; then
    echo "No se encontró superusuario. Creando uno nuevo..."
    python manage.py createsuperuser
fi

# Recopilar archivos estáticos
python manage.py collectstatic --noinput || error_exit "Error en archivos estáticos"

# Iniciar el servidor de desarrollo
echo "Iniciando servidor de desarrollo..."
python manage.py runserver 0.0.0.0:8000
