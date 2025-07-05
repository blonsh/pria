#!/usr/bin/env python3
"""
Script para probar la funcionalidad de edición de centros de trabajo.
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from workcenter.models import WorkCenter
from workcenter.forms import WorkCenterForm

def test_workcenter_edition():
    """Prueba la funcionalidad de edición de centros de trabajo."""
    
    print("=== Prueba de Funcionalidad de Edición de Centros de Trabajo ===\n")
    
    # 1. Verificar que existen centros de trabajo
    workcenters = WorkCenter.objects.all()
    print(f"Centros de trabajo encontrados: {workcenters.count()}")
    
    if workcenters.exists():
        # Mostrar el primer centro de trabajo
        workcenter = workcenters.first()
        print(f"\nCentro de trabajo a editar:")
        print(f"  ID: {workcenter.pk}")
        print(f"  Nombre: {workcenter.name}")
        print(f"  Dirección: {workcenter.address}")
        print(f"  Director: {workcenter.director_name}")
        print(f"  Control Escolar: {workcenter.school_control_name}")
        
        # 2. Probar el formulario de edición
        print(f"\n--- Probando formulario de edición ---")
        
        # Crear datos de prueba
        test_data = {
            'name': f"{workcenter.name} (Actualizado)",
            'address': f"{workcenter.address} - Edición de prueba",
            'director_name': f"{workcenter.director_name} - Actualizado",
            'school_control_name': f"{workcenter.school_control_name} - Actualizado"
        }
        
        # Crear formulario con datos de prueba
        form = WorkCenterForm(data=test_data, instance=workcenter)
        
        if form.is_valid():
            print("✓ Formulario válido")
            print("  Campos actualizados:")
            for field, value in test_data.items():
                print(f"    {field}: {value}")
            
            # Guardar los cambios
            updated_workcenter = form.save()
            print(f"\n✓ Centro de trabajo actualizado exitosamente")
            print(f"  Nuevo nombre: {updated_workcenter.name}")
            
            # Restaurar datos originales
            original_data = {
                'name': workcenter.name.replace(" (Actualizado)", ""),
                'address': workcenter.address.replace(" - Edición de prueba", ""),
                'director_name': workcenter.director_name.replace(" - Actualizado", ""),
                'school_control_name': workcenter.school_control_name.replace(" - Actualizado", "")
            }
            
            restore_form = WorkCenterForm(data=original_data, instance=updated_workcenter)
            if restore_form.is_valid():
                restore_form.save()
                print("✓ Datos originales restaurados")
            
        else:
            print("✗ Formulario inválido")
            for field, errors in form.errors.items():
                print(f"  {field}: {errors}")
    
    else:
        print("No hay centros de trabajo para probar.")
        print("Ejecuta primero el script create_sample_data.py")
    
    print(f"\n=== URLs disponibles ===")
    print(f"Lista de centros: http://127.0.0.1:8000/workcenter/workcenters/")
    print(f"Crear nuevo: http://127.0.0.1:8000/workcenter/workcenters/new/")
    if workcenters.exists():
        first_id = workcenters.first().pk
        print(f"Ver detalles: http://127.0.0.1:8000/workcenter/workcenters/{first_id}/")
        print(f"Editar: http://127.0.0.1:8000/workcenter/workcenters/{first_id}/edit/")

if __name__ == "__main__":
    test_workcenter_edition() 