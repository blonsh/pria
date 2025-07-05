#!/bin/bash

# Variables de entorno
export DJANGO_ENV=development
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Iniciar medición de tiempo total
echo "\nIniciando configuración..."
START_TIME=$(date +%s)

# Verificación rápida de archivos esenciales
echo "\nVerificando archivos esenciales..."
time ls manage.py requirements.txt 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Error: No se encontraron archivos esenciales."
    echo "❌ Asegúrate de que estás en el directorio correcto y que los archivos existen."
    echo "❌ Los archivos necesarios son: manage.py y requirements.txt"
    exit 1
fi

echo "✅ Archivos esenciales encontrados. Continuando con la configuración..."

# Verificar que estamos en el directorio correcto
if [ ! -f "requirements.txt" ]; then
    echo "❌ Error: No se encuentra requirements.txt. ¿Estás en el directorio correcto?"
    exit 1
fi

# Verificar que Python está instalado
echo "\nVerificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 no está instalado"
    exit 1
fi

# Verificar que pip está instalado
echo "\nVerificando pip..."
if ! command -v pip3 &> /dev/null; then
    echo "❌ Error: pip no está instalado"
    exit 1
fi

# Crear y activar entorno virtual
if [ ! -d "venv" ]; then
    echo "\nCreando entorno virtual..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "❌ Error: No se pudo crear el entorno virtual"
        exit 1
    fi
fi

source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "❌ Error: No se pudo activar el entorno virtual"
    exit 1
fi

# Instalar dependencias
echo "\nInstalando dependencias..."

# Verificar que requirements.txt existe y no está vacío
if [ ! -f "requirements.txt" ]; then
    echo "❌ Error: No se encontró el archivo requirements.txt"
    exit 1
fi

if [ ! -s "requirements.txt" ]; then
    echo "❌ Error: El archivo requirements.txt está vacío"
    exit 1
fi

# Instalar dependencias con verbose para más información
pip install --no-cache-dir -r requirements.txt -v
if [ $? -ne 0 ]; then
    echo "❌ Error: Fallo en la instalación de dependencias"
    echo "⚠️ Verifica que todas las dependencias en requirements.txt son válidas"
    echo "⚠️ Verifica que tienes conexión a internet"
    exit 1
fi

# Verificar que las dependencias se instalaron correctamente
echo "\nVerificando instalación de dependencias..."

# Obtener lista de dependencias requeridas
echo "\nObteniendo lista de dependencias requeridas..."
REQ_DEPS=$(cat requirements.txt | grep -v '^#' | grep -v '^$')

# Mostrar dependencias instaladas
echo "\nDependencias instaladas:"
pip list

# Verificar cada dependencia requerida
echo "\nVerificando cada dependencia requerida..."
for dep in $REQ_DEPS; do
    # Extraer nombre y versión requerida
    dep_name=$(echo $dep | cut -d'=' -f1 | cut -d'>' -f1 | cut -d'<' -f1)
    
    # Verificar si está instalada
    if ! pip list | grep -q "^$dep_name"; then
        echo "❌ Error: La dependencia $dep_name no está instalada"
        exit 1
    fi

done

# Verificar versiones de dependencias
echo "\nVerificando versiones de dependencias..."
python -c "import django; print(f'Django {django.__version__}')"
python -c "import django.contrib.admin; print('django.contrib.admin OK')" 2>/dev/null
python -c "import django.contrib.auth; print('django.contrib.auth OK')" 2>/dev/null
python -c "import django.contrib.contenttypes; print('django.contrib.contenttypes OK')" 2>/dev/null
python -c "import django.contrib.sessions; print('django.contrib.sessions OK')" 2>/dev/null
python -c "import django.contrib.messages; print('django.contrib.messages OK')" 2>/dev/null
python -c "import django.contrib.staticfiles; print('django.contrib.staticfiles OK')" 2>/dev/null

# Verificar dependencias específicas del proyecto
echo "\nVerificando dependencias específicas del proyecto..."
python -c "import core; print('core OK')" 2>/dev/null
echo "✅ Todas las dependencias están instaladas y son compatibles"
echo "✅ Dependencias instaladas correctamente"

# Verificar configuración de Python
echo "\nVerificando configuración de Python..."
python -c "import django; print(f'Django {django.__version__}')"
if [ $? -ne 0 ]; then
    echo "❌ Error: Django no se instaló correctamente"
    exit 1
fi

echo "\nVerificando y aplicando migraciones..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "❌ Error: No se pudieron aplicar las migraciones"
    exit 1
fi

echo "✅ Migraciones aplicadas correctamente"

# Verificar estructura del proyecto
echo "\nVerificando estructura del proyecto..."

# Verificar enlaces simbólicos
if [ -n "$(find . -type l -exec ls -l {} \;)" ]; then
    echo "⚠️ Se encontraron enlaces simbólicos en el proyecto:"
    find . -type l -exec ls -l {} \;
    echo "⚠️ Considera revisar estos enlaces simbólicos para asegurarte de que apunten a ubicaciones válidas"
fi

if [ ! -f "manage.py" ]; then
    echo "❌ Error: No se encontró manage.py"
    exit 1
fi

if [ ! -d "core" ]; then
    echo "❌ Error: No se encontró el directorio core"
    exit 1
fi

# Verificar archivo .env
echo "\nVerificando archivo .env..."
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        echo "\nNo se encontró archivo .env. Creando desde .env.example..."
        cp .env.example .env
        if [ $? -ne 0 ]; then
            echo "❌ Error: No se pudo copiar .env.example"
            exit 1
        fi
    else
        echo "❌ Error: No se encontró archivo .env.example para crear el archivo .env"
        exit 1
    fi
else
    echo "⚠️ Archivo .env ya existe. No se sobrescribirá."
fi

# Verificar y crear directorios necesarios
echo "\nVerificando y creando directorios necesarios..."
for dir in logs media staticfiles; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        if [ $? -ne 0 ]; then
            echo "❌ Error: No se pudo crear el directorio $dir"
            exit 1
        fi
    fi
done

# Verificar y corregir permisos del proyecto
echo "\nVerificando y corrigiendo permisos..."

# Obtener el usuario actual
CURRENT_USER=$(whoami)

# Verificar permisos actuales
echo "\nVerificando permisos actuales..."
ls -lR | head -n 20

# Corregir permisos de manera segura
# 1. Directorios: rwxr-x--- (750)
# 2. Archivos: rw-r----- (640)
echo "\nCorrigiendo permisos..."

# Directorios
find . -type d -exec chmod 750 {} \;

# Archivos
find . -type f -exec chmod 640 {} \;

# Hacer ejecutables los scripts necesarios
chmod +x manage.py
chmod +x scripts/*.sh

# Verificar que los cambios de permisos fueron exitosos
if [ $? -ne 0 ]; then
    echo "❌ Error: No se pudieron cambiar los permisos"
    echo "⚠️ Los permisos podrían no ser correctos."
    echo "⚠️ Considera ejecutar manualmente:"
    echo "    chmod 750 -R ."
    echo "    chmod 640 -R ."
    echo "    chmod +x manage.py scripts/*.sh"
    exit 1
fi

# Verificar propietario
echo "\nVerificando propietario..."
if [ ! -z "$(find . ! -user $CURRENT_USER)" ]; then
    echo "⚠️ Se encontraron archivos que no son propiedad de $CURRENT_USER"
    echo "⚠️ Considera cambiar el propietario manualmente:"
    echo "    chown -R $CURRENT_USER:$CURRENT_USER ."
fi

# Verificar permisos finales
echo "\nVerificando permisos finales..."
ls -lR | head -n 20

# Mensaje final
echo "\n✅ Configuración completada exitosamente."
echo "✅ Entorno virtual activado y configurado."
echo "✅ Dependencias instaladas correctamente."
echo "✅ Estructura del proyecto verificada."
echo "✅ Archivo .env configurado."
echo "✅ Directorios necesarios creados."
echo "✅ Permisos establecidos correctamente."

# Mostrar tiempo total de ejecución
END_TIME=$(date +%s)
TOTAL_TIME=$((END_TIME - START_TIME))
echo "\nTiempo total de configuración: $TOTAL_TIME segundos"
echo "\nEl proyecto está listo para usar. Puedes comenzar ejecutando:"
echo "python manage.py runserver"
