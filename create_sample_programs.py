#!/usr/bin/env python3
"""
Script para crear programas académicos de ejemplo para diferentes niveles educativos
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from core.models import EducationalLevel, AcademicProgram

def create_sample_programs():
    """Crear programas académicos de ejemplo para diferentes niveles."""
    
    # Obtener niveles educativos
    niveles = {
        'maternal': EducationalLevel.objects.get(nombre='Maternal'),
        'preescolar': EducationalLevel.objects.get(nombre='Preescolar'),
        'primaria': EducationalLevel.objects.get(nombre='Primaria'),
        'secundaria': EducationalLevel.objects.get(nombre='Secundaria'),
        'preparatoria': EducationalLevel.objects.get(nombre='Preparatoria'),
        'universidad': EducationalLevel.objects.get(nombre='Universidad'),
        'posgrado': EducationalLevel.objects.get(nombre='Posgrado'),
        'curso_verano': EducationalLevel.objects.get(nombre='Curso de Verano'),
        'diplomado': EducationalLevel.objects.get(nombre='Diplomado'),
        'taller': EducationalLevel.objects.get(nombre='Taller'),
    }
    
    programas_data = [
        # Maternal
        {
            'nombre': 'Maternal Turno Matutino',
            'nivel_educativo': niveles['maternal'],
            'descripcion': 'Programa de maternal en horario matutino para niños de 1-3 años.',
            'duracion': '2 años',
            'es_temporal': False
        },
        {
            'nombre': 'Maternal Turno Vespertino',
            'nivel_educativo': niveles['maternal'],
            'descripcion': 'Programa de maternal en horario vespertino para niños de 1-3 años.',
            'duracion': '2 años',
            'es_temporal': False
        },
        
        # Preescolar
        {
            'nombre': 'Preescolar Turno Matutino',
            'nivel_educativo': niveles['preescolar'],
            'descripcion': 'Programa de preescolar en horario matutino para niños de 3-6 años.',
            'duracion': '3 años',
            'es_temporal': False
        },
        {
            'nombre': 'Preescolar Turno Vespertino',
            'nivel_educativo': niveles['preescolar'],
            'descripcion': 'Programa de preescolar en horario vespertino para niños de 3-6 años.',
            'duracion': '3 años',
            'es_temporal': False
        },
        
        # Primaria
        {
            'nombre': 'Primaria Turno Matutino',
            'nivel_educativo': niveles['primaria'],
            'descripcion': 'Programa de primaria en horario matutino.',
            'duracion': '6 años',
            'es_temporal': False
        },
        {
            'nombre': 'Primaria Turno Vespertino',
            'nivel_educativo': niveles['primaria'],
            'descripcion': 'Programa de primaria en horario vespertino.',
            'duracion': '6 años',
            'es_temporal': False
        },
        
        # Secundaria
        {
            'nombre': 'Secundaria Turno Matutino',
            'nivel_educativo': niveles['secundaria'],
            'descripcion': 'Programa de secundaria en horario matutino.',
            'duracion': '3 años',
            'es_temporal': False
        },
        {
            'nombre': 'Secundaria Turno Vespertino',
            'nivel_educativo': niveles['secundaria'],
            'descripcion': 'Programa de secundaria en horario vespertino.',
            'duracion': '3 años',
            'es_temporal': False
        },
        
        # Preparatoria
        {
            'nombre': 'Preparatoria Turno Matutino',
            'nivel_educativo': niveles['preparatoria'],
            'descripcion': 'Programa de preparatoria en horario matutino.',
            'duracion': '3 años',
            'es_temporal': False
        },
        {
            'nombre': 'Preparatoria Turno Vespertino',
            'nivel_educativo': niveles['preparatoria'],
            'descripcion': 'Programa de preparatoria en horario vespertino.',
            'duracion': '3 años',
            'es_temporal': False
        },
        
        # Posgrado
        {
            'nombre': 'Maestría en Administración de Empresas',
            'nivel_educativo': niveles['posgrado'],
            'descripcion': 'Maestría en administración de empresas con enfoque en gestión estratégica.',
            'duracion': '2 años',
            'es_temporal': False
        },
        {
            'nombre': 'Doctorado en Ciencias de la Computación',
            'nivel_educativo': niveles['posgrado'],
            'descripcion': 'Doctorado en ciencias de la computación con especialización en IA.',
            'duracion': '4 años',
            'es_temporal': False
        },
        
        # Cursos de Verano
        {
            'nombre': 'Curso de Inglés Básico',
            'nivel_educativo': niveles['curso_verano'],
            'descripcion': 'Curso intensivo de inglés básico durante el verano.',
            'duracion': '4 semanas',
            'es_temporal': True
        },
        {
            'nombre': 'Curso de Matemáticas',
            'nivel_educativo': niveles['curso_verano'],
            'descripcion': 'Curso de refuerzo en matemáticas para estudiantes de secundaria.',
            'duracion': '6 semanas',
            'es_temporal': True
        },
        
        # Diplomados
        {
            'nombre': 'Diplomado en Marketing Digital',
            'nivel_educativo': niveles['diplomado'],
            'descripcion': 'Diplomado especializado en marketing digital y redes sociales.',
            'duracion': '6 meses',
            'es_temporal': False
        },
        {
            'nombre': 'Diplomado en Gestión de Proyectos',
            'nivel_educativo': niveles['diplomado'],
            'descripcion': 'Diplomado en gestión de proyectos con metodologías ágiles.',
            'duracion': '8 meses',
            'es_temporal': False
        },
        
        # Talleres
        {
            'nombre': 'Taller de Pintura',
            'nivel_educativo': niveles['taller'],
            'descripcion': 'Taller de pintura para todas las edades.',
            'duracion': '3 meses',
            'es_temporal': False
        },
        {
            'nombre': 'Taller de Programación',
            'nivel_educativo': niveles['taller'],
            'descripcion': 'Taller introductorio a la programación para jóvenes.',
            'duracion': '2 meses',
            'es_temporal': False
        }
    ]
    
    programas_creados = []
    
    for programa_data in programas_data:
        programa, created = AcademicProgram.objects.get_or_create(
            nombre=programa_data['nombre'],
            nivel_educativo=programa_data['nivel_educativo'],
            defaults=programa_data
        )
        
        if created:
            programas_creados.append(programa)
            print(f"✅ Programa creado: {programa.nombre} ({programa.nivel_educativo.nombre})")
        else:
            print(f"ℹ️  Programa ya existe: {programa.nombre}")
    
    return programas_creados

def main():
    """Función principal."""
    print("🎓 Creando programas académicos de ejemplo...")
    print("=" * 50)
    
    try:
        programas = create_sample_programs()
        
        print("=" * 50)
        print(f"✅ Proceso completado exitosamente!")
        print(f"📊 Total de programas en el sistema: {AcademicProgram.objects.count()}")
        print(f"🆕 Programas creados en esta ejecución: {len(programas)}")
        
        print("\n📋 Programas por nivel educativo:")
        for nivel in EducationalLevel.objects.all():
            programas_nivel = AcademicProgram.objects.filter(nivel_educativo=nivel)
            if programas_nivel.exists():
                print(f"\n  🎯 {nivel.nombre}:")
                for programa in programas_nivel:
                    temporal = " (Temporal)" if programa.es_temporal else ""
                    print(f"    • {programa.nombre} - {programa.duracion}{temporal}")
            
    except Exception as e:
        print(f"❌ Error al crear programas: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 