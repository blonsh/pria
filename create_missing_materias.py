#!/usr/bin/env python
"""
Script para crear las materias faltantes y mejorar la asignación a planes de estudio.
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


def crear_materias_psicologia():
    """Crear materias para Psicología"""
    materias = [
        # Primer semestre
        {'codigo': 'PSI101', 'nombre': 'Introducción a la Psicología', 'creditos': 4},
        {'codigo': 'BIO101', 'nombre': 'Biología Humana', 'creditos': 4},
        {'codigo': 'FIL101', 'nombre': 'Filosofía de la Ciencia', 'creditos': 3},
        {'codigo': 'COM101', 'nombre': 'Comunicación Humana', 'creditos': 3},
        {'codigo': 'MET101', 'nombre': 'Metodología de la Investigación', 'creditos': 4},
        
        # Segundo semestre
        {'codigo': 'PSI201', 'nombre': 'Psicología del Desarrollo', 'creditos': 4},
        {'codigo': 'NEU101', 'nombre': 'Neuropsicología', 'creditos': 4},
        {'codigo': 'EST101', 'nombre': 'Estadística Descriptiva', 'creditos': 4},
        {'codigo': 'SOC101', 'nombre': 'Sociología General', 'creditos': 3},
        {'codigo': 'ING101', 'nombre': 'Inglés I', 'creditos': 3},
        
        # Tercer semestre
        {'codigo': 'PSI301', 'nombre': 'Psicología Social', 'creditos': 4},
        {'codigo': 'PSI302', 'nombre': 'Psicología Cognitiva', 'creditos': 4},
        {'codigo': 'PSI303', 'nombre': 'Psicología de la Personalidad', 'creditos': 4},
        {'codigo': 'EST201', 'nombre': 'Estadística Inferencial', 'creditos': 4},
        {'codigo': 'ING201', 'nombre': 'Inglés II', 'creditos': 3},
        
        # Cuarto semestre
        {'codigo': 'PSI401', 'nombre': 'Psicología Clínica', 'creditos': 4},
        {'codigo': 'PSI402', 'nombre': 'Psicología Educativa', 'creditos': 4},
        {'codigo': 'PSI403', 'nombre': 'Psicología Organizacional', 'creditos': 4},
        {'codigo': 'PSI404', 'nombre': 'Psicopatología', 'creditos': 4},
        {'codigo': 'OPT301', 'nombre': 'Materia Optativa I', 'creditos': 3},
        
        # Quinto semestre
        {'codigo': 'PSI501', 'nombre': 'Evaluación Psicológica', 'creditos': 4},
        {'codigo': 'PSI502', 'nombre': 'Intervención Psicológica', 'creditos': 4},
        {'codigo': 'PSI503', 'nombre': 'Psicología Comunitaria', 'creditos': 4},
        {'codigo': 'PSI504', 'nombre': 'Psicología Forense', 'creditos': 4},
        {'codigo': 'OPT302', 'nombre': 'Materia Optativa II', 'creditos': 3},
        
        # Sexto semestre
        {'codigo': 'PSI601', 'nombre': 'Psicoterapia', 'creditos': 4},
        {'codigo': 'PSI602', 'nombre': 'Psicología de la Salud', 'creditos': 4},
        {'codigo': 'PSI603', 'nombre': 'Psicología del Deporte', 'creditos': 4},
        {'codigo': 'PSI604', 'nombre': 'Psicología Ambiental', 'creditos': 4},
        {'codigo': 'OPT303', 'nombre': 'Materia Optativa III', 'creditos': 3},
        
        # Séptimo semestre
        {'codigo': 'PSI701', 'nombre': 'Seminario de Investigación', 'creditos': 3},
        {'codigo': 'PSI702', 'nombre': 'Psicología Transcultural', 'creditos': 4},
        {'codigo': 'PSI703', 'nombre': 'Psicología Positiva', 'creditos': 4},
        {'codigo': 'OPT401', 'nombre': 'Materia Optativa IV', 'creditos': 3},
        {'codigo': 'OPT402', 'nombre': 'Materia Optativa V', 'creditos': 3},
        
        # Octavo semestre
        {'codigo': 'PSI801', 'nombre': 'Proyecto de Grado', 'creditos': 6},
        {'codigo': 'PSI802', 'nombre': 'Ética Profesional', 'creditos': 3},
        {'codigo': 'OPT403', 'nombre': 'Materia Optativa VI', 'creditos': 3},
        {'codigo': 'OPT404', 'nombre': 'Materia Optativa VII', 'creditos': 3},
    ]
    return materias


def crear_materias_derecho():
    """Crear materias para Derecho"""
    materias = [
        # Primer semestre
        {'codigo': 'DER101', 'nombre': 'Introducción al Derecho', 'creditos': 4},
        {'codigo': 'FIL101', 'nombre': 'Filosofía del Derecho', 'creditos': 4},
        {'codigo': 'HIS101', 'nombre': 'Historia del Derecho', 'creditos': 3},
        {'codigo': 'COM101', 'nombre': 'Comunicación Jurídica', 'creditos': 3},
        {'codigo': 'ING101', 'nombre': 'Inglés I', 'creditos': 3},
        
        # Segundo semestre
        {'codigo': 'DER201', 'nombre': 'Derecho Civil I', 'creditos': 4},
        {'codigo': 'DER202', 'nombre': 'Derecho Constitucional', 'creditos': 4},
        {'codigo': 'DER203', 'nombre': 'Derecho Romano', 'creditos': 3},
        {'codigo': 'DER204', 'nombre': 'Derecho Penal I', 'creditos': 4},
        {'codigo': 'ING201', 'nombre': 'Inglés II', 'creditos': 3},
        
        # Tercer semestre
        {'codigo': 'DER301', 'nombre': 'Derecho Civil II', 'creditos': 4},
        {'codigo': 'DER302', 'nombre': 'Derecho Administrativo', 'creditos': 4},
        {'codigo': 'DER303', 'nombre': 'Derecho Procesal Civil', 'creditos': 4},
        {'codigo': 'DER304', 'nombre': 'Derecho Penal II', 'creditos': 4},
        {'codigo': 'DER305', 'nombre': 'Derecho Mercantil', 'creditos': 3},
        
        # Cuarto semestre
        {'codigo': 'DER401', 'nombre': 'Derecho Civil III', 'creditos': 4},
        {'codigo': 'DER402', 'nombre': 'Derecho Laboral', 'creditos': 4},
        {'codigo': 'DER403', 'nombre': 'Derecho Procesal Penal', 'creditos': 4},
        {'codigo': 'DER404', 'nombre': 'Derecho Tributario', 'creditos': 4},
        {'codigo': 'DER405', 'nombre': 'Derecho Internacional Público', 'creditos': 3},
        
        # Quinto semestre
        {'codigo': 'DER501', 'nombre': 'Derecho Civil IV', 'creditos': 4},
        {'codigo': 'DER502', 'nombre': 'Derecho de Familia', 'creditos': 4},
        {'codigo': 'DER503', 'nombre': 'Derecho Procesal Laboral', 'creditos': 4},
        {'codigo': 'DER504', 'nombre': 'Derecho Internacional Privado', 'creditos': 4},
        {'codigo': 'OPT301', 'nombre': 'Materia Optativa I', 'creditos': 3},
        
        # Sexto semestre
        {'codigo': 'DER601', 'nombre': 'Derecho de Sucesiones', 'creditos': 4},
        {'codigo': 'DER602', 'nombre': 'Derecho de Seguridad Social', 'creditos': 4},
        {'codigo': 'DER603', 'nombre': 'Derecho Procesal Constitucional', 'creditos': 4},
        {'codigo': 'DER604', 'nombre': 'Derecho Ambiental', 'creditos': 4},
        {'codigo': 'OPT302', 'nombre': 'Materia Optativa II', 'creditos': 3},
        
        # Séptimo semestre
        {'codigo': 'DER701', 'nombre': 'Seminario de Investigación', 'creditos': 3},
        {'codigo': 'DER702', 'nombre': 'Derecho de Propiedad Intelectual', 'creditos': 4},
        {'codigo': 'DER703', 'nombre': 'Derecho de la Competencia', 'creditos': 4},
        {'codigo': 'OPT401', 'nombre': 'Materia Optativa III', 'creditos': 3},
        {'codigo': 'OPT402', 'nombre': 'Materia Optativa IV', 'creditos': 3},
        
        # Octavo semestre
        {'codigo': 'DER801', 'nombre': 'Proyecto de Grado', 'creditos': 6},
        {'codigo': 'DER802', 'nombre': 'Ética Profesional', 'creditos': 3},
        {'codigo': 'OPT403', 'nombre': 'Materia Optativa V', 'creditos': 3},
        {'codigo': 'OPT404', 'nombre': 'Materia Optativa VI', 'creditos': 3},
    ]
    return materias


def crear_materias_por_carrera():
    """Crear materias según la carrera"""
    materias_por_carrera = {
        'Ingeniería en Sistemas Computacionales': crear_materias_ingenieria_sistemas(),
        'Contaduría Pública': crear_materias_contabilidad(),
        'Psicología': crear_materias_psicologia(),
        'Derecho': crear_materias_derecho(),
    }
    return materias_por_carrera


def crear_materias_faltantes():
    """Crear las materias faltantes en la base de datos"""
    print("🚀 Creando materias faltantes en la base de datos...")
    
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


def asignar_materias_faltantes():
    """Asignar materias faltantes a los planes de estudio"""
    print("\n🔗 Asignando materias faltantes a planes de estudio...")
    
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
                    
                    # Asignar materias específicas de la carrera
                    materias_carrera = []
                    for materia_data in materias:
                        if nombre_carrera == 'Ingeniería en Sistemas Computacionales':
                            if materia_data['codigo'].startswith(('PRO', 'BD', 'RED', 'SIS', 'WEB', 'ING')):
                                materias_carrera.append(materia_data)
                        elif nombre_carrera == 'Contaduría Pública':
                            if materia_data['codigo'].startswith(('CON', 'FIN', 'AUD')):
                                materias_carrera.append(materia_data)
                        elif nombre_carrera == 'Psicología':
                            if materia_data['codigo'].startswith(('PSI', 'NEU')):
                                materias_carrera.append(materia_data)
                        elif nombre_carrera == 'Derecho':
                            if materia_data['codigo'].startswith(('DER', 'FIL')):
                                materias_carrera.append(materia_data)
                    
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


def mostrar_estadisticas_finales():
    """Mostrar estadísticas finales del sistema"""
    print("\n📊 ESTADÍSTICAS FINALES DEL SISTEMA:")
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
    print("🎓 SCRIPT DE CREACIÓN DE MATERIAS FALTANTES")
    print("=" * 60)
    
    try:
        # Crear materias faltantes
        materias_creadas = crear_materias_faltantes()
        
        # Asignar materias faltantes
        asignaciones_creadas = asignar_materias_faltantes()
        
        # Mostrar estadísticas finales
        mostrar_estadisticas_finales()
        
        print(f"\n✅ Proceso completado exitosamente!")
        print(f"📝 Materias creadas: {materias_creadas}")
        print(f"🔗 Asignaciones realizadas: {asignaciones_creadas}")
        
    except Exception as e:
        print(f"\n❌ Error durante la ejecución: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main() 