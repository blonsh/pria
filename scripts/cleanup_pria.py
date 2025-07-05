import os
import shutil
from pathlib import Path

print("Limpiando estructura del proyecto...")

# Directorios
project_dir = Path(__file__).resolve().parent.parent
pria_dir = project_dir / 'pria'

# Verificar si el directorio pria existe
if pria_dir.exists():
    print("\nEliminando directorio pria redundante...")
    try:
        shutil.rmtree(pria_dir)
        print("✅ Directorio pria eliminado")
    except Exception as e:
        print(f"❌ Error al eliminar pria: {str(e)}")
else:
    print("✅ Directorio pria no existe (ya eliminado)")

# Verificar que la estructura core esté completa
required_core_files = [
    'settings',
    'urls.py',
    'wsgi.py',
    'apps.py',
    'models.py',
    'views.py',
    'templates'
]

print("\nVerificando estructura core...")
core_dir = project_dir / 'core'
missing_core_files = []

for file in required_core_files:
    if not (core_dir / file).exists():
        missing_core_files.append(file)

if missing_core_files:
    print(f"⚠️ Faltan archivos en core: {', '.join(missing_core_files)}")
else:
    print("✅ Estructura core completa")

print("\nLimpieza completada. Por favor, revisa los mensajes y asegúrate de que todo esté correcto.")
