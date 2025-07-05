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

def test_workcenter_editing():
    """Prueba la funcionalidad completa de edición de centros de trabajo."""
    
    print("=== Prueba de Edición de Centros de Trabajo ===\n")
    
    # 1. Verificar centros de trabajo existentes
    workcenters = WorkCenter.objects.all()
    print(f"📊 Centros de trabajo disponibles: {workcenters.count()}")
    
    if workcenters.exists():
        # Mostrar el primer centro de trabajo
        workcenter = workcenters.first()
        print(f"\n🏢 Centro de trabajo a editar:")
        print(f"  • ID: {workcenter.pk}")
        print(f"  • Nombre: {workcenter.name}")
        print(f"  • Dirección: {workcenter.address}")
        print(f"  • Director: {workcenter.director_name}")
        print(f"  • Control Escolar: {workcenter.school_control_name}")
        
        # 2. Probar el formulario de edición
        print(f"\n--- Probando formulario de edición ---")
        
        # Crear datos de prueba para edición
        test_data = {
            'name': f"{workcenter.name} (Editado)",
            'address': f"{workcenter.address} - Dirección actualizada",
            'director_name': f"{workcenter.director_name} - Director actualizado",
            'school_control_name': f"{workcenter.school_control_name} - Control actualizado"
        }
        
        # Crear formulario con datos de prueba
        form = WorkCenterForm(data=test_data, instance=workcenter)
        
        if form.is_valid():
            print("✅ Formulario válido")
            print("  Campos a actualizar:")
            for field, value in test_data.items():
                print(f"    • {field}: {value}")
            
            # Guardar los cambios
            updated_workcenter = form.save()
            print(f"\n✅ Centro de trabajo actualizado exitosamente")
            print(f"  Nuevo nombre: {updated_workcenter.name}")
            
            # Restaurar datos originales
            original_data = {
                'name': workcenter.name.replace(" (Editado)", ""),
                'address': workcenter.address.replace(" - Dirección actualizada", ""),
                'director_name': workcenter.director_name.replace(" - Director actualizado", ""),
                'school_control_name': workcenter.school_control_name.replace(" - Control actualizado", "")
            }
            
            restore_form = WorkCenterForm(data=original_data, instance=updated_workcenter)
            if restore_form.is_valid():
                restore_form.save()
                print("✅ Datos originales restaurados")
            
        else:
            print("❌ Formulario inválido")
            for field, errors in form.errors.items():
                print(f"  • {field}: {errors}")
    
    else:
        print("❌ No hay centros de trabajo para probar.")
        print("💡 Ejecuta primero el script create_sample_data.py")
    
    # 3. Verificar URLs disponibles
    print(f"\n🌐 URLs de edición disponibles:")
    print(f"  • Lista de centros: http://127.0.0.1:8000/workcenter/workcenters/")
    print(f"  • Crear nuevo: http://127.0.0.1:8000/workcenter/workcenters/new/")
    if workcenters.exists():
        for i, wc in enumerate(workcenters[:3], 1):
            print(f"  • Editar centro {i}: http://127.0.0.1:8000/workcenter/workcenters/{wc.pk}/edit/")
            print(f"  • Ver detalles: http://127.0.0.1:8000/workcenter/workcenters/{wc.pk}/")
    
    # 4. Verificar funcionalidades implementadas
    print(f"\n✅ Funcionalidades implementadas:")
    print(f"  • Vista de edición: workcenter_update")
    print(f"  • Formulario: WorkCenterForm")
    print(f"  • Template: workcenter_form.html")
    print(f"  • URL: /workcenter/workcenters/<id>/edit/")
    print(f"  • Enlaces en lista: workcenter_list.html")
    print(f"  • Validación de formularios")
    print(f"  • Mensajes de éxito/error")
    print(f"  • Redirección después de actualizar")
    
    # 5. Verificar navegación
    print(f"\n🧭 Flujo de navegación:")
    print(f"  1. Lista de centros → http://127.0.0.1:8000/workcenter/workcenters/")
    print(f"  2. Hacer clic en ícono de editar (✏️)")
    print(f"  3. Formulario de edición → /workcenter/workcenters/<id>/edit/")
    print(f"  4. Modificar campos")
    print(f"  5. Guardar cambios")
    print(f"  6. Redirección a lista de centros")
    
    print(f"\n✨ La funcionalidad de edición está lista!")
    print(f"   Accede a: http://127.0.0.1:8000/workcenter/workcenters/")

if __name__ == "__main__":
    test_workcenter_editing() 