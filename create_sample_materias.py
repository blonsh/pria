#!/usr/bin/env python
"""
Script para crear materias de ejemplo y asignarlas a planes de estudio.
Este script genera materias comunes para diferentes carreras y las asigna a los planes existentes.
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
from workcenter.models import WorkCenter


def crear_materias_ingenieria_sistemas():
    """Crear materias para Ingeniería en Sistemas"""
    materias = [
        # Primer semestre
        {'codigo': 'MAT101', 'nombre': 'Matemáticas I', 'creditos': 4},
        {'codigo': 'FIS101', 'nombre': 'Física I', 'creditos': 4},
        {'codigo': 'PRO101', 'nombre': 'Programación I', 'creditos': 5},
        {'codigo': 'ING101', 'nombre': 'Introducción a la Ingeniería', 'creditos': 3},
        {'codigo': 'COM101', 'nombre': 'Comunicación Oral y Escrita', 'creditos': 3},
        
        # Segundo semestre
        {'codigo': 'MAT102', 'nombre': 'Matemáticas II', 'creditos': 4},
        {'codigo': 'FIS102', 'nombre': 'Física II', 'creditos': 4},
        {'codigo': 'PRO102', 'nombre': 'Programación II', 'creditos': 5},
        {'codigo': 'EST101', 'nombre': 'Estadística I', 'creditos': 3},
        {'codigo': 'ING102', 'nombre': 'Dibujo Técnico', 'creditos': 3},
        
        # Tercer semestre
        {'codigo': 'MAT201', 'nombre': 'Cálculo Diferencial', 'creditos': 4},
        {'codigo': 'PRO201', 'nombre': 'Estructuras de Datos', 'creditos': 5},
        {'codigo': 'BD101', 'nombre': 'Bases de Datos I', 'creditos': 4},
        {'codigo': 'RED101', 'nombre': 'Redes de Computadoras', 'creditos': 4},
        {'codigo': 'ING201', 'nombre': 'Investigación de Operaciones', 'creditos': 3},
        
        # Cuarto semestre
        {'codigo': 'MAT202', 'nombre': 'Cálculo Integral', 'creditos': 4},
        {'codigo': 'PRO202', 'nombre': 'Programación Orientada a Objetos', 'creditos': 5},
        {'codigo': 'BD201', 'nombre': 'Bases de Datos II', 'creditos': 4},
        {'codigo': 'SIS201', 'nombre': 'Sistemas Operativos', 'creditos': 4},
        {'codigo': 'ING202', 'nombre': 'Probabilidad y Estadística', 'creditos': 3},
        
        # Quinto semestre
        {'codigo': 'PRO301', 'nombre': 'Análisis y Diseño de Sistemas', 'creditos': 5},
        {'codigo': 'WEB201', 'nombre': 'Desarrollo Web', 'creditos': 4},
        {'codigo': 'SIS301', 'nombre': 'Arquitectura de Computadoras', 'creditos': 4},
        {'codigo': 'ING301', 'nombre': 'Ingeniería de Software', 'creditos': 4},
        {'codigo': 'OPT301', 'nombre': 'Materia Optativa I', 'creditos': 3},
        
        # Sexto semestre
        {'codigo': 'PRO302', 'nombre': 'Desarrollo de Software', 'creditos': 5},
        {'codigo': 'WEB301', 'nombre': 'Aplicaciones Web Avanzadas', 'creditos': 4},
        {'codigo': 'SIS302', 'nombre': 'Sistemas Distribuidos', 'creditos': 4},
        {'codigo': 'ING302', 'nombre': 'Gestión de Proyectos', 'creditos': 4},
        {'codigo': 'OPT302', 'nombre': 'Materia Optativa II', 'creditos': 3},
        
        # Séptimo semestre
        {'codigo': 'PRO401', 'nombre': 'Inteligencia Artificial', 'creditos': 4},
        {'codigo': 'SIS401', 'nombre': 'Seguridad Informática', 'creditos': 4},
        {'codigo': 'ING401', 'nombre': 'Seminario de Investigación', 'creditos': 3},
        {'codigo': 'OPT401', 'nombre': 'Materia Optativa III', 'creditos': 3},
        {'codigo': 'OPT402', 'nombre': 'Materia Optativa IV', 'creditos': 3},
        
        # Octavo semestre
        {'codigo': 'PRO402', 'nombre': 'Proyecto de Grado', 'creditos': 6},
        {'codigo': 'ING402', 'nombre': 'Ética Profesional', 'creditos': 3},
        {'codigo': 'OPT403', 'nombre': 'Materia Optativa V', 'creditos': 3},
        {'codigo': 'OPT404', 'nombre': 'Materia Optativa VI', 'creditos': 3},
    ]
    return materias


def crear_materias_administracion():
    """Crear materias para Administración de Empresas"""
    materias = [
        # Primer semestre
        {'codigo': 'MAT101', 'nombre': 'Matemáticas Básicas', 'creditos': 4},
        {'codigo': 'ECO101', 'nombre': 'Introducción a la Economía', 'creditos': 4},
        {'codigo': 'ADM101', 'nombre': 'Introducción a la Administración', 'creditos': 4},
        {'codigo': 'COM101', 'nombre': 'Comunicación Empresarial', 'creditos': 3},
        {'codigo': 'ING101', 'nombre': 'Inglés I', 'creditos': 3},
        
        # Segundo semestre
        {'codigo': 'EST101', 'nombre': 'Estadística Descriptiva', 'creditos': 4},
        {'codigo': 'ECO201', 'nombre': 'Microeconomía', 'creditos': 4},
        {'codigo': 'ADM201', 'nombre': 'Teoría Organizacional', 'creditos': 4},
        {'codigo': 'CON101', 'nombre': 'Contabilidad I', 'creditos': 4},
        {'codigo': 'ING201', 'nombre': 'Inglés II', 'creditos': 3},
        
        # Tercer semestre
        {'codigo': 'EST201', 'nombre': 'Estadística Inferencial', 'creditos': 4},
        {'codigo': 'ECO301', 'nombre': 'Macroeconomía', 'creditos': 4},
        {'codigo': 'ADM301', 'nombre': 'Gestión de Recursos Humanos', 'creditos': 4},
        {'codigo': 'CON201', 'nombre': 'Contabilidad II', 'creditos': 4},
        {'codigo': 'MAR101', 'nombre': 'Marketing I', 'creditos': 4},
        
        # Cuarto semestre
        {'codigo': 'FIN101', 'nombre': 'Finanzas I', 'creditos': 4},
        {'codigo': 'ADM401', 'nombre': 'Gestión de Operaciones', 'creditos': 4},
        {'codigo': 'CON301', 'nombre': 'Contabilidad de Costos', 'creditos': 4},
        {'codigo': 'MAR201', 'nombre': 'Marketing II', 'creditos': 4},
        {'codigo': 'DER101', 'nombre': 'Derecho Comercial', 'creditos': 3},
        
        # Quinto semestre
        {'codigo': 'FIN201', 'nombre': 'Finanzas II', 'creditos': 4},
        {'codigo': 'ADM501', 'nombre': 'Gestión Estratégica', 'creditos': 4},
        {'codigo': 'MAR301', 'nombre': 'Investigación de Mercados', 'creditos': 4},
        {'codigo': 'ADM502', 'nombre': 'Gestión de Calidad', 'creditos': 4},
        {'codigo': 'OPT301', 'nombre': 'Materia Optativa I', 'creditos': 3},
        
        # Sexto semestre
        {'codigo': 'FIN301', 'nombre': 'Finanzas Corporativas', 'creditos': 4},
        {'codigo': 'ADM601', 'nombre': 'Gestión de Proyectos', 'creditos': 4},
        {'codigo': 'ADM602', 'nombre': 'Emprendimiento', 'creditos': 4},
        {'codigo': 'ADM603', 'nombre': 'Gestión Internacional', 'creditos': 4},
        {'codigo': 'OPT302', 'nombre': 'Materia Optativa II', 'creditos': 3},
        
        # Séptimo semestre
        {'codigo': 'ADM701', 'nombre': 'Seminario de Investigación', 'creditos': 3},
        {'codigo': 'ADM702', 'nombre': 'Gestión del Cambio', 'creditos': 4},
        {'codigo': 'ADM703', 'nombre': 'Responsabilidad Social', 'creditos': 3},
        {'codigo': 'OPT401', 'nombre': 'Materia Optativa III', 'creditos': 3},
        {'codigo': 'OPT402', 'nombre': 'Materia Optativa IV', 'creditos': 3},
        
        # Octavo semestre
        {'codigo': 'ADM801', 'nombre': 'Proyecto de Grado', 'creditos': 6},
        {'codigo': 'ADM802', 'nombre': 'Ética Empresarial', 'creditos': 3},
        {'codigo': 'OPT403', 'nombre': 'Materia Optativa V', 'creditos': 3},
        {'codigo': 'OPT404', 'nombre': 'Materia Optativa VI', 'creditos': 3},
    ]
    return materias


def crear_materias_contabilidad():
    """Crear materias para Contabilidad"""
    materias = [
        # Primer semestre
        {'codigo': 'MAT101', 'nombre': 'Matemáticas Básicas', 'creditos': 4},
        {'codigo': 'CON101', 'nombre': 'Contabilidad Básica', 'creditos': 5},
        {'codigo': 'ECO101', 'nombre': 'Introducción a la Economía', 'creditos': 4},
        {'codigo': 'COM101', 'nombre': 'Comunicación Empresarial', 'creditos': 3},
        {'codigo': 'ING101', 'nombre': 'Inglés I', 'creditos': 3},
        
        # Segundo semestre
        {'codigo': 'CON201', 'nombre': 'Contabilidad Intermedia', 'creditos': 5},
        {'codigo': 'EST101', 'nombre': 'Estadística Descriptiva', 'creditos': 4},
        {'codigo': 'ECO201', 'nombre': 'Microeconomía', 'creditos': 4},
        {'codigo': 'DER101', 'nombre': 'Derecho Civil', 'creditos': 3},
        {'codigo': 'ING201', 'nombre': 'Inglés II', 'creditos': 3},
        
        # Tercer semestre
        {'codigo': 'CON301', 'nombre': 'Contabilidad Avanzada', 'creditos': 5},
        {'codigo': 'CON302', 'nombre': 'Contabilidad de Costos', 'creditos': 4},
        {'codigo': 'FIN101', 'nombre': 'Finanzas I', 'creditos': 4},
        {'codigo': 'DER201', 'nombre': 'Derecho Comercial', 'creditos': 3},
        {'codigo': 'EST201', 'nombre': 'Estadística Inferencial', 'creditos': 4},
        
        # Cuarto semestre
        {'codigo': 'CON401', 'nombre': 'Auditoría I', 'creditos': 4},
        {'codigo': 'CON402', 'nombre': 'Contabilidad Gubernamental', 'creditos': 4},
        {'codigo': 'FIN201', 'nombre': 'Finanzas II', 'creditos': 4},
        {'codigo': 'CON403', 'nombre': 'Sistemas de Información Contable', 'creditos': 4},
        {'codigo': 'DER301', 'nombre': 'Derecho Tributario', 'creditos': 3},
        
        # Quinto semestre
        {'codigo': 'CON501', 'nombre': 'Auditoría II', 'creditos': 4},
        {'codigo': 'CON502', 'nombre': 'Contabilidad Internacional', 'creditos': 4},
        {'codigo': 'CON503', 'nombre': 'Análisis Financiero', 'creditos': 4},
        {'codigo': 'CON504', 'nombre': 'Contabilidad de Sociedades', 'creditos': 4},
        {'codigo': 'OPT301', 'nombre': 'Materia Optativa I', 'creditos': 3},
        
        # Sexto semestre
        {'codigo': 'CON601', 'nombre': 'Auditoría Forense', 'creditos': 4},
        {'codigo': 'CON602', 'nombre': 'Contabilidad Pública', 'creditos': 4},
        {'codigo': 'CON603', 'nombre': 'Gestión Tributaria', 'creditos': 4},
        {'codigo': 'CON604', 'nombre': 'Normas Internacionales', 'creditos': 4},
        {'codigo': 'OPT302', 'nombre': 'Materia Optativa II', 'creditos': 3},
        
        # Séptimo semestre
        {'codigo': 'CON701', 'nombre': 'Seminario de Investigación', 'creditos': 3},
        {'codigo': 'CON702', 'nombre': 'Auditoría de Sistemas', 'creditos': 4},
        {'codigo': 'CON703', 'nombre': 'Contabilidad Ambiental', 'creditos': 3},
        {'codigo': 'OPT401', 'nombre': 'Materia Optativa III', 'creditos': 3},
        {'codigo': 'OPT402', 'nombre': 'Materia Optativa IV', 'creditos': 3},
        
        # Octavo semestre
        {'codigo': 'CON801', 'nombre': 'Proyecto de Grado', 'creditos': 6},
        {'codigo': 'CON802', 'nombre': 'Ética Profesional', 'creditos': 3},
        {'codigo': 'OPT403', 'nombre': 'Materia Optativa V', 'creditos': 3},
        {'codigo': 'OPT404', 'nombre': 'Materia Optativa VI', 'creditos': 3},
    ]
    return materias


def crear_materias_medicina():
    """Crear materias para Medicina"""
    materias = [
        # Primer semestre
        {'codigo': 'BIO101', 'nombre': 'Biología Celular', 'creditos': 5},
        {'codigo': 'QUI101', 'nombre': 'Química General', 'creditos': 4},
        {'codigo': 'FIS101', 'nombre': 'Física Médica', 'creditos': 4},
        {'codigo': 'MAT101', 'nombre': 'Matemáticas para Medicina', 'creditos': 3},
        {'codigo': 'COM101', 'nombre': 'Comunicación en Salud', 'creditos': 3},
        
        # Segundo semestre
        {'codigo': 'BIO201', 'nombre': 'Anatomía I', 'creditos': 6},
        {'codigo': 'BIO202', 'nombre': 'Fisiología I', 'creditos': 5},
        {'codigo': 'QUI201', 'nombre': 'Bioquímica I', 'creditos': 4},
        {'codigo': 'HIS101', 'nombre': 'Histología', 'creditos': 4},
        {'codigo': 'ING101', 'nombre': 'Inglés Médico I', 'creditos': 3},
        
        # Tercer semestre
        {'codigo': 'BIO301', 'nombre': 'Anatomía II', 'creditos': 6},
        {'codigo': 'BIO302', 'nombre': 'Fisiología II', 'creditos': 5},
        {'codigo': 'QUI301', 'nombre': 'Bioquímica II', 'creditos': 4},
        {'codigo': 'PAT101', 'nombre': 'Patología General', 'creditos': 4},
        {'codigo': 'ING201', 'nombre': 'Inglés Médico II', 'creditos': 3},
        
        # Cuarto semestre
        {'codigo': 'MED401', 'nombre': 'Semiología', 'creditos': 5},
        {'codigo': 'MED402', 'nombre': 'Propedéutica', 'creditos': 4},
        {'codigo': 'FAR101', 'nombre': 'Farmacología I', 'creditos': 4},
        {'codigo': 'MIC101', 'nombre': 'Microbiología', 'creditos': 4},
        {'codigo': 'PAR101', 'nombre': 'Parasitología', 'creditos': 3},
        
        # Quinto semestre
        {'codigo': 'MED501', 'nombre': 'Medicina Interna I', 'creditos': 6},
        {'codigo': 'MED502', 'nombre': 'Cirugía I', 'creditos': 5},
        {'codigo': 'FAR201', 'nombre': 'Farmacología II', 'creditos': 4},
        {'codigo': 'RAD101', 'nombre': 'Radiología', 'creditos': 3},
        {'codigo': 'OPT301', 'nombre': 'Materia Optativa I', 'creditos': 3},
        
        # Sexto semestre
        {'codigo': 'MED601', 'nombre': 'Medicina Interna II', 'creditos': 6},
        {'codigo': 'MED602', 'nombre': 'Cirugía II', 'creditos': 5},
        {'codigo': 'PED101', 'nombre': 'Pediatría', 'creditos': 4},
        {'codigo': 'GIN101', 'nombre': 'Ginecología', 'creditos': 4},
        {'codigo': 'OPT302', 'nombre': 'Materia Optativa II', 'creditos': 3},
        
        # Séptimo semestre
        {'codigo': 'MED701', 'nombre': 'Medicina de Urgencias', 'creditos': 4},
        {'codigo': 'MED702', 'nombre': 'Medicina Preventiva', 'creditos': 4},
        {'codigo': 'MED703', 'nombre': 'Medicina Legal', 'creditos': 3},
        {'codigo': 'OPT401', 'nombre': 'Materia Optativa III', 'creditos': 3},
        {'codigo': 'OPT402', 'nombre': 'Materia Optativa IV', 'creditos': 3},
        
        # Octavo semestre
        {'codigo': 'MED801', 'nombre': 'Internado Rotatorio', 'creditos': 8},
        {'codigo': 'MED802', 'nombre': 'Ética Médica', 'creditos': 3},
        {'codigo': 'OPT403', 'nombre': 'Materia Optativa V', 'creditos': 3},
        {'codigo': 'OPT404', 'nombre': 'Materia Optativa VI', 'creditos': 3},
    ]
    return materias


def crear_materias_por_carrera():
    """Crear materias según la carrera"""
    materias_por_carrera = {
        'Ingeniería en Sistemas': crear_materias_ingenieria_sistemas(),
        'Administración de Empresas': crear_materias_administracion(),
        'Contabilidad': crear_materias_contabilidad(),
        'Medicina': crear_materias_medicina(),
    }
    return materias_por_carrera


def crear_materias_en_db():
    """Crear las materias en la base de datos"""
    print("🚀 Creando materias en la base de datos...")
    
    materias_por_carrera = crear_materias_por_carrera()
    materias_creadas = 0
    
    with transaction.atomic():
        for nombre_carrera, materias in materias_por_carrera.items():
            try:
                carrera = Carrera.objects.get(nombre=nombre_carrera)
                print(f"\n📚 Procesando carrera: {nombre_carrera}")
                
                for materia_data in materias:
                    materia, created = Materia.objects.get_or_create(
                        codigo=materia_data['codigo'],
                        defaults={
                            'nombre': materia_data['nombre'],
                            'creditos': materia_data['creditos']
                        }
                    )
                    
                    if created:
                        print(f"  ✅ Creada: {materia.codigo} - {materia.nombre}")
                        materias_creadas += 1
                    else:
                        print(f"  ⚠️  Ya existe: {materia.codigo} - {materia.nombre}")
                    
                    # Asignar materia a la carrera
                    materia.carrera.add(carrera)
                
            except Carrera.DoesNotExist:
                print(f"  ❌ Carrera no encontrada: {nombre_carrera}")
    
    print(f"\n🎉 Proceso completado. {materias_creadas} materias nuevas creadas.")
    return materias_creadas


def asignar_materias_a_planes():
    """Asignar materias a los planes de estudio existentes"""
    print("\n🔗 Asignando materias a planes de estudio...")
    
    materias_por_carrera = crear_materias_por_carrera()
    asignaciones_creadas = 0
    
    with transaction.atomic():
        for nombre_carrera, materias in materias_por_carrera.items():
            try:
                carrera = Carrera.objects.get(nombre=nombre_carrera)
                planes = PlanEstudio.objects.filter(carrera=carrera)
                
                print(f"\n📋 Procesando planes de {nombre_carrera}:")
                
                for plan in planes:
                    print(f"  📖 Plan: {plan.nombre}")
                    
                    # Crear semestres si no existen
                    for semestre_num in range(1, plan.duracion_semestres + 1):
                        semestre, created = SemestrePlan.objects.get_or_create(
                            plan_estudio=plan,
                            numero_semestre=semestre_num,
                            defaults={
                                'nombre': f'Semestre {semestre_num}',
                                'creditos_semestre': 0
                            }
                        )
                        
                        if created:
                            print(f"    📅 Creado semestre {semestre_num}")
                    
                    # Asignar materias a semestres
                    materias_carrera = [m for m in materias if m['codigo'].startswith(('MAT', 'FIS', 'QUI', 'BIO', 'PRO', 'ECO', 'ADM', 'CON', 'MED', 'FAR', 'PED', 'GIN'))]
                    
                    for i, materia_data in enumerate(materias_carrera):
                        try:
                            materia = Materia.objects.get(codigo=materia_data['codigo'])
                            semestre_num = (i // 5) + 1  # 5 materias por semestre
                            
                            if semestre_num <= plan.duracion_semestres:
                                semestre = SemestrePlan.objects.get(
                                    plan_estudio=plan,
                                    numero_semestre=semestre_num
                                )
                                
                                materia_plan, created = MateriaPlan.objects.get_or_create(
                                    semestre=semestre,
                                    materia=materia,
                                    defaults={
                                        'tipo_materia': 'OBLIGATORIA',
                                        'creditos': materia_data['creditos'],
                                        'horas_teoria': materia_data['creditos'] * 2,
                                        'horas_practica': materia_data['creditos'],
                                        'horas_independiente': materia_data['creditos'] * 2,
                                        'orden': (i % 5) + 1
                                    }
                                )
                                
                                if created:
                                    print(f"      📝 Asignada: {materia.codigo} al semestre {semestre_num}")
                                    asignaciones_creadas += 1
                                else:
                                    print(f"      ⚠️  Ya asignada: {materia.codigo}")
                        
                        except Materia.DoesNotExist:
                            print(f"      ❌ Materia no encontrada: {materia_data['codigo']}")
                        except SemestrePlan.DoesNotExist:
                            print(f"      ❌ Semestre no encontrado: {semestre_num}")
                
            except Carrera.DoesNotExist:
                print(f"  ❌ Carrera no encontrada: {nombre_carrera}")
    
    print(f"\n🎉 Asignación completada. {asignaciones_creadas} materias asignadas a planes.")
    return asignaciones_creadas


def mostrar_estadisticas():
    """Mostrar estadísticas del sistema"""
    print("\n📊 ESTADÍSTICAS DEL SISTEMA:")
    print("=" * 50)
    
    # Estadísticas de carreras
    carreras = Carrera.objects.all()
    print(f"🏫 Carreras: {carreras.count()}")
    for carrera in carreras:
        materias_count = carrera.materias.count()
        planes_count = carrera.planes_estudio.count()
        print(f"  • {carrera.nombre}: {materias_count} materias, {planes_count} planes")
    
    # Estadísticas de materias
    materias = Materia.objects.all()
    print(f"\n📚 Materias totales: {materias.count()}")
    
    # Estadísticas de planes
    planes = PlanEstudio.objects.all()
    print(f"📖 Planes de estudio: {planes.count()}")
    
    # Estadísticas de semestres
    semestres = SemestrePlan.objects.all()
    print(f"📅 Semestres configurados: {semestres.count()}")
    
    # Estadísticas de materias asignadas
    materias_plan = MateriaPlan.objects.all()
    print(f"📝 Materias asignadas a planes: {materias_plan.count()}")
    
    print("=" * 50)


def main():
    """Función principal del script"""
    print("🎓 SCRIPT DE CREACIÓN DE MATERIAS PARA PLANES DE ESTUDIO")
    print("=" * 60)
    
    try:
        # Crear materias
        materias_creadas = crear_materias_en_db()
        
        # Asignar materias a planes
        asignaciones_creadas = asignar_materias_a_planes()
        
        # Mostrar estadísticas
        mostrar_estadisticas()
        
        print(f"\n✅ Proceso completado exitosamente!")
        print(f"📝 Materias creadas: {materias_creadas}")
        print(f"🔗 Asignaciones realizadas: {asignaciones_creadas}")
        
    except Exception as e:
        print(f"\n❌ Error durante la ejecución: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main() 