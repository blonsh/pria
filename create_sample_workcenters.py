#!/usr/bin/env python3
"""
Script para crear centros de trabajo de ejemplo para el sistema PRIA
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from workcenter.models import WorkCenter

def create_sample_workcenters():
    """Crear centros de trabajo de ejemplo."""
    workcenters_data = [
        {
            'name': 'Escuela Primaria Benito Juárez',
            'address': 'Av. Reforma 123, Centro Histórico, Ciudad de México',
            'director_name': 'María González López',
            'school_control_name': 'Ana Martínez Rodríguez'
        },
        {
            'name': 'Escuela Secundaria Técnica No. 15',
            'address': 'Calle Morelos 456, Colonia Industrial, Guadalajara',
            'director_name': 'Carlos Ramírez Mendoza',
            'school_control_name': 'Patricia Sánchez Vega'
        },
        {
            'name': 'Preparatoria Oficial No. 8',
            'address': 'Blvd. Universidad 789, Zona Universitaria, Monterrey',
            'director_name': 'Roberto Silva Torres',
            'school_control_name': 'Carmen López Hernández'
        },
        {
            'name': 'Universidad Tecnológica del Norte',
            'address': 'Carretera Federal 85 Km 12, Zona Industrial, Saltillo',
            'director_name': 'Dr. Francisco Mendoza Ruiz',
            'school_control_name': 'Lic. Guadalupe Torres Jiménez'
        },
        {
            'name': 'Instituto Tecnológico de Estudios Superiores',
            'address': 'Av. Tecnológico 321, Parque Industrial, Querétaro',
            'director_name': 'Ing. Laura Fernández Castro',
            'school_control_name': 'C.P. Ricardo Morales Díaz'
        },
        {
            'name': 'Centro de Estudios Avanzados',
            'address': 'Paseo de la Reforma 654, Polanco, Ciudad de México',
            'director_name': 'Dra. Isabel Vargas Moreno',
            'school_control_name': 'Lic. Adriana Ruiz Mendoza'
        },
        {
            'name': 'Escuela de Artes y Oficios',
            'address': 'Calle Independencia 987, Centro, Puebla',
            'director_name': 'Prof. Manuel Ortiz García',
            'school_control_name': 'Sra. Elena Castro Morales'
        },
        {
            'name': 'Centro de Capacitación Profesional',
            'address': 'Av. Constitución 147, Zona Centro, León',
            'director_name': 'Lic. Fernando Herrera Luna',
            'school_control_name': 'C.P. Rosa María Delgado'
        }
    ]
    
    workcenters_creados = []
    
    for workcenter_data in workcenters_data:
        workcenter, created = WorkCenter.objects.get_or_create(
            name=workcenter_data['name'],
            defaults=workcenter_data
        )
        
        if created:
            workcenters_creados.append(workcenter)
            print(f"✅ Centro de trabajo creado: {workcenter.name}")
        else:
            print(f"ℹ️  Centro de trabajo ya existe: {workcenter.name}")
    
    return workcenters_creados

def main():
    """Función principal."""
    print("🏢 Creando centros de trabajo de ejemplo...")
    print("=" * 50)
    
    try:
        workcenters = create_sample_workcenters()
        
        print("=" * 50)
        print(f"✅ Proceso completado exitosamente!")
        print(f"📊 Total de centros de trabajo en el sistema: {WorkCenter.objects.count()}")
        print(f"🆕 Centros de trabajo creados en esta ejecución: {len(workcenters)}")
        
        print("\n📋 Centros de trabajo disponibles:")
        for workcenter in WorkCenter.objects.all():
            print(f"  • {workcenter.name} (ID: {workcenter.id})")
            print(f"    Director: {workcenter.director_name}")
            print(f"    Control Escolar: {workcenter.school_control_name}")
            print()
            
    except Exception as e:
        print(f"❌ Error al crear centros de trabajo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 