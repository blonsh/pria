#!/bin/bash

# Variables de entorno
export DJANGO_ENV=development
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Configurar .env si no existe
if [ ! -f ".env" ]; then
    echo "Configurando archivo .env..."
    cp .env.example .env
    echo "Por favor, edita el archivo .env con tus credenciales"
fi

# Crear estructura de directorios
mkdir -p logs media staticfiles

# Ejecutar migraciones
echo "Ejecutando migraciones..."
python manage.py migrate

# Crear superusuario
echo "¿Crear superusuario? (s/n)"
read respuesta
if [ "$respuesta" = "s" ]; then
    python manage.py createsuperuser
fi

# Iniciar servidor
echo "Iniciando servidor..."
python manage.py runserver 0.0.0.0:8000
