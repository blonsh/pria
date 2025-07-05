#!/usr/bin/env python3
"""
Script para abrir el navegador y probar la visibilidad de los botones.
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

def test_buttons_browser():
    """Abre el navegador para probar la visibilidad de los botones."""
    
    print("=== Probando Visibilidad de Botones en el Navegador ===\n")
    
    # Obtener un ciclo para editar
    cycle = SchoolCycle.objects.first()
    
    if not cycle:
        print("❌ No hay ciclos escolares disponibles.")
        print("   Ejecuta primero: python3 create_sample_data.py")
        return
    
    # URLs a probar
    urls = [
        "http://127.0.0.1:8000/workcenter/schoolcycles/",
        f"http://127.0.0.1:8000/workcenter/schoolcycles/{cycle.pk}/edit/",
    ]
    
    print("🌐 Abriendo navegador para probar:")
    print(f"  1. Lista de ciclos: {urls[0]}")
    print(f"  2. Editar ciclo '{cycle.name}': {urls[1]}")
    
    # Abrir cada URL
    for i, url in enumerate(urls, 1):
        print(f"\n📱 Abriendo {i}/2: {url}")
        webbrowser.open(url)
        time.sleep(3)  # Pausa entre aperturas
    
    print(f"\n✅ Navegador abierto para verificar botones")
    print(f"   Verifica lo siguiente:")
    print(f"   • En la lista de ciclos, busca botones azules 'Editar'")
    print(f"   • Los botones deben tener fondo azul y texto blanco")
    print(f"   • Haz clic en 'Editar' para ir al formulario")
    print(f"   • En el formulario, busca el botón púrpura 'Actualizar Ciclo'")
    print(f"   • Si no ves los botones, recarga la página (Ctrl+F5)")

if __name__ == '__main__':
    test_buttons_browser() 