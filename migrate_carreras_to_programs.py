#!/usr/bin/env python3
"""
Script para migrar carreras existentes a programas académicos
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from core.models import Carrera, EducationalLevel, AcademicProgram

def migrate_carreras_to_programs():
    """Migrar carreras existentes a programas académicos."""
    
    # Obtener o crear nivel universitario
    nivel_universidad, created = EducationalLevel.objects.get_or_create(
        nombre='Universidad',
        defaults={
            'orden': 6,
            'activo': True,
            'es_nivel_superior': True
        }
    )
    
    if created:
        print(f"✅ Nivel universitario creado: {nivel_universidad.nombre}")
    else:
        print(f"ℹ️  Nivel universitario ya existe: {nivel_universidad.nombre}")
    
    # Obtener todas las carreras existentes
    carreras = Carrera.objects.all()
    programas_migrados = []
    
    print(f"\n🔄 Migrando {carreras.count()} carreras a programas académicos...")
    
    for carrera in carreras:
        # Crear programa académico
        programa, created = AcademicProgram.objects.get_or_create(
            nombre=carrera.nombre,
            nivel_educativo=nivel_universidad,
            defaults={
                'descripcion': carrera.descripcion,
                'duracion': f"{carrera.duracion_anios} años",
                'es_temporal': False,
                'activo': carrera.activa
            }
        )
        
        if created:
            programas_migrados.append(programa)
            print(f"✅ Programa migrado: {programa.nombre}")
        else:
            print(f"ℹ️  Programa ya existe: {programa.nombre}")
    
    return programas_migrados

def main():
    """Función principal."""
    print("🔄 Migrando carreras a programas académicos...")
    print("=" * 50)
    
    try:
        programas = migrate_carreras_to_programs()
        
        print("=" * 50)
        print(f"✅ Migración completada exitosamente!")
        print(f"📊 Total de programas académicos: {AcademicProgram.objects.count()}")
        print(f"🆕 Programas migrados en esta ejecución: {len(programas)}")
        
        print("\n📋 Programas académicos disponibles:")
        for programa in AcademicProgram.objects.all():
            print(f"  • {programa.nombre} ({programa.nivel_educativo.nombre})")
            
    except Exception as e:
        print(f"❌ Error en la migración: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 