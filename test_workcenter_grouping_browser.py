#!/usr/bin/env python3
"""
Script para probar el agrupamiento del módulo workcenter en el navegador.
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

def main():
    print("🎯 Iniciando prueba del agrupamiento de Centro de Trabajo...")
    
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
        print("  1. Verificar que 'Centro de Trabajo' aparezca como una sola sección")
        print("  2. Expandir la sección 'Centro de Trabajo'")
        print("  3. Verificar que incluya todos los modelos:")
        print("     - Aula")
        print("     - Ciclo Escolar") 
        print("     - Configuración de Ciclo")
        print("     - Período Escolar")
        print("     - Centro de Trabajo")
        print("  4. Verificar que no haya secciones separadas para cada modelo")
        print("  5. Probar la selección de permisos de diferentes tipos")
        
        print("\n📊 Módulos agrupados esperados:")
        print("  - Autenticación (Group, Permission, User)")
        print("  - Núcleo (Carrera, Perfil de Usuario, Materia, Docente, Curso, Alumno, Matrícula)")
        print("  - Centro de Trabajo (Aula, Ciclo Escolar, Configuración de Ciclo, Período Escolar, Centro de Trabajo)")
        print("  - Otros módulos separados por modelo")
        
        print("\n🎨 Características visuales:")
        print("  - Sección 'Centro de Trabajo' con contador de permisos")
        print("  - Permisos organizados en grid responsivo")
        print("  - Iconos de colores para cada tipo de permiso")
        print("  - Animaciones suaves al expandir/contraer")
        print("  - Interfaz moderna y intuitiva")
        
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