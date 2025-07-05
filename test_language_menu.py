#!/usr/bin/env python3
"""
Test script for the language menu functionality
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

def main():
    print("🎯 Iniciando prueba del menú de idioma...")
    
    # Verificar que estamos en el directorio correcto
    if not Path("manage.py").exists():
        print("❌ Error: No se encontró manage.py. Asegúrate de estar en el directorio del proyecto.")
        return
    
    # Verificar que el servidor no esté corriendo
    try:
        import requests
        response = requests.get("http://127.0.0.1:8000/", timeout=1)
        print("⚠️  El servidor ya está corriendo en el puerto 8000")
    except:
        print("🚀 Iniciando servidor Django...")
        try:
            # Iniciar el servidor en segundo plano
            subprocess.Popen([
                "python3", "manage.py", "runserver", "127.0.0.1:8000"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(3)  # Esperar a que el servidor inicie
        except Exception as e:
            print(f"❌ Error al iniciar el servidor: {e}")
            return
    
    print("🌐 Abriendo navegador...")
    
    # URLs a abrir
    urls = [
        "http://127.0.0.1:8000/users/",
        "http://127.0.0.1:8000/workcenter/"
    ]
    
    for url in urls:
        print(f"📱 Abriendo: {url}")
        try:
            webbrowser.open(url)
            time.sleep(1)
        except Exception as e:
            print(f"❌ Error al abrir {url}: {e}")
    
    print("✅ Navegador abierto exitosamente!")
    print("📋 URLs abiertas:")
    for url in urls:
        print(f"  - {url}")
    
    print("\n🔧 Funcionalidades del menú de idioma a probar:")
    print("  1. Verificar que el selector de idioma aparezca en el sidebar")
    print("  2. Hacer clic en el botón del idioma para abrir el menú")
    print("  3. Seleccionar 'Español' y verificar que se mantenga seleccionado")
    print("  4. Seleccionar 'English' y verificar que cambie la selección")
    print("  5. Verificar que aparezca la notificación de cambio de idioma")
    print("  6. Verificar que la preferencia se guarde en localStorage")
    print("  7. Recargar la página y verificar que se mantenga la selección")
    print("  8. Hacer clic fuera del menú para cerrarlo")
    
    print("\n🎨 Características del menú de idioma:")
    print("  - Selector elegante en el sidebar")
    print("  - Icono de globo para identificar el menú")
    print("  - Banderas de países (🇪🇸 y 🇺🇸)")
    print("  - Check marks para mostrar la selección actual")
    print("  - Animaciones suaves al abrir/cerrar")
    print("  - Notificaciones de confirmación")
    print("  - Persistencia de la selección")
    print("  - Cierre automático al hacer clic fuera")
    
    print("\n📊 Opciones disponibles:")
    print("  🇪🇸 Español (predeterminado)")
    print("  🇺🇸 English")
    
    print("\n✨ Ventajas del menú de idioma:")
    print("  ✅ Interfaz intuitiva y fácil de usar")
    print("  ✅ Diseño consistente con el resto de la aplicación")
    print("  ✅ Feedback visual inmediato")
    print("  ✅ Persistencia de preferencias")
    print("  ✅ Animaciones suaves y profesionales")
    print("  ✅ Accesible desde cualquier página")
    print("  ✅ Preparado para futuras implementaciones de i18n")
    
    print("\n🔮 Funcionalidades futuras que se pueden implementar:")
    print("  - Traducción completa de la interfaz")
    print("  - Cambio dinámico de idioma sin recargar")
    print("  - Más idiomas (Francés, Alemán, etc.)")
    print("  - Detección automática del idioma del navegador")
    print("  - Configuración de idioma por usuario")
    
    print("\n⏰ El servidor seguirá ejecutándose. Presiona Ctrl+C para detener.")
    print("💡 Consejo: Prueba cambiar entre idiomas varias veces para ver las animaciones!")

if __name__ == "__main__":
    main() 