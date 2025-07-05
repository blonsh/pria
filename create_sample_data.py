#!/usr/bin/env python3
"""
Script para crear datos de ejemplo para el sistema PRIA.
"""

import os
import sys
import django
from datetime import date, timedelta

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from workcenter.models import WorkCenter, Classroom, SchoolCycle, SchoolPeriod

def create_sample_data():
    """Crea datos de ejemplo para el sistema."""
    
    print("=== Creando Datos de Ejemplo para PRIA ===\n")
    
    # Obtener centros de trabajo existentes
    workcenters = WorkCenter.objects.all()
    
    if not workcenters.exists():
        print("❌ No hay centros de trabajo. Ejecuta primero el script para crear centros.")
        return
    
    print(f"📚 Creando aulas para {workcenters.count()} centros de trabajo...")
    
    # Crear aulas para cada centro de trabajo
    for workcenter in workcenters:
        # Crear 3-5 aulas por centro
        num_classrooms = 3 + (workcenter.id % 3)  # 3-5 aulas
        
        for i in range(num_classrooms):
            classroom = Classroom.objects.create(
                work_center=workcenter,
                name=f"Aula {chr(65 + i)}",  # A, B, C, D, E
                capacity=30 + (i * 5)  # 30, 35, 40, 45, 50
            )
            print(f"  ✅ Aula {classroom.name} creada en {workcenter.name} (Capacidad: {classroom.capacity})")
    
    print(f"\n📅 Creando ciclos escolares...")
    
    # Crear ciclos escolares
    current_year = date.today().year
    cycles_data = [
        {
            'name': f'Ciclo Escolar {current_year}-{current_year + 1}',
            'start_date': date(current_year, 8, 15),
            'end_date': date(current_year + 1, 7, 15)
        },
        {
            'name': f'Ciclo Escolar {current_year - 1}-{current_year}',
            'start_date': date(current_year - 1, 8, 15),
            'end_date': date(current_year, 7, 15)
        },
        {
            'name': f'Ciclo Escolar {current_year + 1}-{current_year + 2}',
            'start_date': date(current_year + 1, 8, 15),
            'end_date': date(current_year + 2, 7, 15)
        }
    ]
    
    for workcenter in workcenters:
        for cycle_data in cycles_data:
            cycle = SchoolCycle.objects.create(
                work_center=workcenter,
                name=cycle_data['name'],
                start_date=cycle_data['start_date'],
                end_date=cycle_data['end_date']
            )
            print(f"  ✅ Ciclo {cycle.name} creado en {workcenter.name}")
    
    print(f"\n⏰ Creando periodos escolares...")
    
    # Crear periodos escolares para cada ciclo
    for cycle in SchoolCycle.objects.all():
        periods_data = [
            {
                'name': 'Primer Periodo',
                'period_type': 'BIMESTRE',
                'start_date': cycle.start_date,
                'end_date': cycle.start_date + timedelta(days=60)
            },
            {
                'name': 'Segundo Periodo',
                'period_type': 'BIMESTRE',
                'start_date': cycle.start_date + timedelta(days=61),
                'end_date': cycle.start_date + timedelta(days=120)
            },
            {
                'name': 'Tercer Periodo',
                'period_type': 'BIMESTRE',
                'start_date': cycle.start_date + timedelta(days=121),
                'end_date': cycle.start_date + timedelta(days=180)
            },
            {
                'name': 'Cuarto Periodo',
                'period_type': 'BIMESTRE',
                'start_date': cycle.start_date + timedelta(days=181),
                'end_date': cycle.end_date
            }
        ]
        
        for period_data in periods_data:
            period = SchoolPeriod.objects.create(
                school_cycle=cycle,
                name=period_data['name'],
                period_type=period_data['period_type'],
                start_date=period_data['start_date'],
                end_date=period_data['end_date']
            )
            print(f"  ✅ Periodo {period.name} creado para {cycle.name}")
    
    # Mostrar estadísticas finales
    print(f"\n📊 Estadísticas Finales:")
    print(f"  • Centros de trabajo: {WorkCenter.objects.count()}")
    print(f"  • Aulas: {Classroom.objects.count()}")
    print(f"  • Ciclos escolares: {SchoolCycle.objects.count()}")
    print(f"  • Periodos escolares: {SchoolPeriod.objects.count()}")
    
    print(f"\n✅ Datos de ejemplo creados exitosamente!")
    print(f"   Accede al dashboard: http://127.0.0.1:8000/workcenter/")

if __name__ == "__main__":
    create_sample_data() 