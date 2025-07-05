import os
import shutil
from pathlib import Path

print("Reorganizando estructura del proyecto...")

# Directorios
project_dir = Path(__file__).resolve().parent.parent
old_settings_dir = project_dir / 'pria'
new_settings_dir = project_dir / 'core' / 'settings'

# Verificar si el directorio pria existe
if old_settings_dir.exists():
    print("\nEliminando directorio pria redundante...")
    try:
        shutil.rmtree(old_settings_dir)
        print("✅ Directorio pria eliminado")
    except Exception as e:
        print(f"❌ Error al eliminar pria: {str(e)}")
else:
    print("✅ Directorio pria no existe (ya eliminado)")

# Verificar y actualizar manage.py
manage_py = project_dir / 'manage.py'
if manage_py.exists():
    print("\nActualizando manage.py...")
    try:
        with open(manage_py, 'r') as f:
            content = f.read()
        
        # Actualizar la línea de DJANGO_SETTINGS_MODULE
        new_content = content.replace('pria.settings', 'core.settings')
        
        with open(manage_py, 'w') as f:
            f.write(new_content)
        
        print("✅ manage.py actualizado")
    except Exception as e:
        print(f"❌ Error al actualizar manage.py: {str(e)}")

# Verificar que la estructura core esté completa
required_core_files = ['settings', 'urls.py', 'wsgi.py']
missing_core_files = []
for file in required_core_files:
    if not (new_settings_dir / file).exists():
        missing_core_files.append(file)

if missing_core_files:
    print(f"\n⚠️ Faltan archivos en core: {', '.join(missing_core_files)}")
else:
    print("✅ Estructura core completa")

print("\nReorganización completada. Por favor, revisa los mensajes y asegúrate de que todo esté correcto.")
