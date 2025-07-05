#!/usr/bin/env python3
"""
Script para abrir el navegador y probar la funcionalidad de configuración de ciclos.
"""

import webbrowser
import time
import subprocess
import sys
import os

def start_server():
    """Inicia el servidor Django"""
    print("🚀 Iniciando servidor Django...")
    try:
        # Iniciar el servidor en segundo plano
        process = subprocess.Popen(
            ["python3", "manage.py", "runserver"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Esperar un momento para que el servidor se inicie
        time.sleep(3)
        
        return process
    except Exception as e:
        print(f"❌ Error al iniciar el servidor: {e}")
        return None

def open_browser():
    """Abre el navegador con las páginas de configuración de ciclos"""
    base_url = "http://127.0.0.1:8000"
    
    print("🌐 Abriendo navegador...")
    
    # URLs para probar
    urls = [
        f"{base_url}/workcenter/cycle-config/",
        f"{base_url}/workcenter/schoolcycles/",
        f"{base_url}/workcenter/",
    ]
    
    for url in urls:
        print(f"📱 Abriendo: {url}")
        webbrowser.open(url)
        time.sleep(1)  # Pequeña pausa entre aperturas

def main():
    """Función principal"""
    print("🎯 Iniciando prueba de configuración de ciclos en navegador...")
    
    # Iniciar servidor
    server_process = start_server()
    
    if server_process is None:
        print("❌ No se pudo iniciar el servidor")
        sys.exit(1)
    
    try:
        # Abrir navegador
        open_browser()
        
        print("\n✅ Navegador abierto exitosamente!")
        print("\n📋 URLs abiertas:")
        print("  - Configuración de ciclos: http://127.0.0.1:8000/workcenter/cycle-config/")
        print("  - Lista de ciclos: http://127.0.0.1:8000/workcenter/schoolcycles/")
        print("  - Dashboard: http://127.0.0.1:8000/workcenter/")
        
        print("\n🔧 Funcionalidades a probar:")
        print("  1. Ver configuración de ciclos por centro de trabajo")
        print("  2. Editar configuración de un centro específico")
        print("  3. Gestionar activación manual de ciclos")
        print("  4. Ver ciclos activos por configuración en la lista")
        print("  5. Navegar desde el dashboard a la configuración")
        
        print("\n⏰ El servidor seguirá ejecutándose. Presiona Ctrl+C para detener.")
        
        # Mantener el script ejecutándose
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Deteniendo servidor...")
            server_process.terminate()
            print("✅ Servidor detenido")
            
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")
        if server_process:
            server_process.terminate()
        sys.exit(1)

if __name__ == "__main__":
    main() 