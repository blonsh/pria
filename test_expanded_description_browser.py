#!/usr/bin/env python3
"""
Script para probar el campo descripción ampliado en el formulario de roles.
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

def main():
    print("🎯 Iniciando prueba del campo descripción ampliado...")
    
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
        print("  1. Verificar que el campo descripción sea un Textarea (área de texto)")
        print("  2. Verificar que tenga 4 filas de altura por defecto")
        print("  3. Probar que se pueda escribir texto largo")
        print("  4. Verificar que el contador muestre 'X / 1000 caracteres'")
        print("  5. Probar diferentes longitudes:")
        print("     - 0-800 caracteres: Verde ✓ Disponible")
        print("     - 801-950 caracteres: Amarillo ⚠ Cuidado")
        print("     - 951-1000 caracteres: Naranja ⚠ Casi lleno")
        print("     - Más de 1000 caracteres: Rojo ✗ Excedido")
        print("  6. Verificar que se pueda hacer scroll dentro del textarea")
        print("  7. Probar que el placeholder aparezca correctamente")
        print("  8. Verificar que la validación funcione en el servidor")
        
        print("\n📊 Características del campo ampliado:")
        print("  - Tipo: Textarea (área de texto)")
        print("  - Altura: 4 filas por defecto")
        print("  - Límite: 1000 caracteres")
        print("  - Scroll automático cuando el contenido excede la altura")
        print("  - Placeholder descriptivo")
        print("  - Contador en tiempo real")
        print("  - Validación visual con colores")
        
        print("\n🎨 Estados visuales del contador:")
        print("  - Verde: 0-800 caracteres (✓ Disponible)")
        print("  - Amarillo: 801-950 caracteres (⚠ Cuidado)")
        print("  - Naranja: 951-1000 caracteres (⚠ Casi lleno)")
        print("  - Rojo: Más de 1000 caracteres (✗ Excedido)")
        
        print("\n💡 Ventajas del campo ampliado:")
        print("  - Permite descripciones detalladas y completas")
        print("  - Mejor visualización del texto largo")
        print("  - Scroll interno para navegar por el contenido")
        print("  - Mantiene la validación y contador visual")
        print("  - Experiencia de usuario mejorada")
        
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