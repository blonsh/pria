import os
import sys
from pathlib import Path

print("Verificando el entorno de ejecución...")

# Verificar estructura de directorios
print("\nVerificando estructura de directorios:")
project_dir = Path(__file__).resolve().parent.parent
print(f"Directorio del proyecto: {project_dir}")

required_dirs = ['core', 'manage.py', 'requirements.txt']
missing_dirs = []
for dir in required_dirs:
    if not (project_dir / dir).exists():
        missing_dirs.append(dir)

if missing_dirs:
    print(f"\nFaltan los siguientes directorios: {', '.join(missing_dirs)}")
else:
    print("✅ Todos los directorios principales están presentes")

# Verificar variables de entorno
print("\nVerificando variables de entorno:")
required_env_vars = ['SECRET_KEY', 'DB_NAME', 'DB_USER', 'DB_PASSWORD', 'DB_HOST', 'DB_PORT']
missing_env_vars = []
for var in required_env_vars:
    if not os.getenv(var):
        missing_env_vars.append(var)

if missing_env_vars:
    print(f"\nFaltan las siguientes variables de entorno: {', '.join(missing_env_vars)}")
else:
    print("✅ Todas las variables de entorno están presentes")

# Verificar dependencias
print("\nVerificando dependencias:")
try:
    import django
    print("✅ Django instalado")
except ImportError:
    print("❌ Django no está instalado")

try:
    import dotenv
    print("✅ python-dotenv instalado")
except ImportError:
    print("❌ python-dotenv no está instalado")

# Verificar configuración de Django
print("\nVerificando configuración de Django:")
try:
    from django.conf import settings
    print("✅ Configuración de Django accesible")
except Exception as e:
    print(f"❌ Error en la configuración de Django: {str(e)}")

print("\nVerificación completada. Por favor, revisa los mensajes de error y corrige los problemas encontrados.")
