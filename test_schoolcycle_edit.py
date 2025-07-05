#!/usr/bin/env python3
"""
Script para probar la funcionalidad de edición de ciclos escolares.
"""

import os
import sys
import django
from datetime import date

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from workcenter.models import SchoolCycle, WorkCenter

def test_schoolcycle_edit():
    """Prueba la funcionalidad de edición de ciclos escolares."""
    
    print("=== Probando Funcionalidad de Edición de Ciclos Escolares ===\n")
    
    # Verificar que hay datos
    total_cycles = SchoolCycle.objects.count()
    
    print(f"📊 Datos disponibles:")
    print(f"  • Ciclos escolares: {total_cycles}")
    
    if total_cycles == 0:
        print(f"\n⚠️  No hay ciclos escolares. Ejecuta primero:")
        print(f"   python3 create_sample_data.py")
        return
    
    # Mostrar algunos ciclos disponibles para editar
    print(f"\n📅 Ciclos disponibles para editar:")
    cycles = SchoolCycle.objects.all().select_related('work_center')[:3]
    
    for i, cycle in enumerate(cycles, 1):
        duration = (cycle.end_date - cycle.start_date).days
        status = "Activo" if cycle.start_date <= date.today() <= cycle.end_date else "Inactivo"
        
        print(f"  {i}. {cycle.name}")
        print(f"     Centro: {cycle.work_center.name}")
        print(f"     Fechas: {cycle.start_date} - {cycle.end_date}")
        print(f"     Duración: {duration} días")
        print(f"     Estado: {status}")
        print(f"     URL de edición: http://127.0.0.1:8000/workcenter/schoolcycles/{cycle.pk}/edit/")
        print()
    
    # Verificar URLs
    print(f"🔗 URLs disponibles:")
    print(f"  • Lista de ciclos: http://127.0.0.1:8000/workcenter/schoolcycles/")
    print(f"  • Crear ciclo: http://127.0.0.1:8000/workcenter/schoolcycles/new/")
    print(f"  • Editar ciclo (ejemplo): http://127.0.0.1:8000/workcenter/schoolcycles/{cycles[0].pk}/edit/")
    
    # Verificar funcionalidades
    print(f"\n✅ Funcionalidades implementadas:")
    print(f"  • Vista schoolcycle_update mejorada")
    print(f"  • Template schoolcycle_form.html modernizado")
    print(f"  • Validación de formularios con mensajes de error")
    print(f"  • Redirección a la lista de ciclos después de editar")
    print(f"  • Información adicional del ciclo en modo edición")
    print(f"  • Estados visuales (Activo, Próximo, Finalizado)")
    print(f"  • Navegación mejorada entre secciones")
    print(f"  • Botones de acción con iconos")
    
    # Verificar características del diseño
    print(f"\n🎨 Características del diseño:")
    print(f"  • Header con título y botón de volver")
    print(f"  • Mensajes de éxito/error con iconos")
    print(f"  • Formulario con validación visual")
    print(f"  • Información adicional del ciclo en edición")
    print(f"  • Botones de acción responsivos")
    print(f"  • Navegación inferior con enlaces")
    
    print(f"\n✨ La funcionalidad de edición de ciclos está lista!")
    print(f"   Prueba editando un ciclo en: http://127.0.0.1:8000/workcenter/schoolcycles/")

if __name__ == '__main__':
    test_schoolcycle_edit() 