#!/usr/bin/env python3
"""
Script para crear carreras de ejemplo para el sistema de registro de alumnos
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from core.models import Carrera

def create_sample_carreras():
    """Crear carreras de ejemplo."""
    carreras_data = [
        {
            'nombre': 'Ingeniería en Sistemas Computacionales',
            'descripcion': 'Forma profesionales capaces de diseñar, desarrollar e implementar soluciones tecnológicas innovadoras.',
            'duracion_anios': 4,
            'activa': True
        },
        {
            'nombre': 'Ingeniería Industrial',
            'descripcion': 'Forma ingenieros especializados en optimización de procesos y gestión de la producción.',
            'duracion_anios': 4,
            'activa': True
        },
        {
            'nombre': 'Administración de Empresas',
            'descripcion': 'Forma administradores capaces de gestionar organizaciones de manera eficiente.',
            'duracion_anios': 4,
            'activa': True
        },
        {
            'nombre': 'Contaduría Pública',
            'descripcion': 'Forma contadores especializados en finanzas, auditoría y gestión fiscal.',
            'duracion_anios': 4,
            'activa': True
        },
        {
            'nombre': 'Derecho',
            'descripcion': 'Forma abogados con sólidos conocimientos en el sistema jurídico mexicano.',
            'duracion_anios': 4,
            'activa': True
        },
        {
            'nombre': 'Psicología',
            'descripcion': 'Forma psicólogos capaces de comprender y mejorar el comportamiento humano.',
            'duracion_anios': 4,
            'activa': True
        },
        {
            'nombre': 'Medicina',
            'descripcion': 'Forma médicos generales con conocimientos científicos y habilidades clínicas.',
            'duracion_anios': 6,
            'activa': True
        },
        {
            'nombre': 'Enfermería',
            'descripcion': 'Forma enfermeros especializados en el cuidado integral de la salud.',
            'duracion_anios': 4,
            'activa': True
        },
        {
            'nombre': 'Arquitectura',
            'descripcion': 'Forma arquitectos creativos con habilidades de diseño y construcción.',
            'duracion_anios': 5,
            'activa': True
        },
        {
            'nombre': 'Comunicación y Periodismo',
            'descripcion': 'Forma comunicadores especializados en medios y relaciones públicas.',
            'duracion_anios': 4,
            'activa': True
        }
    ]
    
    carreras_creadas = []
    
    for carrera_data in carreras_data:
        carrera, created = Carrera.objects.get_or_create(
            nombre=carrera_data['nombre'],
            defaults=carrera_data
        )
        
        if created:
            carreras_creadas.append(carrera)
            print(f"✅ Carrera creada: {carrera.nombre}")
        else:
            print(f"ℹ️  Carrera ya existe: {carrera.nombre}")
    
    return carreras_creadas

def main():
    """Función principal."""
    print("🎓 Creando carreras de ejemplo...")
    print("=" * 50)
    
    try:
        carreras = create_sample_carreras()
        
        print("=" * 50)
        print(f"✅ Proceso completado exitosamente!")
        print(f"📊 Total de carreras en el sistema: {Carrera.objects.count()}")
        print(f"🆕 Carreras creadas en esta ejecución: {len(carreras)}")
        
        print("\n📋 Carreras disponibles:")
        for carrera in Carrera.objects.all():
            print(f"  • {carrera.nombre} ({carrera.duracion_anios} años)")
            
    except Exception as e:
        print(f"❌ Error al crear carreras: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 