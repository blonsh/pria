#!/usr/bin/env python3
"""
Script para abrir el navegador y probar la aplicación PRIA.
"""

import os
import sys
import subprocess
import time
import webbrowser
from urllib.request import urlopen
from urllib.error import URLError

def test_browser_access():
    """Prueba el acceso al navegador y captura errores."""
    
    print("=== Prueba de Acceso al Navegador ===\n")
    
    # URLs a probar
    urls_to_test = [
        "http://127.0.0.1:8000/",
        "http://127.0.0.1:8000/workcenter/",
        "http://127.0.0.1:8000/workcenter/classrooms/",
        "http://127.0.0.1:8000/workcenter/workcenters/",
        "http://127.0.0.1:8000/admin/",
    ]
    
    print("🔍 Probando conectividad con el servidor...")
    
    for url in urls_to_test:
        try:
            response = urlopen(url, timeout=5)
            status_code = response.getcode()
            print(f"✅ {url} - Status: {status_code}")
        except URLError as e:
            print(f"❌ {url} - Error: {e}")
        except Exception as e:
            print(f"⚠️  {url} - Error inesperado: {e}")
    
    print(f"\n🌐 Abriendo navegador...")
    
    # Abrir navegador en macOS
    try:
        # Opción 1: Usar el comando 'open'
        subprocess.run(['open', 'http://127.0.0.1:8000/workcenter/'], check=True)
        print("✅ Navegador abierto con 'open'")
    except subprocess.CalledProcessError:
        try:
            # Opción 2: Usar webbrowser
            webbrowser.open('http://127.0.0.1:8000/workcenter/')
            print("✅ Navegador abierto con webbrowser")
        except Exception as e:
            print(f"❌ Error al abrir navegador: {e}")
    
    print(f"\n📋 Instrucciones para reportar errores:")
    print(f"1. Navega por la aplicación en el navegador")
    print(f"2. Si encuentras errores, copia:")
    print(f"   - La URL completa")
    print(f"   - El mensaje de error")
    print(f"   - Una descripción de lo que estabas haciendo")
    print(f"3. Envíame la información en el chat")
    
    print(f"\n🔗 URLs principales para probar:")
    for i, url in enumerate(urls_to_test, 1):
        print(f"  {i}. {url}")
    
    print(f"\n💡 Consejos para debugging:")
    print(f"  • Usa F12 para abrir las herramientas de desarrollador")
    print(f"  • Revisa la pestaña 'Console' para errores JavaScript")
    print(f"  • Revisa la pestaña 'Network' para errores de red")
    print(f"  • Toma capturas de pantalla si es necesario")

if __name__ == "__main__":
    test_browser_access() 