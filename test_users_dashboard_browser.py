#!/usr/bin/env python3
"""
Script para abrir el navegador y probar el dashboard de usuarios mejorado con tarjetas centradas.
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
    """Abre el navegador con las páginas de usuarios"""
    base_url = "http://127.0.0.1:8000"
    
    print("🌐 Abriendo navegador...")
    
    # URLs para probar
    urls = [
        f"{base_url}/users/",
        f"{base_url}/users/roles/new/",
        f"{base_url}/users/users/new/",
    ]
    
    for url in urls:
        print(f"📱 Abriendo: {url}")
        webbrowser.open(url)
        time.sleep(1)  # Pequeña pausa entre aperturas

def main():
    """Función principal"""
    print("🎯 Iniciando prueba del dashboard de usuarios mejorado...")
    
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
        print("  - Dashboard Usuarios: http://127.0.0.1:8000/users/")
        print("  - Crear Rol: http://127.0.0.1:8000/users/roles/new/")
        print("  - Crear Usuario: http://127.0.0.1:8000/users/users/new/")
        
        print("\n🔧 Funcionalidades a probar:")
        print("  1. Verificar que las tarjetas estén centradas")
        print("  2. Verificar el diseño responsivo en diferentes pantallas")
        print("  3. Verificar las estadísticas en la parte superior")
        print("  4. Verificar los estados vacíos con mensajes informativos")
        print("  5. Verificar las acciones rápidas centradas")
        print("  6. Verificar los hover effects y transiciones")
        print("  7. Verificar la navegación entre secciones")
        
        print("\n🎨 Características visuales:")
        print("  - Header centrado con título y descripción")
        print("  - Estadísticas en tarjetas con iconos")
        print("  - Tarjetas de roles y usuarios centradas")
        print("  - Gradientes en los headers de las tarjetas")
        print("  - Iconos descriptivos para cada sección")
        print("  - Estados vacíos con mensajes y botones de acción")
        print("  - Acciones rápidas centradas en la parte inferior")
        print("  - Diseño responsivo (1 columna móvil, 2 desktop)")
        
        print("\n📱 Responsive design:")
        print("  - Móvil: 1 columna, tarjetas apiladas")
        print("  - Desktop: 2 columnas, tarjetas lado a lado")
        print("  - Espaciado adaptativo")
        print("  - Texto y elementos centrados")
        
        print("\n🔗 Navegación disponible:")
        print("  - Crear nuevo rol")
        print("  - Crear nuevo usuario")
        print("  - Editar roles existentes")
        print("  - Editar usuarios existentes")
        
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