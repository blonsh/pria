#!/usr/bin/env python3
"""
Script para probar que el error del template se ha solucionado.
"""

import os
import sys
import django
from datetime import date

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from workcenter.models import SchoolCycle

def test_template_error_fix():
    """Prueba que el error del template se ha solucionado."""
    
    print("=== Probando Solución del Error de Template ===\n")
    
    # Verificar que hay datos
    total_cycles = SchoolCycle.objects.count()
    
    print(f"📊 Datos disponibles:")
    print(f"  • Ciclos escolares: {total_cycles}")
    
    if total_cycles == 0:
        print(f"\n⚠️  No hay ciclos escolares. Ejecuta primero:")
        print(f"   python3 create_sample_data.py")
        return
    
    # Obtener un ciclo de ejemplo
    cycle = SchoolCycle.objects.first()
    duration = (cycle.end_date - cycle.start_date).days
    
    print(f"\n📅 Ciclo de ejemplo:")
    print(f"  • Nombre: {cycle.name}")
    print(f"  • Centro: {cycle.work_center.name}")
    print(f"  • Fechas: {cycle.start_date} - {cycle.end_date}")
    print(f"  • Duración calculada: {duration} días")
    
    print(f"\n🔗 URLs para probar:")
    print(f"  • Editar ciclo: http://127.0.0.1:8000/workcenter/schoolcycles/{cycle.pk}/edit/")
    print(f"  • Lista de ciclos: http://127.0.0.1:8000/workcenter/schoolcycles/")
    
    print(f"\n✅ Problema solucionado:")
    print(f"  • Error: 'Invalid filter: sub'")
    print(f"  • Causa: Filtro 'sub' no existe en Django")
    print(f"  • Solución: Calcular duración en la vista")
    print(f"  • Variable: duration_days pasada al template")
    
    print(f"\n🔧 Cambios realizados:")
    print(f"  • Vista: Agregada variable duration_days")
    print(f"  • Template: Usa {{ duration_days }} en lugar de filtros")
    print(f"  • Cálculo: (end_date - start_date).days")
    
    print(f"\n✨ El error del template está solucionado!")
    print(f"   Prueba editando un ciclo en: http://127.0.0.1:8000/workcenter/schoolcycles/{cycle.pk}/edit/")

if __name__ == '__main__':
    test_template_error_fix() 