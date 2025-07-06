#!/usr/bin/env python3
"""
Script para crear niveles educativos de ejemplo para el sistema PRIA
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from core.models import EducationalLevel

def create_sample_levels():
    """Crear niveles educativos de ejemplo."""
    levels_data = [
        {
            'nombre': 'Maternal',
            'orden': 1,
            'activo': True,
            'es_nivel_superior': False
        },
        {
            'nombre': 'Preescolar',
            'orden': 2,
            'activo': True,
            'es_nivel_superior': False
        },
        {
            'nombre': 'Primaria',
            'orden': 3,
            'activo': True,
            'es_nivel_superior': False
        },
        {
            'nombre': 'Secundaria',
            'orden': 4,
            'activo': True,
            'es_nivel_superior': False
        },
        {
            'nombre': 'Preparatoria',
            'orden': 5,
            'activo': True,
            'es_nivel_superior': False
        },
        {
            'nombre': 'Universidad',
            'orden': 6,
            'activo': True,
            'es_nivel_superior': True
        },
        {
            'nombre': 'Posgrado',
            'orden': 7,
            'activo': True,
            'es_nivel_superior': True
        },
        {
            'nombre': 'Curso de Verano',
            'orden': 8,
            'activo': True,
            'es_nivel_superior': False
        },
        {
            'nombre': 'Diplomado',
            'orden': 9,
            'activo': True,
            'es_nivel_superior': False
        },
        {
            'nombre': 'Taller',
            'orden': 10,
            'activo': True,
            'es_nivel_superior': False
        }
    ]
    
    levels_creados = []
    
    for level_data in levels_data:
        level, created = EducationalLevel.objects.get_or_create(
            nombre=level_data['nombre'],
            defaults=level_data
        )
        
        if created:
            levels_creados.append(level)
            print(f"✅ Nivel creado: {level.nombre}")
        else:
            print(f"ℹ️  Nivel ya existe: {level.nombre}")
    
    return levels_creados

def main():
    """Función principal."""
    print("🎓 Creando niveles educativos de ejemplo...")
    print("=" * 50)
    
    try:
        levels = create_sample_levels()
        
        print("=" * 50)
        print(f"✅ Proceso completado exitosamente!")
        print(f"📊 Total de niveles en el sistema: {EducationalLevel.objects.count()}")
        print(f"🆕 Niveles creados en esta ejecución: {len(levels)}")
        
        print("\n📋 Niveles disponibles:")
        for level in EducationalLevel.objects.all():
            tipo = "Superior" if level.es_nivel_superior else "Básico"
            print(f"  • {level.nombre} ({tipo}) - Orden: {level.orden}")
            
    except Exception as e:
        print(f"❌ Error al crear niveles: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 