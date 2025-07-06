#!/usr/bin/env python3
"""
Script para crear cursos de ejemplo para el sistema PRIA
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from core.models import Materia, Docente, Curso
from django.contrib.auth.models import User

def create_sample_courses():
    """Crear cursos de ejemplo."""
    
    # Crear materias de ejemplo
    materias_data = [
        {
            'codigo': 'MAT101',
            'nombre': 'Matemáticas Básicas',
            'creditos': 6
        },
        {
            'codigo': 'FIS101',
            'nombre': 'Física I',
            'creditos': 8
        },
        {
            'codigo': 'PRO101',
            'nombre': 'Programación I',
            'creditos': 10
        },
        {
            'codigo': 'ING101',
            'nombre': 'Inglés Técnico',
            'creditos': 4
        },
        {
            'codigo': 'HIS101',
            'nombre': 'Historia de México',
            'creditos': 6
        },
        {
            'codigo': 'LIT101',
            'nombre': 'Literatura Universal',
            'creditos': 6
        },
        {
            'codigo': 'BIO101',
            'nombre': 'Biología General',
            'creditos': 8
        },
        {
            'codigo': 'QUI101',
            'nombre': 'Química General',
            'creditos': 8
        },
        {
            'codigo': 'ECO101',
            'nombre': 'Economía Básica',
            'creditos': 6
        },
        {
            'codigo': 'FIL101',
            'nombre': 'Filosofía',
            'creditos': 4
        }
    ]
    
    materias_creadas = []
    
    for materia_data in materias_data:
        materia, created = Materia.objects.get_or_create(
            codigo=materia_data['codigo'],
            defaults=materia_data
        )
        
        if created:
            materias_creadas.append(materia)
            print(f"✅ Materia creada: {materia.codigo} - {materia.nombre}")
        else:
            print(f"ℹ️  Materia ya existe: {materia.codigo} - {materia.nombre}")
    
    # Crear docente de ejemplo si no existe
    try:
        docente_user = User.objects.get(username='docente1')
    except User.DoesNotExist:
        docente_user = User.objects.create_user(
            username='docente1',
            first_name='Juan',
            last_name='Pérez',
            email='juan.perez@example.com',
            password='docente123'
        )
        print(f"✅ Usuario docente creado: {docente_user.username}")
    
    docente, created = Docente.objects.get_or_create(
        user=docente_user,
        defaults={
            'especialidad': 'Matemáticas',
            'fecha_contratacion': '2023-01-15'
        }
    )
    
    if created:
        print(f"✅ Docente creado: {docente.user.first_name} {docente.user.last_name}")
    else:
        print(f"ℹ️  Docente ya existe: {docente.user.first_name} {docente.user.last_name}")
    
    # Crear cursos de ejemplo
    cursos_data = [
        {
            'materia': Materia.objects.get(codigo='MAT101'),
            'docente': docente,
            'anio_academico': 2024,
            'semestre': 1,
            'cupo_maximo': 30
        },
        {
            'materia': Materia.objects.get(codigo='FIS101'),
            'docente': docente,
            'anio_academico': 2024,
            'semestre': 1,
            'cupo_maximo': 25
        },
        {
            'materia': Materia.objects.get(codigo='PRO101'),
            'docente': docente,
            'anio_academico': 2024,
            'semestre': 1,
            'cupo_maximo': 20
        },
        {
            'materia': Materia.objects.get(codigo='ING101'),
            'docente': docente,
            'anio_academico': 2024,
            'semestre': 1,
            'cupo_maximo': 35
        },
        {
            'materia': Materia.objects.get(codigo='HIS101'),
            'docente': docente,
            'anio_academico': 2024,
            'semestre': 1,
            'cupo_maximo': 40
        },
        {
            'materia': Materia.objects.get(codigo='LIT101'),
            'docente': docente,
            'anio_academico': 2024,
            'semestre': 1,
            'cupo_maximo': 30
        },
        {
            'materia': Materia.objects.get(codigo='BIO101'),
            'docente': docente,
            'anio_academico': 2024,
            'semestre': 1,
            'cupo_maximo': 25
        },
        {
            'materia': Materia.objects.get(codigo='QUI101'),
            'docente': docente,
            'anio_academico': 2024,
            'semestre': 1,
            'cupo_maximo': 25
        },
        {
            'materia': Materia.objects.get(codigo='ECO101'),
            'docente': docente,
            'anio_academico': 2024,
            'semestre': 1,
            'cupo_maximo': 30
        },
        {
            'materia': Materia.objects.get(codigo='FIL101'),
            'docente': docente,
            'anio_academico': 2024,
            'semestre': 1,
            'cupo_maximo': 35
        }
    ]
    
    cursos_creados = []
    
    for curso_data in cursos_data:
        curso, created = Curso.objects.get_or_create(
            materia=curso_data['materia'],
            anio_academico=curso_data['anio_academico'],
            semestre=curso_data['semestre'],
            defaults=curso_data
        )
        
        if created:
            cursos_creados.append(curso)
            print(f"✅ Curso creado: {curso.materia.nombre} ({curso.anio_academico}-{curso.semestre})")
        else:
            print(f"ℹ️  Curso ya existe: {curso.materia.nombre} ({curso.anio_academico}-{curso.semestre})")
    
    return materias_creadas, cursos_creados

def main():
    """Función principal."""
    print("🎓 Creando cursos de ejemplo...")
    print("=" * 50)
    
    try:
        materias, cursos = create_sample_courses()
        
        print("=" * 50)
        print(f"✅ Proceso completado exitosamente!")
        print(f"📊 Total de materias en el sistema: {Materia.objects.count()}")
        print(f"📊 Total de cursos en el sistema: {Curso.objects.count()}")
        print(f"🆕 Materias creadas en esta ejecución: {len(materias)}")
        print(f"🆕 Cursos creados en esta ejecución: {len(cursos)}")
        
        print("\n📋 Cursos disponibles:")
        for curso in Curso.objects.all():
            cupo_disponible = curso.cupo_maximo - curso.matricula_set.count()
            print(f"  • {curso.materia.nombre} ({curso.materia.codigo}) - Cupo: {cupo_disponible}/{curso.cupo_maximo}")
            
    except Exception as e:
        print(f"❌ Error al crear cursos: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 