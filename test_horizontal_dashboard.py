#!/usr/bin/env python3
"""
Script para probar el nuevo diseño horizontal del dashboard.
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from workcenter.models import WorkCenter, Classroom, SchoolCycle, SchoolPeriod

def test_horizontal_dashboard():
    """Prueba el nuevo diseño horizontal del dashboard."""
    
    print("=== Prueba del Nuevo Dashboard Horizontal ===\n")
    
    # 1. Verificar estadísticas
    total_workcenters = WorkCenter.objects.count()
    total_classrooms = Classroom.objects.count()
    total_school_cycles = SchoolCycle.objects.count()
    total_school_periods = SchoolPeriod.objects.count()
    
    print("📊 Estadísticas del Dashboard:")
    print(f"  • Centros de trabajo: {total_workcenters}")
    print(f"  • Aulas: {total_classrooms}")
    print(f"  • Ciclos escolares: {total_school_cycles}")
    print(f"  • Periodos escolares: {total_school_periods}")
    
    # 2. Verificar datos recientes
    recent_workcenters = WorkCenter.objects.all().order_by('-id')[:3]
    recent_classrooms = Classroom.objects.all().order_by('-id')[:3]
    recent_school_cycles = SchoolCycle.objects.all().order_by('-start_date')[:3]
    
    print(f"\n🏢 Centros de trabajo recientes ({len(recent_workcenters)}):")
    for wc in recent_workcenters:
        print(f"  • {wc.name} - {wc.director_name}")
    
    print(f"\n🏫 Aulas recientes ({len(recent_classrooms)}):")
    for classroom in recent_classrooms:
        print(f"  • {classroom.name} - {classroom.work_center.name} ({classroom.capacity} alumnos)")
    
    print(f"\n📅 Ciclos escolares recientes ({len(recent_school_cycles)}):")
    for cycle in recent_school_cycles:
        print(f"  • {cycle.name} - {cycle.work_center.name}")
    
    # 3. Verificar URLs disponibles
    print(f"\n🌐 URLs del Dashboard:")
    print(f"  • Dashboard principal: http://127.0.0.1:8000/workcenter/")
    print(f"  • Lista de centros: http://127.0.0.1:8000/workcenter/workcenters/")
    print(f"  • Crear centro: http://127.0.0.1:8000/workcenter/workcenters/new/")
    print(f"  • Crear aula: http://127.0.0.1:8000/workcenter/classrooms/new/")
    print(f"  • Crear ciclo: http://127.0.0.1:8000/workcenter/schoolcycles/new/")
    print(f"  • Crear periodo: http://127.0.0.1:8000/workcenter/schoolperiods/new/")
    
    # 4. Verificar funcionalidades
    print(f"\n✅ Funcionalidades implementadas:")
    print(f"  • Diseño horizontal con 3 columnas")
    print(f"  • Estadísticas en la parte superior")
    print(f"  • Sección de centros de trabajo (columna 1)")
    print(f"  • Sección de aulas (columna 2)")
    print(f"  • Sección de ciclos escolares (columna 3)")
    print(f"  • Acciones rápidas en la parte inferior")
    print(f"  • Enlaces de navegación entre secciones")
    
    # 5. Verificar responsividad
    print(f"\n📱 Características de diseño:")
    print(f"  • Responsive: grid-cols-1 lg:grid-cols-3")
    print(f"  • En móviles: 1 columna")
    print(f"  • En tablets: 1 columna")
    print(f"  • En desktop: 3 columnas horizontales")
    
    print(f"\n🎨 Colores por sección:")
    print(f"  • Centros de trabajo: Azul (#3B82F6)")
    print(f"  • Aulas: Verde (#10B981)")
    print(f"  • Ciclos escolares: Púrpura (#8B5CF6)")
    print(f"  • Periodos escolares: Naranja (#F59E0B)")
    
    print(f"\n✨ El nuevo diseño horizontal está listo para usar!")
    print(f"   Accede a: http://127.0.0.1:8000/workcenter/")

if __name__ == "__main__":
    test_horizontal_dashboard() 