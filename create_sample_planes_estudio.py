#!/usr/bin/env python
"""
Script para crear datos de muestra para el módulo de planes de estudios.
"""
import os
import sys
import django
from datetime import date, datetime

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import Carrera, Materia
from workcenter.models import WorkCenter, SchoolCycle
from planes_estudio.models import (
    PlanEstudio, SemestrePlan, MateriaPlan, Competencia,
    ObjetivoEducativo, PerfilEgreso
)


def crear_usuarios_muestra():
    """Crear usuarios de muestra si no existen."""
    if not User.objects.filter(username='admin_planes').exists():
        admin_user = User.objects.create_user(
            username='admin_planes',
            email='admin_planes@example.com',
            password='admin123',
            first_name='Administrador',
            last_name='Planes'
        )
        print(f"Usuario creado: {admin_user.username}")
    else:
        admin_user = User.objects.get(username='admin_planes')
    
    return admin_user


def crear_centros_trabajo():
    """Crear centros de trabajo de muestra."""
    centros = []
    
    centros_data = [
        {
            'name': 'Centro de Estudios Tecnológicos',
            'address': 'Av. Tecnología 123, Ciudad de México',
            'director_name': 'Dr. Carlos Méndez',
            'school_control_name': 'Lic. Ana García'
        },
        {
            'name': 'Instituto Politécnico del Norte',
            'address': 'Blvd. Industrial 456, Monterrey',
            'director_name': 'Ing. Roberto Silva',
            'school_control_name': 'Lic. María López'
        },
        {
            'name': 'Centro Universitario del Sur',
            'address': 'Calle Universidad 789, Guadalajara',
            'director_name': 'Dr. Patricia Ruiz',
            'school_control_name': 'Lic. Juan Pérez'
        }
    ]
    
    for data in centros_data:
        centro, created = WorkCenter.objects.get_or_create(
            name=data['name'],
            defaults=data
        )
        if created:
            print(f"Centro de trabajo creado: {centro.name}")
        centros.append(centro)
    
    return centros


def crear_ciclos_escolares(centros):
    """Crear ciclos escolares de muestra."""
    ciclos = []
    
    for centro in centros:
        ciclo_data = {
            'work_center': centro,
            'name': f'Ciclo 2024-2025 - {centro.name}',
            'start_date': date(2024, 8, 1),
            'end_date': date(2025, 7, 31),
            'is_active': True
        }
        
        ciclo, created = SchoolCycle.objects.get_or_create(
            name=ciclo_data['name'],
            work_center=centro,
            defaults=ciclo_data
        )
        if created:
            print(f"Ciclo escolar creado: {ciclo.name}")
        ciclos.append(ciclo)
    
    return ciclos


def crear_carreras_muestra():
    """Crear carreras de muestra."""
    carreras = []
    
    carreras_data = [
        {
            'nombre': 'Ingeniería en Sistemas Computacionales',
            'descripcion': 'Forma profesionales capaces de diseñar, desarrollar e implementar soluciones tecnológicas.',
            'duracion_anios': 4
        },
        {
            'nombre': 'Ingeniería Industrial',
            'descripcion': 'Forma profesionales para optimizar procesos productivos y de gestión.',
            'duracion_anios': 4
        },
        {
            'nombre': 'Administración de Empresas',
            'descripcion': 'Forma profesionales para la gestión y administración de organizaciones.',
            'duracion_anios': 4
        },
        {
            'nombre': 'Contaduría Pública',
            'descripcion': 'Forma profesionales para la gestión financiera y contable.',
            'duracion_anios': 4
        }
    ]
    
    for data in carreras_data:
        carrera, created = Carrera.objects.get_or_create(
            nombre=data['nombre'],
            defaults=data
        )
        if created:
            print(f"Carrera creada: {carrera.nombre}")
        carreras.append(carrera)
    
    return carreras


def crear_materias_muestra(carreras):
    """Crear materias de muestra para cada carrera."""
    materias_por_carrera = {
        'Ingeniería en Sistemas Computacionales': [
            {'nombre': 'Programación I', 'codigo': 'ISC101', 'creditos': 8},
            {'nombre': 'Matemáticas Discretas', 'codigo': 'ISC102', 'creditos': 6},
            {'nombre': 'Fundamentos de Computación', 'codigo': 'ISC103', 'creditos': 6},
            {'nombre': 'Programación II', 'codigo': 'ISC201', 'creditos': 8},
            {'nombre': 'Estructuras de Datos', 'codigo': 'ISC202', 'creditos': 8},
            {'nombre': 'Bases de Datos', 'codigo': 'ISC203', 'creditos': 8},
            {'nombre': 'Programación Orientada a Objetos', 'codigo': 'ISC301', 'creditos': 8},
            {'nombre': 'Redes de Computadoras', 'codigo': 'ISC302', 'creditos': 6},
            {'nombre': 'Desarrollo Web', 'codigo': 'ISC303', 'creditos': 8},
        ],
        'Ingeniería Industrial': [
            {'nombre': 'Fundamentos de Ingeniería', 'codigo': 'II101', 'creditos': 6},
            {'nombre': 'Matemáticas I', 'codigo': 'II102', 'creditos': 6},
            {'nombre': 'Física I', 'codigo': 'II103', 'creditos': 6},
            {'nombre': 'Estadística', 'codigo': 'II201', 'creditos': 6},
            {'nombre': 'Investigación de Operaciones', 'codigo': 'II202', 'creditos': 8},
            {'nombre': 'Control de Calidad', 'codigo': 'II203', 'creditos': 6},
            {'nombre': 'Gestión de Producción', 'codigo': 'II301', 'creditos': 8},
            {'nombre': 'Logística', 'codigo': 'II302', 'creditos': 6},
        ],
        'Administración de Empresas': [
            {'nombre': 'Fundamentos de Administración', 'codigo': 'AE101', 'creditos': 6},
            {'nombre': 'Matemáticas para Administradores', 'codigo': 'AE102', 'creditos': 6},
            {'nombre': 'Contabilidad Básica', 'codigo': 'AE103', 'creditos': 6},
            {'nombre': 'Microeconomía', 'codigo': 'AE201', 'creditos': 6},
            {'nombre': 'Macroeconomía', 'codigo': 'AE202', 'creditos': 6},
            {'nombre': 'Finanzas Corporativas', 'codigo': 'AE203', 'creditos': 8},
            {'nombre': 'Marketing', 'codigo': 'AE301', 'creditos': 8},
            {'nombre': 'Gestión de Recursos Humanos', 'codigo': 'AE302', 'creditos': 6},
        ],
        'Contaduría Pública': [
            {'nombre': 'Contabilidad Básica', 'codigo': 'CP101', 'creditos': 6},
            {'nombre': 'Matemáticas Financieras', 'codigo': 'CP102', 'creditos': 6},
            {'nombre': 'Derecho Mercantil', 'codigo': 'CP103', 'creditos': 6},
            {'nombre': 'Contabilidad Intermedia', 'codigo': 'CP201', 'creditos': 8},
            {'nombre': 'Costos', 'codigo': 'CP202', 'creditos': 8},
            {'nombre': 'Auditoría', 'codigo': 'CP203', 'creditos': 8},
            {'nombre': 'Contabilidad Avanzada', 'codigo': 'CP301', 'creditos': 8},
            {'nombre': 'Fiscal', 'codigo': 'CP302', 'creditos': 8},
        ]
    }
    
    materias_creadas = []
    
    for carrera in carreras:
        if carrera.nombre in materias_por_carrera:
            for materia_data in materias_por_carrera[carrera.nombre]:
                materia, created = Materia.objects.get_or_create(
                    codigo=materia_data['codigo'],
                    defaults={
                        'nombre': materia_data['nombre'],
                        'creditos': materia_data['creditos']
                    }
                )
                if created:
                    print(f"Materia creada: {materia.nombre}")
                materia.carrera.add(carrera)
                materias_creadas.append(materia)
    
    return materias_creadas


def crear_planes_estudio(admin_user, carreras, centros, ciclos):
    """Crear planes de estudios de muestra."""
    planes = []
    
    planes_data = [
        {
            'nombre': 'Plan 2024 - Ingeniería en Sistemas',
            'carrera': carreras[0],  # ISC
            'work_center': centros[0],
            'ciclo_inicio': ciclos[0],
            'duracion_semestres': 8,
            'creditos_totales': 240,
            'estado': 'ACTIVO'
        },
        {
            'nombre': 'Plan 2024 - Ingeniería Industrial',
            'carrera': carreras[1],  # II
            'work_center': centros[1],
            'ciclo_inicio': ciclos[1],
            'duracion_semestres': 8,
            'creditos_totales': 220,
            'estado': 'ACTIVO'
        },
        {
            'nombre': 'Plan 2024 - Administración',
            'carrera': carreras[2],  # AE
            'work_center': centros[2],
            'ciclo_inicio': ciclos[2],
            'duracion_semestres': 8,
            'creditos_totales': 200,
            'estado': 'BORRADOR'
        }
    ]
    
    for data in planes_data:
        plan, created = PlanEstudio.objects.get_or_create(
            nombre=data['nombre'],
            carrera=data['carrera'],
            work_center=data['work_center'],
            defaults={
                'descripcion': f'Plan de estudios actualizado para {data["carrera"].nombre}',
                'ciclo_inicio': data['ciclo_inicio'],
                'duracion_semestres': data['duracion_semestres'],
                'creditos_totales': data['creditos_totales'],
                'estado': data['estado'],
                'creado_por': admin_user
            }
        )
        if created:
            print(f"Plan de estudios creado: {plan.nombre}")
        planes.append(plan)
    
    return planes


def crear_semestres_plan(planes):
    """Crear semestres para cada plan de estudios."""
    semestres_creados = []
    
    for plan in planes:
        for i in range(1, plan.duracion_semestres + 1):
            semestre, created = SemestrePlan.objects.get_or_create(
                plan_estudio=plan,
                numero_semestre=i,
                defaults={
                    'nombre': f'Semestre {i}',
                    'es_optativo': False,
                    'descripcion': f'Semestre {i} del plan {plan.nombre}'
                }
            )
            if created:
                print(f"Semestre creado: {semestre.nombre} para {plan.nombre}")
            semestres_creados.append(semestre)
    
    return semestres_creados


def crear_materias_plan(semestres, materias):
    """Asignar materias a los semestres de los planes."""
    # Mapeo de materias por carrera y semestre
    asignaciones = {
        'Ingeniería en Sistemas Computacionales': {
            1: ['ISC101', 'ISC102', 'ISC103'],
            2: ['ISC201', 'ISC202', 'ISC203'],
            3: ['ISC301', 'ISC302', 'ISC303'],
        },
        'Ingeniería Industrial': {
            1: ['II101', 'II102', 'II103'],
            2: ['II201', 'II202', 'II203'],
            3: ['II301', 'II302'],
        },
        'Administración de Empresas': {
            1: ['AE101', 'AE102', 'AE103'],
            2: ['AE201', 'AE202', 'AE203'],
            3: ['AE301', 'AE302'],
        }
    }
    
    materias_plan_creadas = []
    
    for semestre in semestres:
        plan = semestre.plan_estudio
        carrera = plan.carrera.nombre
        num_semestre = semestre.numero_semestre
        
        if carrera in asignaciones and num_semestre in asignaciones[carrera]:
            codigos_materias = asignaciones[carrera][num_semestre]
            
            for i, codigo in enumerate(codigos_materias, 1):
                try:
                    materia = Materia.objects.get(codigo=codigo)
                    materia_plan, created = MateriaPlan.objects.get_or_create(
                        semestre=semestre,
                        materia=materia,
                        defaults={
                            'tipo_materia': 'OBLIGATORIA',
                            'creditos': materia.creditos,
                            'horas_teoria': materia.creditos * 2,
                            'horas_practica': materia.creditos,
                            'horas_independiente': materia.creditos,
                            'orden': i
                        }
                    )
                    if created:
                        print(f"Materia asignada: {materia.nombre} al {semestre.nombre}")
                    materias_plan_creadas.append(materia_plan)
                except Materia.DoesNotExist:
                    print(f"Materia no encontrada: {codigo}")
    
    return materias_plan_creadas


def crear_competencias():
    """Crear competencias de muestra."""
    competencias = []
    
    competencias_data = [
        {
            'nombre': 'Análisis y Resolución de Problemas',
            'descripcion': 'Capacidad para analizar situaciones complejas y proponer soluciones efectivas.',
            'tipo_competencia': 'GENERICA'
        },
        {
            'nombre': 'Trabajo en Equipo',
            'descripcion': 'Habilidad para colaborar efectivamente en grupos de trabajo.',
            'tipo_competencia': 'GENERICA'
        },
        {
            'nombre': 'Comunicación Efectiva',
            'descripcion': 'Capacidad para transmitir ideas de manera clara y persuasiva.',
            'tipo_competencia': 'GENERICA'
        },
        {
            'nombre': 'Desarrollo de Software',
            'descripcion': 'Capacidad para diseñar, desarrollar e implementar aplicaciones de software.',
            'tipo_competencia': 'ESPECIFICA'
        },
        {
            'nombre': 'Gestión de Proyectos',
            'descripcion': 'Habilidad para planificar, ejecutar y controlar proyectos de ingeniería.',
            'tipo_competencia': 'ESPECIFICA'
        },
        {
            'nombre': 'Análisis Financiero',
            'descripcion': 'Capacidad para analizar información financiera y tomar decisiones estratégicas.',
            'tipo_competencia': 'ESPECIFICA'
        }
    ]
    
    for data in competencias_data:
        competencia, created = Competencia.objects.get_or_create(
            nombre=data['nombre'],
            defaults=data
        )
        if created:
            print(f"Competencia creada: {competencia.nombre}")
        competencias.append(competencia)
    
    return competencias


def crear_objetivos_educativos(planes):
    """Crear objetivos educativos para cada plan."""
    objetivos_creados = []
    
    objetivos_por_carrera = {
        'Ingeniería en Sistemas Computacionales': [
            'Formar profesionales capaces de diseñar y desarrollar soluciones tecnológicas innovadoras.',
            'Desarrollar habilidades para la gestión de proyectos de software.',
            'Fomentar el pensamiento crítico y la resolución de problemas complejos.'
        ],
        'Ingeniería Industrial': [
            'Formar profesionales para optimizar procesos productivos y de gestión.',
            'Desarrollar habilidades para la mejora continua y la calidad.',
            'Fomentar la innovación en procesos industriales.'
        ],
        'Administración de Empresas': [
            'Formar profesionales para la gestión estratégica de organizaciones.',
            'Desarrollar habilidades para el análisis financiero y económico.',
            'Fomentar el liderazgo y la toma de decisiones efectivas.'
        ]
    }
    
    for plan in planes:
        carrera = plan.carrera.nombre
        if carrera in objetivos_por_carrera:
            for i, objetivo_texto in enumerate(objetivos_por_carrera[carrera], 1):
                objetivo, created = ObjetivoEducativo.objects.get_or_create(
                    plan_estudio=plan,
                    titulo=f'Objetivo {i}',
                    defaults={
                        'descripcion': objetivo_texto,
                        'orden': i
                    }
                )
                if created:
                    print(f"Objetivo educativo creado: {objetivo.titulo} para {plan.nombre}")
                objetivos_creados.append(objetivo)
    
    return objetivos_creados


def crear_perfiles_egreso(planes):
    """Crear perfiles de egreso para cada plan."""
    perfiles_creados = []
    
    perfiles_data = {
        'Ingeniería en Sistemas Computacionales': {
            'descripcion_general': 'El egresado será capaz de diseñar, desarrollar e implementar soluciones tecnológicas innovadoras.',
            'competencias_generales': 'Análisis crítico, trabajo en equipo, comunicación efectiva, aprendizaje continuo.',
            'competencias_especificas': 'Desarrollo de software, gestión de bases de datos, redes de computadoras.',
            'campo_laboral': 'Empresas de desarrollo de software, consultoría tecnológica, departamentos de TI.'
        },
        'Ingeniería Industrial': {
            'descripcion_general': 'El egresado será capaz de optimizar procesos productivos y de gestión empresarial.',
            'competencias_generales': 'Análisis de sistemas, mejora continua, gestión de calidad, liderazgo.',
            'competencias_especificas': 'Gestión de producción, logística, control de calidad, investigación de operaciones.',
            'campo_laboral': 'Industria manufacturera, consultoría empresarial, empresas de servicios.'
        },
        'Administración de Empresas': {
            'descripcion_general': 'El egresado será capaz de gestionar estratégicamente organizaciones de diversos sectores.',
            'competencias_generales': 'Pensamiento estratégico, liderazgo, comunicación, toma de decisiones.',
            'competencias_especificas': 'Gestión financiera, marketing, recursos humanos, administración estratégica.',
            'campo_laboral': 'Empresas privadas, organizaciones públicas, consultoría empresarial.'
        }
    }
    
    for plan in planes:
        carrera = plan.carrera.nombre
        if carrera in perfiles_data:
            perfil, created = PerfilEgreso.objects.get_or_create(
                plan_estudio=plan,
                defaults=perfiles_data[carrera]
            )
            if created:
                print(f"Perfil de egreso creado para: {plan.nombre}")
            perfiles_creados.append(perfil)
    
    return perfiles_creados


def main():
    """Función principal para crear todos los datos de muestra."""
    print("=== Creando datos de muestra para Planes de Estudios ===\n")
    
    # Crear usuarios
    admin_user = crear_usuarios_muestra()
    
    # Crear centros de trabajo
    centros = crear_centros_trabajo()
    
    # Crear ciclos escolares
    ciclos = crear_ciclos_escolares(centros)
    
    # Crear carreras
    carreras = crear_carreras_muestra()
    
    # Crear materias
    materias = crear_materias_muestra(carreras)
    
    # Crear planes de estudios
    planes = crear_planes_estudio(admin_user, carreras, centros, ciclos)
    
    # Crear semestres
    semestres = crear_semestres_plan(planes)
    
    # Crear materias en planes
    materias_plan = crear_materias_plan(semestres, materias)
    
    # Crear competencias
    competencias = crear_competencias()
    
    # Crear objetivos educativos
    objetivos = crear_objetivos_educativos(planes)
    
    # Crear perfiles de egreso
    perfiles = crear_perfiles_egreso(planes)
    
    print("\n=== Datos de muestra creados exitosamente ===")
    print(f"✓ {len(centros)} centros de trabajo")
    print(f"✓ {len(ciclos)} ciclos escolares")
    print(f"✓ {len(carreras)} carreras")
    print(f"✓ {len(materias)} materias")
    print(f"✓ {len(planes)} planes de estudios")
    print(f"✓ {len(semestres)} semestres")
    print(f"✓ {len(materias_plan)} materias en planes")
    print(f"✓ {len(competencias)} competencias")
    print(f"✓ {len(objetivos)} objetivos educativos")
    print(f"✓ {len(perfiles)} perfiles de egreso")


if __name__ == '__main__':
    main() 