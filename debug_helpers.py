#!/usr/bin/env python3
"""
Scripts de ayuda para debugging y captura de errores.
"""

import os
import sys
import subprocess
import json
import requests
from urllib.request import urlopen
from urllib.error import URLError

def check_server_status():
    """Verifica el estado del servidor Django."""
    print("=== Verificación del Servidor ===\n")
    
    try:
        response = requests.get("http://127.0.0.1:8000/", timeout=5)
        print(f"✅ Servidor activo - Status: {response.status_code}")
        print(f"📊 Headers: {dict(response.headers)}")
        return True
    except requests.exceptions.ConnectionError:
        print("❌ Servidor no está corriendo")
        print("💡 Ejecuta: python3 manage.py runserver")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_all_urls():
    """Prueba todas las URLs importantes."""
    print("=== Prueba de URLs ===\n")
    
    urls = [
        ("Home", "/"),
        ("Dashboard", "/workcenter/"),
        ("Lista Aulas", "/workcenter/classrooms/"),
        ("Lista Centros", "/workcenter/workcenters/"),
        ("Admin", "/admin/"),
        ("Login", "/login/"),
    ]
    
    for name, path in urls:
        url = f"http://127.0.0.1:8000{path}"
        try:
            response = requests.get(url, timeout=5)
            status = response.status_code
            if status == 200:
                print(f"✅ {name}: {status}")
            elif status == 302:
                print(f"🔄 {name}: {status} (Redirect)")
            elif status == 404:
                print(f"❌ {name}: {status} (Not Found)")
            else:
                print(f"⚠️  {name}: {status}")
        except Exception as e:
            print(f"❌ {name}: Error - {e}")

def generate_error_report():
    """Genera un reporte de errores común."""
    print("=== Reporte de Errores Comunes ===\n")
    
    common_errors = {
        "NoReverseMatch": "URL no encontrada en urls.py",
        "TemplateDoesNotExist": "Template no encontrado",
        "FieldError": "Campo no existe en el modelo",
        "IntegrityError": "Error de integridad en la base de datos",
        "PermissionDenied": "Usuario no tiene permisos",
        "404": "Página no encontrada",
        "500": "Error interno del servidor",
    }
    
    print("🔍 Errores comunes y soluciones:")
    for error, solution in common_errors.items():
        print(f"  • {error}: {solution}")
    
    print(f"\n📋 Información útil para debugging:")
    print(f"  • Logs del servidor: Revisa la terminal donde corre Django")
    print(f"  • Base de datos: python3 manage.py dbshell")
    print(f"  • Migraciones: python3 manage.py showmigrations")
    print(f"  • URLs: python3 manage.py show_urls")

def open_browser_with_debug():
    """Abre el navegador con herramientas de debug."""
    print("=== Abriendo Navegador con Debug ===\n")
    
    # Abrir navegador con herramientas de desarrollador
    debug_url = "http://127.0.0.1:8000/workcenter/"
    
    try:
        # En macOS, abrir con Safari Developer Tools
        subprocess.run(['open', '-a', 'Safari', debug_url])
        print("✅ Safari abierto con herramientas de desarrollador")
        print("💡 Presiona Cmd+Option+I para abrir las herramientas")
    except:
        try:
            # Abrir con Chrome DevTools
            subprocess.run(['open', '-a', 'Google Chrome', debug_url])
            print("✅ Chrome abierto")
            print("💡 Presiona F12 para abrir las herramientas de desarrollador")
        except:
            print("❌ No se pudo abrir el navegador automáticamente")
            print(f"💡 Abre manualmente: {debug_url}")

if __name__ == "__main__":
    print("🛠️  Herramientas de Debugging para PRIA\n")
    
    # Verificar servidor
    if check_server_status():
        # Probar URLs
        test_all_urls()
        
        # Generar reporte
        generate_error_report()
        
        # Abrir navegador
        open_browser_with_debug()
    
    print(f"\n📝 Para reportar errores:")
    print(f"1. Copia el mensaje de error exacto")
    print(f"2. Incluye la URL donde ocurrió")
    print(f"3. Describe los pasos que seguiste")
    print(f"4. Adjunta capturas de pantalla si es necesario") 