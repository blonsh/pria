#!/usr/bin/env python3
"""
Test script for Spanish module names in the role form
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

def main():
    print("🎯 Iniciando prueba de nombres de módulos en español...")
    
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
    
    print("\n🔧 Funcionalidades a verificar:")
    print("  1. Verificar que los nombres de módulos aparezcan en español")
    print("  2. Verificar que los nombres de modelos aparezcan en español")
    print("  3. Verificar que el acordeón muestre los nombres traducidos")
    print("  4. Verificar que los contadores funcionen correctamente")
    print("  5. Verificar que las acciones rápidas funcionen")
    
    print("\n📊 Módulos traducidos al español:")
    modules_spanish = [
        "Administración (Entrada de Log)",
        "Autenticación (Grupo, Permiso, Usuario)",
        "Tipos de Contenido (Tipo de Contenido)",
        "Sesiones (Sesión)",
        "Núcleo (Carrera, Perfil de Usuario, Materia, Docente, Curso, Alumno, Matrícula)",
        "Usuarios (Rol, Usuario)",
        "Alumnos (Alumno)",
        "Docentes (Docente)",
        "Asistencia (Asistencia)",
        "Centro de Trabajo (Ciclo Escolar, Centro de Trabajo, Período Escolar, Aula, Configuración de Ciclo)"
    ]
    
    for i, module in enumerate(modules_spanish, 1):
        print(f"  {i}. {module}")
    
    print("\n🎨 Características de la traducción:")
    print("  - Nombres de módulos en español")
    print("  - Nombres de modelos en español")
    print("  - Mantiene la funcionalidad del acordeón")
    print("  - Contadores y acciones siguen funcionando")
    print("  - Diseño y UX se mantienen igual")
    
    print("\n✨ Ventajas de la traducción:")
    print("  ✅ Interfaz completamente en español")
    print("  ✅ Mejor comprensión para usuarios hispanohablantes")
    print("  ✅ Nombres más descriptivos y claros")
    print("  ✅ Consistencia con el resto de la aplicación")
    print("  ✅ Mantiene toda la funcionalidad original")
    
    print("\n🔍 Traducciones específicas:")
    translations = {
        "admin": "Administración",
        "auth": "Autenticación", 
        "contenttypes": "Tipos de Contenido",
        "sessions": "Sesiones",
        "core": "Núcleo",
        "users": "Usuarios",
        "alumnos": "Alumnos",
        "docentes": "Docentes",
        "asistencia": "Asistencia",
        "workcenter": "Centro de Trabajo"
    }
    
    print("  Módulos:")
    for eng, esp in translations.items():
        print(f"    {eng} → {esp}")
    
    print("\n  Modelos principales:")
    model_translations = {
        "logentry": "Entrada de Log",
        "group": "Grupo",
        "permission": "Permiso", 
        "user": "Usuario",
        "carrera": "Carrera",
        "materia": "Materia",
        "docente": "Docente",
        "alumno": "Alumno",
        "schoolcycle": "Ciclo Escolar",
        "workcenter": "Centro de Trabajo",
        "classroom": "Aula"
    }
    
    for eng, esp in model_translations.items():
        print(f"    {eng} → {esp}")
    
    print("\n⏰ El servidor seguirá ejecutándose. Presiona Ctrl+C para detener.")
    print("💡 Consejo: Expande diferentes módulos para ver los nombres en español!")

if __name__ == "__main__":
    main() 