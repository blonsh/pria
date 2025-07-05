#!/usr/bin/env python3
"""
Test script for the new accordion role form functionality
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

def main():
    print("🎯 Iniciando prueba del formulario de roles con acordeón...")
    
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
        "http://127.0.0.1:8000/users/roles/new/",
        "http://127.0.0.1:8000/users/"
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
    
    print("\n🔧 Funcionalidades a probar:")
    print("  1. Verificar que el acordeón se muestre correctamente")
    print("  2. Expandir y contraer diferentes módulos")
    print("  3. Verificar que los contadores se actualicen al seleccionar permisos")
    print("  4. Probar los botones de selección masiva:")
    print("     - Seleccionar todos")
    print("     - Deseleccionar todos")
    print("     - Solo ver")
    print("  5. Verificar que el resumen total se actualice")
    print("  6. Probar las animaciones suaves del acordeón")
    print("  7. Verificar que los iconos roten correctamente")
    print("  8. Probar la navegación entre módulos")
    
    print("\n🎨 Características del acordeón:")
    print("  - Organización jerárquica por módulos")
    print("  - Contadores de permisos seleccionados por módulo")
    print("  - Resumen total de permisos")
    print("  - Botones de acción rápida por módulo")
    print("  - Animaciones suaves de expansión/contracción")
    print("  - Iconos que rotan al expandir")
    print("  - Hover effects en los elementos")
    print("  - Diseño responsivo y moderno")
    
    print("\n📊 Módulos disponibles en el acordeón:")
    modules = [
        "Admin (Logentry)",
        "Auth (Group, Permission, User)", 
        "Contenttypes (Contenttype)",
        "Sessions (Session)",
        "Core (Carrera, Userprofile, Materia, Docente, Curso, Alumno, Matricula)",
        "Users (Role, User)",
        "Alumnos (Alumno)",
        "Docentes (Docente)",
        "Asistencia (Asistencia)",
        "Workcenter (Schoolcycle, Workcenter, Schoolperiod, Classroom, Schoolcycleconfig)"
    ]
    
    for i, module in enumerate(modules, 1):
        print(f"  {i}. {module}")
    
    print("\n✨ Ventajas del sistema de acordeón:")
    print("  ✅ Mejor organización visual")
    print("  ✅ Jerarquía clara de módulos")
    print("  ✅ Contadores en tiempo real")
    print("  ✅ Acciones rápidas por módulo")
    print("  ✅ Animaciones suaves")
    print("  ✅ Mejor UX para muchos permisos")
    print("  ✅ Diseño más limpio y profesional")
    
    print("\n⏰ El servidor seguirá ejecutándose. Presiona Ctrl+C para detener.")
    print("💡 Consejo: Prueba expandir diferentes módulos y ver cómo se comportan los contadores!")

if __name__ == "__main__":
    main() 