#!/usr/bin/env python3
"""
Script para probar el contador de caracteres en el formulario de roles.
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

def main():
    print("🎯 Iniciando prueba del contador de caracteres...")
    
    # Verificar que estamos en el directorio correcto
    if not Path('manage.py').exists():
        print("❌ Error: No se encontró manage.py. Asegúrate de estar en el directorio del proyecto.")
        return
    
    # Iniciar el servidor Django
    print("🚀 Iniciando servidor Django...")
    try:
        server_process = subprocess.Popen([
            'python3', 'manage.py', 'runserver'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Esperar un momento para que el servidor se inicie
        time.sleep(3)
        
        # Abrir el navegador
        print("🌐 Abriendo navegador...")
        urls = [
            "http://127.0.0.1:8000/users/roles/new/",
            "http://127.0.0.1:8000/users/"
        ]
        
        for url in urls:
            print(f"📱 Abriendo: {url}")
            webbrowser.open(url)
            time.sleep(1)
        
        print("✅ Navegador abierto exitosamente!")
        print("📋 URLs abiertas:")
        print("  - Crear Rol: http://127.0.0.1:8000/users/roles/new/")
        print("  - Dashboard Usuarios: http://127.0.0.1:8000/users/")
        
        print("\n🔧 Funcionalidades a probar:")
        print("  1. Verificar que el contador de caracteres aparezca debajo del campo descripción")
        print("  2. Escribir en el campo descripción y verificar que el contador se actualice")
        print("  3. Probar diferentes longitudes:")
        print("     - 0-200 caracteres: Verde ✓ Disponible")
        print("     - 200-237 caracteres: Amarillo ⚠ Cuidado")
        print("     - 238-250 caracteres: Naranja ⚠ Casi lleno")
        print("     - Más de 250 caracteres: Rojo ✗ Excedido")
        print("  4. Verificar que el límite de 250 caracteres funcione en el formulario")
        print("  5. Probar que el mensaje de error aparezca si se excede el límite")
        
        print("\n📊 Características del contador:")
        print("  - Contador en tiempo real: X / 250 caracteres")
        print("  - Indicador visual de estado con colores")
        print("  - Validación en el servidor (máximo 250 caracteres)")
        print("  - Mensaje de error amigable si se excede")
        
        print("\n🎨 Estados visuales:")
        print("  - Verde: 0-200 caracteres (✓ Disponible)")
        print("  - Amarillo: 201-237 caracteres (⚠ Cuidado)")
        print("  - Naranja: 238-250 caracteres (⚠ Casi lleno)")
        print("  - Rojo: Más de 250 caracteres (✗ Excedido)")
        
        print("\n⏰ El servidor seguirá ejecutándose. Presiona Ctrl+C para detener.")
        
        # Mantener el script ejecutándose
        try:
            server_process.wait()
        except KeyboardInterrupt:
            print("\n🛑 Deteniendo servidor...")
            server_process.terminate()
            server_process.wait()
            print("✅ Servidor detenido.")
            
    except Exception as e:
        print(f"❌ Error al iniciar el servidor: {e}")
        if 'server_process' in locals():
            server_process.terminate()

if __name__ == '__main__':
    main() 