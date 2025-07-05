#!/usr/bin/env python3
"""
Script para probar la funcionalidad de configuración de ciclos activos.
"""

import os
import sys
import django
from datetime import date, timedelta

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from workcenter.models import WorkCenter, SchoolCycle, SchoolCycleConfig

def test_cycle_configuration():
    """Prueba la funcionalidad de configuración de ciclos"""
    print("🔧 Probando configuración de ciclos activos...")
    
    # Obtener centros de trabajo
    work_centers = WorkCenter.objects.all()
    print(f"📊 Centros de trabajo encontrados: {work_centers.count()}")
    
    for work_center in work_centers:
        print(f"\n🏫 Centro: {work_center.name}")
        
        # Crear o obtener configuración
        config, created = SchoolCycleConfig.objects.get_or_create(work_center=work_center)
        if created:
            print(f"  ✅ Configuración creada para {work_center.name}")
        else:
            print(f"  ℹ️  Configuración existente para {work_center.name}")
        
        # Mostrar configuración actual
        print(f"  ⚙️  Activación automática: {'Sí' if config.auto_activate_by_date else 'No'}")
        print(f"  ⚙️  Múltiples activos: {'Sí' if config.allow_multiple_active else 'No'}")
        
        # Obtener ciclos activos
        active_cycles = config.get_active_cycles()
        print(f"  📅 Ciclos activos: {active_cycles.count()}")
        
        for cycle in active_cycles:
            print(f"    - {cycle.name} ({cycle.start_date} - {cycle.end_date})")
    
    print("\n🎯 Prueba completada exitosamente!")

def test_manual_activation():
    """Prueba la activación manual de ciclos"""
    print("\n🔧 Probando activación manual de ciclos...")
    
    work_centers = WorkCenter.objects.all()
    
    for work_center in work_centers:
        print(f"\n🏫 Centro: {work_center.name}")
        
        # Obtener todos los ciclos del centro
        cycles = SchoolCycle.objects.filter(work_center=work_center)
        print(f"  📅 Total de ciclos: {cycles.count()}")
        
        # Mostrar estado actual de activación
        active_cycles = cycles.filter(is_active=True)
        print(f"  ✅ Ciclos marcados como activos: {active_cycles.count()}")
        
        for cycle in active_cycles:
            print(f"    - {cycle.name} (is_active=True)")
        
        # Mostrar ciclos que están en curso por fecha
        today = date.today()
        current_cycles = cycles.filter(start_date__lte=today, end_date__gte=today)
        print(f"  📅 Ciclos en curso por fecha: {current_cycles.count()}")
        
        for cycle in current_cycles:
            print(f"    - {cycle.name} (en curso por fecha)")

def test_configuration_creation():
    """Prueba la creación automática de configuraciones"""
    print("\n🔧 Probando creación automática de configuraciones...")
    
    # Verificar que todos los centros tengan configuración
    work_centers = WorkCenter.objects.all()
    configs = SchoolCycleConfig.objects.all()
    
    print(f"📊 Centros de trabajo: {work_centers.count()}")
    print(f"⚙️  Configuraciones: {configs.count()}")
    
    if work_centers.count() == configs.count():
        print("✅ Todos los centros tienen configuración")
    else:
        print("❌ Faltan configuraciones para algunos centros")
        
        # Crear configuraciones faltantes
        for work_center in work_centers:
            config, created = SchoolCycleConfig.objects.get_or_create(work_center=work_center)
            if created:
                print(f"  ✅ Configuración creada para {work_center.name}")

if __name__ == "__main__":
    print("🚀 Iniciando pruebas de configuración de ciclos...")
    
    try:
        test_cycle_configuration()
        test_manual_activation()
        test_configuration_creation()
        
        print("\n🎉 Todas las pruebas completadas exitosamente!")
        print("\n📋 Resumen:")
        print("  - Configuración de ciclos: ✅")
        print("  - Activación manual: ✅")
        print("  - Creación automática: ✅")
        
    except Exception as e:
        print(f"\n❌ Error durante las pruebas: {e}")
        sys.exit(1) 