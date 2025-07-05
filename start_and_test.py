#!/usr/bin/env python3
"""
Script para iniciar el servidor Django y abrir el navegador automáticamente.
"""

import os
import sys
import subprocess
import time
import signal
import webbrowser
from urllib.request import urlopen
from urllib.error import URLError

def wait_for_server(url, timeout=30):
    """Espera a que el servidor esté disponible."""
    print(f"⏳ Esperando a que el servidor esté disponible en {url}...")
    
    for i in range(timeout):
        try:
            response = urlopen(url, timeout=2)
            if response.getcode() == 200 or response.getcode() == 302:
                print(f"✅ Servidor disponible después de {i+1} segundos")
                return True
        except:
            pass
        time.sleep(1)
    
    print(f"❌ Timeout: El servidor no respondió en {timeout} segundos")
    return False

def start_server_and_browser():
    """Inicia el servidor Django y abre el navegador."""
    
    print("=== Iniciando Servidor y Navegador ===\n")
    
    # Verificar si el servidor ya está corriendo
    try:
        response = urlopen("http://127.0.0.1:8000/", timeout=2)
        print("⚠️  El servidor ya está corriendo en el puerto 8000")
        server_running = True
    except:
        print("🚀 Iniciando servidor Django...")
        server_running = False
    
    if not server_running:
        try:
            # Iniciar servidor en background
            server_process = subprocess.Popen([
                'python3', 'manage.py', 'runserver'
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Esperar a que el servidor esté listo
            if wait_for_server("http://127.0.0.1:8000/"):
                print("✅ Servidor iniciado correctamente")
            else:
                print("❌ Error al iniciar el servidor")
                return
                
        except Exception as e:
            print(f"❌ Error al iniciar servidor: {e}")
            return
    
    # URLs para probar
    test_urls = [
        ("Dashboard", "http://127.0.0.1:8000/workcenter/"),
        ("Lista de Aulas", "http://127.0.0.1:8000/workcenter/classrooms/"),
        ("Lista de Centros", "http://127.0.0.1:8000/workcenter/workcenters/"),
        ("Admin", "http://127.0.0.1:8000/admin/"),
    ]
    
    print(f"\n🔍 Probando URLs...")
    for name, url in test_urls:
        try:
            response = urlopen(url, timeout=5)
            status = response.getcode()
            print(f"✅ {name}: {status}")
        except Exception as e:
            print(f"❌ {name}: Error - {e}")
    
    print(f"\n🌐 Abriendo navegador...")
    
    # Abrir navegador
    try:
        webbrowser.open('http://127.0.0.1:8000/workcenter/')
        print("✅ Navegador abierto en el dashboard")
    except Exception as e:
        print(f"❌ Error al abrir navegador: {e}")
        print("💡 Abre manualmente: http://127.0.0.1:8000/workcenter/")
    
    print(f"\n📋 Guía de Testing:")
    print(f"1. Navega por las diferentes secciones")
    print(f"2. Prueba crear, editar y ver elementos")
    print(f"3. Reporta cualquier error que encuentres")
    
    print(f"\n🔗 URLs principales:")
    for name, url in test_urls:
        print(f"  • {name}: {url}")
    
    print(f"\n🛠️  Herramientas de debugging:")
    print(f"  • F12: Herramientas de desarrollador")
    print(f"  • Ctrl+Shift+I: Inspeccionar elemento")
    print(f"  • Ctrl+Shift+C: Seleccionar elemento")
    print(f"  • Ctrl+R: Recargar página")
    
    print(f"\n📝 Para reportar errores:")
    print(f"  • Copia la URL completa")
    print(f"  • Copia el mensaje de error")
    print(f"  • Describe los pasos que seguiste")
    print(f"  • Incluye capturas de pantalla si es necesario")

if __name__ == "__main__":
    start_server_and_browser() 