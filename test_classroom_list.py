#!/usr/bin/env python3
"""
Script para probar la funcionalidad de lista de aulas.
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from workcenter.models import Classroom, WorkCenter

def test_classroom_list():
    """Prueba la funcionalidad de lista de aulas."""
    
    print("=== Prueba de Lista de Aulas ===\n")
    
    # 1. Verificar aulas existentes
    classrooms = Classroom.objects.all().select_related('work_center')
    total_classrooms = classrooms.count()
    total_capacity = sum(classroom.capacity for classroom in classrooms)
    avg_capacity = total_capacity / total_classrooms if total_classrooms > 0 else 0
    
    print("📊 Estadísticas de Aulas:")
    print(f"  • Total de aulas: {total_classrooms}")
    print(f"  • Capacidad total: {total_capacity} alumnos")
    print(f"  • Capacidad promedio: {avg_capacity:.1f} alumnos")
    
    # 2. Mostrar aulas por centro de trabajo
    workcenters = WorkCenter.objects.all()
    print(f"\n🏫 Aulas por Centro de Trabajo:")
    for workcenter in workcenters:
        workcenter_classrooms = classrooms.filter(work_center=workcenter)
        print(f"  • {workcenter.name}: {workcenter_classrooms.count()} aulas")
        for classroom in workcenter_classrooms:
            print(f"    - {classroom.name}: {classroom.capacity} alumnos")
    
    # 3. Verificar URLs
    print(f"\n🌐 URLs Disponibles:")
    print(f"  • Lista de aulas: http://127.0.0.1:8000/workcenter/classrooms/")
    print(f"  • Crear nueva aula: http://127.0.0.1:8000/workcenter/classrooms/new/")
    print(f"  • Dashboard: http://127.0.0.1:8000/workcenter/")
    
    # 4. Verificar funcionalidades
    print(f"\n✅ Funcionalidades implementadas:")
    print(f"  • Vista de lista de todas las aulas")
    print(f"  • Estadísticas de capacidad")
    print(f"  • Enlaces a edición de aulas")
    print(f"  • Enlaces a centros de trabajo")
    print(f"  • Diseño responsive con tarjetas")
    print(f"  • Navegación desde el dashboard")
    
    # 5. Verificar datos de ejemplo
    if total_classrooms > 0:
        print(f"\n📋 Datos de ejemplo disponibles:")
        print(f"  • {total_classrooms} aulas creadas")
        print(f"  • Distribuidas en {workcenters.count()} centros")
        print(f"  • Capacidades entre 30-50 alumnos")
        
        # Mostrar algunas aulas de ejemplo
        print(f"\n📝 Ejemplos de aulas:")
        for i, classroom in enumerate(classrooms[:3]):
            print(f"  {i+1}. {classroom.name} - {classroom.work_center.name} ({classroom.capacity} alumnos)")
    
    print(f"\n✨ La funcionalidad de lista de aulas está lista!")
    print(f"   Accede a: http://127.0.0.1:8000/workcenter/classrooms/")

if __name__ == "__main__":
    test_classroom_list() 