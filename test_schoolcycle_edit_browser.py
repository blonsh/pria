#!/usr/bin/env python3
"""
Script para abrir el navegador y probar la funcionalidad de edición de ciclos escolares.
"""

import webbrowser
import time
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from workcenter.models import SchoolCycle

def test_schoolcycle_edit_browser():
    """Abre el navegador para probar la funcionalidad de edición de ciclos escolares."""
    
    print("=== Probando Funcionalidad de Edición de Ciclos Escolares en el Navegador ===\n")
    
    # Obtener un ciclo para editar
    cycle = SchoolCycle.objects.first()
    
    if not cycle:
        print("❌ No hay ciclos escolares disponibles para editar.")
        print("   Ejecuta primero: python3 create_sample_data.py")
        return
    
    # URLs a probar
    urls = [
        "http://127.0.0.1:8000/workcenter/schoolcycles/",
        f"http://127.0.0.1:8000/workcenter/schoolcycles/{cycle.pk}/edit/",
        "http://127.0.0.1:8000/workcenter/schoolcycles/new/",
    ]
    
    print("🌐 Abriendo navegador para probar:")
    print(f"  1. Lista de ciclos: {urls[0]}")
    print(f"  2. Editar ciclo '{cycle.name}': {urls[1]}")
    print(f"  3. Crear nuevo ciclo: {urls[2]}")
    
    # Abrir cada URL
    for i, url in enumerate(urls, 1):
        print(f"\n📱 Abriendo {i}/3: {url}")
        webbrowser.open(url)
        time.sleep(2)  # Pausa entre aperturas
    
    print(f"\n✅ Navegador abierto con las páginas de edición de ciclos")
    print(f"   Prueba las siguientes funcionalidades:")
    print(f"   • En la lista, haz clic en el icono de editar (lápiz)")
    print(f"   • En el formulario de edición, verifica la información del ciclo")
    print(f"   • Modifica algún campo y guarda los cambios")
    print(f"   • Verifica que te redirija a la lista de ciclos")
    print(f"   • Prueba la validación de formularios")
    print(f"   • Verifica los botones de navegación")

if __name__ == '__main__':
    test_schoolcycle_edit_browser() 