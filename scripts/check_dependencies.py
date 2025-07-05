import os
import sys
import subprocess
from pathlib import Path

print("Verificando dependencias del proyecto...")

# Verificar estructura de directorios
def check_directory_structure():
    print("\nVerificando estructura de directorios:")
    project_dir = Path(__file__).resolve().parent.parent
    required_dirs = ['core', 'manage.py', 'requirements.txt']
    
    for dir in required_dirs:
        if not (project_dir / dir).exists():
            print(f"❌ Falta el directorio: {dir}")
        else:
            print(f"✅ Directorio encontrado: {dir}")

# Verificar dependencias instaladas
def check_installed_packages():
    print("\nVerificando dependencias instaladas:")
    required_packages = ['django', 'python-dotenv', 'psycopg2-binary']
    
    try:
        result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
        installed_packages = result.stdout.lower()
        
        for pkg in required_packages:
            if pkg.lower() in installed_packages:
                print(f"✅ {pkg} está instalado")
            else:
                print(f"❌ {pkg} NO está instalado")
    except Exception as e:
        print(f"❌ Error al verificar paquetes: {str(e)}")

# Verificar configuración de entorno
def check_environment():
    print("\nVerificando configuración de entorno:")
    required_env_vars = ['SECRET_KEY', 'DB_NAME', 'DB_USER', 'DB_PASSWORD', 'DB_HOST', 'DB_PORT']
    
    for var in required_env_vars:
        if os.getenv(var):
            print(f"✅ Variable de entorno {var} está configurada")
        else:
            print(f"❌ Variable de entorno {var} NO está configurada")

# Verificar versiones de Python
def check_python_version():
    print("\nVerificando versión de Python:")
    try:
        result = subprocess.run(['python3', '--version'], capture_output=True, text=True)
        print(f"✅ Versión de Python: {result.stdout.strip()}")
    except Exception as e:
        print(f"❌ Error al verificar Python: {str(e)}")

# Ejecutar todas las verificaciones
def main():
    check_directory_structure()
    check_installed_packages()
    check_environment()
    check_python_version()

if __name__ == '__main__':
    main()
