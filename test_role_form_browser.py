#!/usr/bin/env python3
"""
Script para abrir el navegador y probar el formulario de roles mejorado con pestañas.
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
    """Abre el navegador con las páginas de roles"""
    base_url = "http://127.0.0.1:8000"
    
    print("🌐 Abriendo navegador...")
    
    # URLs para probar
    urls = [
        f"{base_url}/users/roles/new/",
        f"{base_url}/users/",
    ]
    
    for url in urls:
        print(f"📱 Abriendo: {url}")
        webbrowser.open(url)
        time.sleep(1)  # Pequeña pausa entre aperturas

def main():
    """Función principal"""
    print("🎯 Iniciando prueba del formulario de roles mejorado...")
    
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
        print("  - Crear Rol: http://127.0.0.1:8000/users/roles/new/")
        print("  - Dashboard Usuarios: http://127.0.0.1:8000/users/")
        
        print("\n🔧 Funcionalidades a probar:")
        print("  1. Verificar que las pestañas se muestren correctamente")
        print("  2. Navegar entre las diferentes pestañas de módulos")
        print("  3. Verificar que los permisos estén organizados por módulo")
        print("  4. Verificar que los iconos se muestren para cada tipo de permiso")
        print("  5. Seleccionar permisos de diferentes módulos")
        print("  6. Verificar que el formulario funcione correctamente")
        
        print("\n📊 Módulos disponibles:")
        print("  - Admin (Logentry)")
        print("  - Auth (Group, Permission, User)")
        print("  - Contenttypes (Contenttype)")
        print("  - Sessions (Session)")
        print("  - Core (Carrera, Userprofile, Materia, Docente, Curso, Alumno, Matricula)")
        print("  - Users (Role, User)")
        print("  - Alumnos (Alumno)")
        print("  - Docentes (Docente)")
        print("  - Asistencia (Asistencia)")
        print("  - Workcenter (Schoolcycle, Workcenter, Schoolperiod, Classroom, Schoolcycleconfig)")
        
        print("\n🎨 Características visuales:")
        print("  - Pestañas con iconos y nombres legibles")
        print("  - Permisos organizados en grid responsivo")
        print("  - Iconos de colores para cada tipo de permiso")
        print("  - Animaciones suaves al cambiar pestañas")
        print("  - Interfaz moderna y intuitiva")
        
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