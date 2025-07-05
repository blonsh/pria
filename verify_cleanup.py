#!/usr/bin/env python3
"""
Script para verificar los resultados de la limpieza de ciclos escolares.
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

from workcenter.models import SchoolCycle, WorkCenter

def verify_cleanup():
    """Verifica los resultados de la limpieza de ciclos escolares."""
    
    print("=== Verificación de Limpieza de Ciclos Escolares ===\n")
    
    # Verificar estado final
    total_cycles = SchoolCycle.objects.count()
    total_workcenters = WorkCenter.objects.count()
    
    print(f"📊 Estado final:")
    print(f"  • Total de ciclos: {total_cycles}")
    print(f"  • Total de centros: {total_workcenters}")
    print(f"  • Ciclos por centro: {total_cycles // total_workcenters if total_workcenters > 0 else 0}")
    
    # Verificar que solo tenemos los ciclos correctos
    cycles = SchoolCycle.objects.all().select_related('work_center').order_by('work_center__name', 'start_date')
    
    print(f"\n📅 Ciclos finales:")
    for i, cycle in enumerate(cycles, 1):
        duration = (cycle.end_date - cycle.start_date).days
        status = "Activo" if cycle.start_date <= date.today() <= cycle.end_date else "Inactivo"
        
        print(f"  {i}. {cycle.name}")
        print(f"     Centro: {cycle.work_center.name}")
        print(f"     Fechas: {cycle.start_date} - {cycle.end_date}")
        print(f"     Duración: {duration} días")
        print(f"     Estado: {status}")
        print()
    
    # Verificar que no hay duplicados
    cycle_names = [cycle.name for cycle in cycles]
    unique_names = set(cycle_names)
    
    print(f"🔍 Verificación de duplicados:")
    print(f"  • Nombres únicos: {len(unique_names)}")
    print(f"  • Nombres totales: {len(cycle_names)}")
    print(f"  • ¿Sin duplicados?: {'✅ Sí' if len(unique_names) == len(cycle_names) else '❌ No'}")
    
    # Verificar que solo tenemos 2024-2025 y 2025-2026
    expected_names = {'Ciclo Escolar 2024-2025', 'Ciclo Escolar 2025-2026'}
    actual_names = set(unique_names)
    
    print(f"\n✅ Verificación de ciclos objetivo:")
    print(f"  • Ciclos esperados: {expected_names}")
    print(f"  • Ciclos actuales: {actual_names}")
    print(f"  • ¿Coinciden?: {'✅ Sí' if expected_names == actual_names else '❌ No'}")
    
    # URLs para verificar
    urls = [
        "http://127.0.0.1:8000/workcenter/schoolcycles/",
        "http://127.0.0.1:8000/workcenter/",
    ]
    
    print(f"\n🌐 Abriendo navegador para verificar:")
    print(f"  1. Lista de ciclos: {urls[0]}")
    print(f"  2. Dashboard: {urls[1]}")
    
    # Abrir navegador
    for i, url in enumerate(urls, 1):
        print(f"\n📱 Abriendo {i}/2: {url}")
        webbrowser.open(url)
        time.sleep(2)
    
    print(f"\n✅ Verificación completada!")
    print(f"   Verifica en el navegador:")
    print(f"   • Solo 10 ciclos en total")
    print(f"   • 2 ciclos por centro de trabajo")
    print(f"   • Solo 2024-2025 y 2025-2026")
    print(f"   • Sin duplicados")
    print(f"   • Estados correctos (Activo/Inactivo)")

if __name__ == '__main__':
    verify_cleanup() 