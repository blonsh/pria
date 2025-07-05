#!/usr/bin/env python3
"""
Script para limpiar ciclos escolares duplicados y mantener solo 2024-2025 y 2025-2026.
"""

import os
import sys
import django
from datetime import date

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from workcenter.models import SchoolCycle, WorkCenter

def cleanup_schoolcycles():
    """Limpia los ciclos escolares duplicados."""
    
    print("=== Limpieza de Ciclos Escolares ===\n")
    
    # Verificar ciclos actuales
    total_cycles = SchoolCycle.objects.count()
    print(f"📊 Estado actual:")
    print(f"  • Total de ciclos: {total_cycles}")
    
    if total_cycles == 0:
        print("❌ No hay ciclos escolares para limpiar.")
        return
    
    # Mostrar todos los ciclos actuales
    print(f"\n📅 Ciclos actuales:")
    cycles = SchoolCycle.objects.all().select_related('work_center').order_by('work_center__name', 'start_date')
    
    for i, cycle in enumerate(cycles, 1):
        duration = (cycle.end_date - cycle.start_date).days
        print(f"  {i}. {cycle.name}")
        print(f"     Centro: {cycle.work_center.name}")
        print(f"     Fechas: {cycle.start_date} - {cycle.end_date}")
        print(f"     Duración: {duration} días")
        print(f"     ID: {cycle.pk}")
        print()
    
    # Definir los ciclos que queremos mantener
    target_cycles = [
        {
            'name': 'Ciclo Escolar 2024-2025',
            'start_date': date(2024, 8, 15),
            'end_date': date(2025, 7, 15)
        },
        {
            'name': 'Ciclo Escolar 2025-2026',
            'start_date': date(2025, 8, 15),
            'end_date': date(2026, 7, 15)
        }
    ]
    
    print(f"🎯 Ciclos objetivo:")
    for i, cycle_data in enumerate(target_cycles, 1):
        duration = (cycle_data['end_date'] - cycle_data['start_date']).days
        print(f"  {i}. {cycle_data['name']}")
        print(f"     Fechas: {cycle_data['start_date']} - {cycle_data['end_date']}")
        print(f"     Duración: {duration} días")
        print()
    
    # Obtener todos los centros de trabajo
    workcenters = WorkCenter.objects.all()
    
    if not workcenters.exists():
        print("❌ No hay centros de trabajo. No se pueden crear ciclos.")
        return
    
    print(f"🏫 Centros de trabajo disponibles:")
    for workcenter in workcenters:
        print(f"  • {workcenter.name}")
    
    # Eliminar todos los ciclos existentes
    print(f"\n🗑️  Eliminando ciclos existentes...")
    deleted_count = SchoolCycle.objects.count()
    SchoolCycle.objects.all().delete()
    print(f"  ✅ {deleted_count} ciclos eliminados")
    
    # Crear los ciclos objetivo para cada centro de trabajo
    print(f"\n✨ Creando ciclos objetivo...")
    created_count = 0
    
    for workcenter in workcenters:
        for cycle_data in target_cycles:
            cycle = SchoolCycle.objects.create(
                work_center=workcenter,
                name=cycle_data['name'],
                start_date=cycle_data['start_date'],
                end_date=cycle_data['end_date']
            )
            duration = (cycle.end_date - cycle.start_date).days
            print(f"  ✅ {cycle.name} creado en {workcenter.name} ({duration} días)")
            created_count += 1
    
    # Verificar resultado final
    final_count = SchoolCycle.objects.count()
    print(f"\n📊 Resultado final:")
    print(f"  • Ciclos eliminados: {deleted_count}")
    print(f"  • Ciclos creados: {created_count}")
    print(f"  • Total final: {final_count}")
    
    # Mostrar ciclos finales
    print(f"\n📅 Ciclos finales:")
    final_cycles = SchoolCycle.objects.all().select_related('work_center').order_by('work_center__name', 'start_date')
    
    for i, cycle in enumerate(final_cycles, 1):
        duration = (cycle.end_date - cycle.start_date).days
        status = "Activo" if cycle.start_date <= date.today() <= cycle.end_date else "Inactivo"
        print(f"  {i}. {cycle.name}")
        print(f"     Centro: {cycle.work_center.name}")
        print(f"     Fechas: {cycle.start_date} - {cycle.end_date}")
        print(f"     Duración: {duration} días")
        print(f"     Estado: {status}")
        print()
    
    print(f"✅ Limpieza completada exitosamente!")
    print(f"   Accede a: http://127.0.0.1:8000/workcenter/schoolcycles/")

if __name__ == '__main__':
    cleanup_schoolcycles() 