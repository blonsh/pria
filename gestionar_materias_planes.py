#!/usr/bin/env python
"""
Script para mostrar cómo gestionar las materias de los planes de estudio.
Este script proporciona ejemplos de cómo acceder y modificar las materias.
"""

import os
import sys
import django
from django.db import transaction

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from core.models import Carrera, Materia
from planes_estudio.models import PlanEstudio, SemestrePlan, MateriaPlan


def mostrar_planes_con_materias():
    """Mostrar todos los planes de estudio con sus materias"""
    print("📖 PLANES DE ESTUDIO CON SUS MATERIAS:")
    print("=" * 60)
    
    planes = PlanEstudio.objects.all()
    
    for plan in planes:
        print(f"\n🎓 PLAN: {plan.nombre}")
        print(f"   📚 Carrera: {plan.carrera.nombre}")
        print(f"   🏫 Centro: {plan.work_center.name}")
        print(f"   📅 Duración: {plan.duracion_semestres} semestres")
        print(f"   📊 Estado: {plan.get_estado_display()}")
        print(f"   💰 Créditos totales: {plan.creditos_totales}")
        print(f"   📝 Créditos actuales: {plan.get_creditos_actuales()}")
        
        semestres = plan.semestres.all().order_by('numero_semestre')
        
        for semestre in semestres:
            print(f"\n   📅 SEMESTRE {semestre.numero_semestre}: {semestre.nombre}")
            print(f"      💰 Créditos del semestre: {semestre.get_creditos_semestre()}")
            
            materias = semestre.materias.all().order_by('orden')
            
            if materias:
                for materia in materias:
                    print(f"      📚 {materia.materia.codigo} - {materia.materia.nombre}")
                    print(f"         💰 Créditos: {materia.creditos}")
                    print(f"         📖 Tipo: {materia.get_tipo_materia_display()}")
                    print(f"         ⏰ Horas: T={materia.horas_teoria}, P={materia.horas_practica}, I={materia.horas_independiente}")
            else:
                print(f"      ⚠️  No hay materias asignadas")
        
        print("\n" + "-" * 60)


def mostrar_estadisticas_detalladas():
    """Mostrar estadísticas detalladas del sistema"""
    print("\n📊 ESTADÍSTICAS DETALLADAS:")
    print("=" * 50)
    
    # Estadísticas generales
    total_planes = PlanEstudio.objects.count()
    total_semestres = SemestrePlan.objects.count()
    total_materias_plan = MateriaPlan.objects.count()
    total_materias = Materia.objects.count()
    
    print(f"📖 Planes de estudio: {total_planes}")
    print(f"📅 Semestres configurados: {total_semestres}")
    print(f"📝 Materias asignadas a planes: {total_materias_plan}")
    print(f"📚 Materias totales en el sistema: {total_materias}")
    
    # Estadísticas por carrera
    print(f"\n🏫 ESTADÍSTICAS POR CARRERA:")
    carreras = Carrera.objects.all()
    
    for carrera in carreras:
        planes_carrera = PlanEstudio.objects.filter(carrera=carrera)
        materias_carrera = carrera.materias.count()
        
        print(f"\n  📚 {carrera.nombre}:")
        print(f"     📖 Planes: {planes_carrera.count()}")
        print(f"     📝 Materias disponibles: {materias_carrera}")
        
        for plan in planes_carrera:
            semestres_plan = plan.semestres.count()
            materias_plan = MateriaPlan.objects.filter(semestre__plan_estudio=plan).count()
            creditos_plan = plan.get_creditos_actuales()
            
            print(f"     📋 Plan '{plan.nombre}':")
            print(f"        📅 Semestres: {semestres_plan}")
            print(f"        📝 Materias asignadas: {materias_plan}")
            print(f"        💰 Créditos: {creditos_plan}/{plan.creditos_totales}")
            print(f"        📊 Estado: {plan.get_estado_display()}")


def mostrar_materias_por_tipo():
    """Mostrar materias organizadas por tipo"""
    print("\n📚 MATERIAS POR TIPO:")
    print("=" * 50)
    
    tipos_materia = MateriaPlan.objects.values_list('tipo_materia', flat=True).distinct()
    
    for tipo in tipos_materia:
        materias_tipo = MateriaPlan.objects.filter(tipo_materia=tipo)
        print(f"\n  📖 {tipo}: {materias_tipo.count()} materias")
        
        # Mostrar algunas materias de ejemplo
        for materia_plan in materias_tipo[:5]:  # Solo las primeras 5
            print(f"     • {materia_plan.materia.codigo} - {materia_plan.materia.nombre}")
        
        if materias_tipo.count() > 5:
            print(f"     ... y {materias_tipo.count() - 5} más")


def mostrar_materias_sin_asignar():
    """Mostrar materias que no están asignadas a ningún plan"""
    print("\n⚠️  MATERIAS SIN ASIGNAR:")
    print("=" * 50)
    
    materias_asignadas = MateriaPlan.objects.values_list('materia_id', flat=True).distinct()
    materias_sin_asignar = Materia.objects.exclude(id__in=materias_asignadas)
    
    print(f"📚 Total de materias sin asignar: {materias_sin_asignar.count()}")
    
    for materia in materias_sin_asignar[:10]:  # Solo las primeras 10
        carreras = materia.carrera.all()
        carreras_str = ", ".join([c.nombre for c in carreras])
        print(f"  • {materia.codigo} - {materia.nombre} (Carreras: {carreras_str})")
    
    if materias_sin_asignar.count() > 10:
        print(f"  ... y {materias_sin_asignar.count() - 10} más")


def mostrar_ejemplos_uso():
    """Mostrar ejemplos de cómo usar las materias en Python"""
    print("\n🐍 EJEMPLOS DE USO EN PYTHON:")
    print("=" * 50)
    
    # Ejemplo 1: Obtener todas las materias de un plan
    print("1. Obtener todas las materias de un plan:")
    plan = PlanEstudio.objects.first()
    if plan:
        print(f"   plan = PlanEstudio.objects.get(id={plan.id})")
        print(f"   materias = MateriaPlan.objects.filter(semestre__plan_estudio=plan)")
        print(f"   # Resultado: {MateriaPlan.objects.filter(semestre__plan_estudio=plan).count()} materias")
    
    # Ejemplo 2: Obtener materias por semestre
    print("\n2. Obtener materias por semestre:")
    semestre = SemestrePlan.objects.first()
    if semestre:
        print(f"   semestre = SemestrePlan.objects.get(id={semestre.id})")
        print(f"   materias = semestre.materias.all()")
        print(f"   # Resultado: {semestre.materias.count()} materias en el semestre")
    
    # Ejemplo 3: Buscar materias por código
    print("\n3. Buscar materias por código:")
    materia = Materia.objects.filter(codigo__startswith='PRO').first()
    if materia:
        print(f"   materia = Materia.objects.get(codigo='{materia.codigo}')")
        print(f"   # Resultado: {materia.nombre}")
    
    # Ejemplo 4: Obtener materias por carrera
    print("\n4. Obtener materias por carrera:")
    carrera = Carrera.objects.first()
    if carrera:
        print(f"   carrera = Carrera.objects.get(id={carrera.id})")
        print(f"   materias = carrera.materias.all()")
        print(f"   # Resultado: {carrera.materias.count()} materias disponibles")


def mostrar_urls_acceso():
    """Mostrar URLs para acceder a las materias desde la web"""
    print("\n🌐 URLs PARA ACCEDER DESDE LA WEB:")
    print("=" * 50)
    
    print("📖 Dashboard de Planes de Estudio:")
    print("   http://localhost:8000/planes-estudio/")
    
    print("\n📋 Lista de Planes:")
    print("   http://localhost:8000/planes-estudio/planes/")
    
    print("\n📝 Crear Nuevo Plan:")
    print("   http://localhost:8000/planes-estudio/planes/crear/")
    
    print("\n📚 Gestión de Competencias:")
    print("   http://localhost:8000/planes-estudio/competencias/")
    
    print("\n📖 Documentación:")
    print("   http://localhost:8000/planes-estudio/documentacion/")
    
    # Mostrar URLs específicas para planes existentes
    planes = PlanEstudio.objects.all()[:3]  # Solo los primeros 3
    for plan in planes:
        print(f"\n📋 Plan '{plan.nombre}':")
        print(f"   Ver detalles: http://localhost:8000/planes-estudio/planes/{plan.id}/")
        print(f"   Editar: http://localhost:8000/planes-estudio/planes/{plan.id}/editar/")
        print(f"   Semestres: http://localhost:8000/planes-estudio/planes/{plan.id}/semestres/")


def main():
    """Función principal del script"""
    print("🎓 SCRIPT DE GESTIÓN DE MATERIAS EN PLANES DE ESTUDIO")
    print("=" * 70)
    
    try:
        # Mostrar información detallada
        mostrar_planes_con_materias()
        mostrar_estadisticas_detalladas()
        mostrar_materias_por_tipo()
        mostrar_materias_sin_asignar()
        mostrar_ejemplos_uso()
        mostrar_urls_acceso()
        
        print("\n✅ Script de gestión completado exitosamente!")
        print("\n💡 PRÓXIMOS PASOS:")
        print("   1. Accede a http://localhost:8000/planes-estudio/")
        print("   2. Explora los planes de estudio creados")
        print("   3. Revisa las materias asignadas a cada semestre")
        print("   4. Crea nuevos planes o modifica los existentes")
        print("   5. Gestiona las competencias y objetivos educativos")
        
    except Exception as e:
        print(f"\n❌ Error durante la ejecución: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main() 