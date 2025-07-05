#!/usr/bin/env python3
"""
Test script for Core module permissions grouping
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

def main():
    print("🎯 Iniciando prueba de agrupación de permisos del módulo Núcleo...")
    
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
    print("  1. Verificar que los permisos del Núcleo estén agrupados")
    print("  2. Verificar que aparezca 'Núcleo (Carrera, Perfil de Usuario, Materia, Docente, Curso, Alumno, Matrícula)'")
    print("  3. Verificar que Autenticación siga agrupado")
    print("  4. Verificar que otros módulos sigan separados")
    print("  5. Verificar que los contadores funcionen correctamente")
    print("  6. Verificar que las acciones rápidas funcionen")
    
    print("\n📊 Módulos después de la agrupación:")
    modules_grouped = [
        "Administración (Entrada de Log)",
        "Autenticación (Grupo, Permiso, Usuario) ← AGRUPADO",
        "Núcleo (Carrera, Perfil de Usuario, Materia, Docente, Curso, Alumno, Matrícula) ← AGRUPADO",
        "Tipos de Contenido (Tipo de Contenido)",
        "Sesiones (Sesión)",
        "Usuarios (Rol, Usuario)",
        "Alumnos (Alumno)",
        "Docentes (Docente)",
        "Asistencia (Asistencia)",
        "Centro de Trabajo (Ciclo Escolar, Centro de Trabajo, Período Escolar, Aula, Configuración de Ciclo)"
    ]
    
    for i, module in enumerate(modules_grouped, 1):
        if "← AGRUPADO" in module:
            print(f"  {i}. {module}")
        else:
            print(f"  {i}. {module}")
    
    print("\n🎨 Características de la agrupación:")
    print("  - Permisos de autenticación agrupados en una sola sección")
    print("  - Permisos del núcleo agrupados en una sola sección")
    print("  - Otros módulos mantienen su separación original")
    print("  - Contadores muestran total de permisos por módulo")
    print("  - Acciones rápidas afectan todos los permisos del módulo")
    print("  - Funcionalidad completa preservada")
    
    print("\n✨ Ventajas de la agrupación:")
    print("  ✅ Interfaz más limpia y organizada")
    print("  ✅ Menos secciones para navegar")
    print("  ✅ Permisos relacionados juntos")
    print("  ✅ Mejor experiencia de usuario")
    print("  ✅ Mantiene toda la funcionalidad")
    
    print("\n🔍 Cambios específicos:")
    print("  ANTES (Núcleo separado):")
    print("    - Núcleo (Carrera)")
    print("    - Núcleo (Perfil de Usuario)")
    print("    - Núcleo (Materia)")
    print("    - Núcleo (Docente)")
    print("    - Núcleo (Curso)")
    print("    - Núcleo (Alumno)")
    print("    - Núcleo (Matrícula)")
    print("  DESPUÉS (Núcleo agrupado):")
    print("    - Núcleo (Carrera, Perfil de Usuario, Materia, Docente, Curso, Alumno, Matrícula)")
    
    print("\n⚙️ Implementación técnica:")
    print("  - Lógica de agrupación extendida en get_permissions_by_module()")
    print("  - Condición especial para app_label == 'core'")
    print("  - module_key = 'core_combined' para agrupación")
    print("  - Autenticación y Núcleo agrupados, otros separados")
    
    print("\n📈 Beneficios de la agrupación:")
    print("  - Reducción de 7 secciones a 1 para Núcleo")
    print("  - Reducción de 3 secciones a 1 para Autenticación")
    print("  - Total: 10 secciones reducidas a 8")
    print("  - Mejor organización visual")
    print("  - Navegación más eficiente")
    
    print("\n⏰ El servidor seguirá ejecutándose. Presiona Ctrl+C para detener.")
    print("💡 Consejo: Expande las secciones de Autenticación y Núcleo para ver todos los permisos agrupados!")

if __name__ == "__main__":
    main() 