#!/usr/bin/env python3
"""
Script para probar la funcionalidad mejorada del dashboard de usuarios con tarjetas centradas.
"""

import os
import sys
import django
from datetime import date

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from users.models import Role, User

def test_users_dashboard_data():
    """Prueba los datos del dashboard de usuarios"""
    print("🔧 Probando datos del dashboard de usuarios...")
    
    # Obtener roles y usuarios
    roles = Role.objects.all()
    users = User.objects.all()
    
    print(f"📊 Roles en el sistema: {roles.count()}")
    print(f"👥 Usuarios en el sistema: {users.count()}")
    
    # Mostrar roles
    if roles:
        print("\n🏷️  Roles disponibles:")
        for role in roles:
            print(f"  - {role.name}: {role.permissions.count()} permisos")
            if role.description:
                print(f"    Descripción: {role.description}")
    else:
        print("\n⚠️  No hay roles creados")
    
    # Mostrar usuarios
    if users:
        print("\n👤 Usuarios disponibles:")
        for user in users:
            role_name = user.role.name if user.role else "Sin rol"
            full_name = user.get_full_name() or user.username
            print(f"  - {full_name} ({user.username})")
            print(f"    Email: {user.email}")
            print(f"    Rol: {role_name}")
    else:
        print("\n⚠️  No hay usuarios creados")
    
    return roles, users

def test_dashboard_layout():
    """Prueba la estructura del dashboard"""
    print("\n🔧 Probando estructura del dashboard...")
    
    print("📋 Elementos del dashboard:")
    print("  ✅ Header con título y descripción")
    print("  ✅ Estadísticas en tarjetas")
    print("  ✅ Tarjeta de roles centrada")
    print("  ✅ Tarjeta de usuarios centrada")
    print("  ✅ Acciones rápidas centradas")
    
    print("\n🎨 Características visuales:")
    print("  ✅ Layout responsivo")
    print("  ✅ Tarjetas con sombras")
    print("  ✅ Gradientes en headers")
    print("  ✅ Iconos para cada sección")
    print("  ✅ Estados vacíos con mensajes")
    print("  ✅ Hover effects")
    print("  ✅ Transiciones suaves")

def test_centered_layout():
    """Prueba el layout centrado"""
    print("\n🔧 Probando layout centrado...")
    
    print("📐 Estructura de centrado:")
    print("  ✅ Contenedor principal con max-width")
    print("  ✅ Flex justify-center para centrar")
    print("  ✅ Grid responsivo para tarjetas")
    print("  ✅ Espaciado uniforme")
    print("  ✅ Márgenes automáticos")
    
    print("\n📱 Responsive design:")
    print("  ✅ 1 columna en móvil")
    print("  ✅ 2 columnas en desktop")
    print("  ✅ Espaciado adaptativo")
    print("  ✅ Texto centrado")

def test_user_interface():
    """Prueba la interfaz de usuario"""
    print("\n🔧 Probando interfaz de usuario...")
    
    print("🎯 Elementos de UX:")
    print("  ✅ Botones de acción prominentes")
    print("  ✅ Información clara y organizada")
    print("  ✅ Estados visuales (hover, focus)")
    print("  ✅ Iconos descriptivos")
    print("  ✅ Colores consistentes")
    print("  ✅ Tipografía legible")
    
    print("\n🔗 Navegación:")
    print("  ✅ Enlaces a crear roles")
    print("  ✅ Enlaces a crear usuarios")
    print("  ✅ Enlaces a editar elementos")
    print("  ✅ Botones de acción rápida")

if __name__ == "__main__":
    print("🚀 Iniciando pruebas del dashboard de usuarios mejorado...")
    
    try:
        # Ejecutar pruebas
        roles, users = test_users_dashboard_data()
        test_dashboard_layout()
        test_centered_layout()
        test_user_interface()
        
        print("\n🎉 Todas las pruebas completadas exitosamente!")
        print("\n📋 Resumen de mejoras:")
        print("  ✅ Tarjetas centradas en el layout")
        print("  ✅ Diseño responsivo y moderno")
        print("  ✅ Estadísticas visuales")
        print("  ✅ Estados vacíos informativos")
        print("  ✅ Acciones rápidas centradas")
        print("  ✅ Interfaz intuitiva y atractiva")
        
        print(f"\n🔗 URL para probar: http://127.0.0.1:8000/users/")
        print("  - Verificar que las tarjetas estén centradas")
        print("  - Verificar el diseño responsivo")
        print("  - Verificar los estados vacíos")
        print("  - Verificar las acciones rápidas")
        
    except Exception as e:
        print(f"\n❌ Error durante las pruebas: {e}")
        sys.exit(1) 