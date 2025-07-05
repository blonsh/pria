#!/usr/bin/env python3
"""
Test script to verify the home page is working correctly
"""

import requests
import time
import webbrowser
import subprocess
import sys
import os

def main():
    print("🎯 Verificando que la página principal funcione correctamente...")
    
    # Start Django server
    print("🚀 Iniciando servidor Django...")
    try:
        server_process = subprocess.Popen(
            ['python3', 'manage.py', 'runserver'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(3)  # Wait for server to start
        
        # Test the home page
        print("🌐 Probando la página principal...")
        response = requests.get('http://127.0.0.1:8000/', timeout=10)
        
        if response.status_code == 200:
            print("✅ Página principal cargada exitosamente!")
            print(f"📊 Status Code: {response.status_code}")
            
            # Check for key content
            content = response.text
            if "PRIA" in content and "Plataforma de Registro" in content:
                print("✅ Contenido principal encontrado")
            else:
                print("⚠️  Contenido principal no encontrado")
                
            # Open browser
            print("🌐 Abriendo navegador...")
            webbrowser.open('http://127.0.0.1:8000/')
            print("✅ Navegador abierto!")
            
        else:
            print(f"❌ Error al cargar la página: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    finally:
        # Clean up
        if 'server_process' in locals():
            server_process.terminate()
            print("🛑 Servidor detenido")

if __name__ == "__main__":
    main() 