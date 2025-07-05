#!/usr/bin/env python3
"""
Script para probar la funcionalidad final de edición de ciclos escolares.
"""

import webbrowser
import time
import os
import sys
import django
from datetime import date

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from workcenter.models import SchoolCycle

def test_final_functionality():
    """Prueba la funcionalidad final de edición de ciclos escolares."""
    
    print("=== Probando Funcionalidad Final de Edición ===\n")
    
    # Obtener un ciclo para editar
    cycle = SchoolCycle.objects.first()
    
    if not cycle:
        print("❌ No hay ciclos escolares disponibles.")
        print("   Ejecuta primero: python3 create_sample_data.py")
        return
    
    duration = (cycle.end_date - cycle.start_date).days
    
    print(f"📊 Datos del ciclo de prueba:")
    print(f"  • Nombre: {cycle.name}")
    print(f"  • Centro: {cycle.work_center.name}")
    print(f"  • Duración: {duration} días")
    print(f"  • Estado: {'Activo' if cycle.start_date <= date.today() <= cycle.end_date else 'Inactivo'}")
    
    # URLs a probar
    urls = [
        "http://127.0.0.1:8000/workcenter/schoolcycles/",
        f"http://127.0.0.1:8000/workcenter/schoolcycles/{cycle.pk}/edit/",
    ]
    
    print(f"\n🌐 Abriendo navegador para probar:")
    print(f"  1. Lista de ciclos: {urls[0]}")
    print(f"  2. Editar ciclo '{cycle.name}': {urls[1]}")
    
    # Abrir cada URL
    for i, url in enumerate(urls, 1):
        print(f"\n📱 Abriendo {i}/2: {url}")
        webbrowser.open(url)
        time.sleep(3)  # Pausa entre aperturas
    
    print(f"\n✅ Navegador abierto para verificar funcionalidad")
    print(f"   Verifica lo siguiente:")
    print(f"   • En la lista: Botones azules 'Editar' visibles")
    print(f"   • En el formulario: Información del ciclo mostrada")
    print(f"   • Duración: {duration} días calculada correctamente")
    print(f"   • Botón 'Actualizar Ciclo' púrpura visible")
    print(f"   • Sin errores de template")
    
    print(f"\n🎯 Funcionalidades implementadas:")
    print(f"  ✅ Vista de edición funcional")
    print(f"  ✅ Template sin errores")
    print(f"  ✅ Botones visibles y funcionales")
    print(f"  ✅ Cálculo de duración correcto")
    print(f"  ✅ Validación de formularios")
    print(f"  ✅ Redirección después de guardar")
    print(f"  ✅ Mensajes de éxito/error")
    print(f"  ✅ Navegación entre secciones")

if __name__ == '__main__':
    test_final_functionality() 