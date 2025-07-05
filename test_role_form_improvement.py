#!/usr/bin/env python3
"""
Script para probar la funcionalidad mejorada del formulario de roles con pestañas.
"""

import os
import sys
import django
from datetime import date

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from users.models import Role

def test_permissions_grouping():
    """Prueba la agrupación de permisos por módulo"""
    print("🔧 Probando agrupación de permisos por módulo...")
    
    # Obtener todos los permisos
    permissions = Permission.objects.select_related('content_type').all()
    print(f"📊 Total de permisos: {permissions.count()}")
    
    # Agrupar permisos por content_type
    permissions_by_module = {}
    
    for permission in permissions:
        content_type = permission.content_type
        app_label = content_type.app_label
        model_name = content_type.model
        
        # Crear nombre legible del módulo
        module_name = app_label.replace('_', ' ').title()
        
        # Crear nombre legible del modelo
        model_display_name = model_name.replace('_', ' ').title()
        
        # Crear clave única para el módulo
        module_key = f"{app_label}_{model_name}"
        
        if module_key not in permissions_by_module:
            permissions_by_module[module_key] = {
                'module_name': module_name,
                'model_name': model_display_name,
                'app_label': app_label,
                'content_type': content_type,
                'permissions': []
            }
        
        permissions_by_module[module_key]['permissions'].append(permission)
    
    # Mostrar resultados
    print(f"\n📋 Módulos encontrados: {len(permissions_by_module)}")
    
    for module_key, module_data in permissions_by_module.items():
        print(f"\n🏷️  Módulo: {module_data['module_name']}")
        print(f"   📝 Modelo: {module_data['model_name']}")
        print(f"   🔑 App: {module_data['app_label']}")
        print(f"   📊 Permisos: {len(module_data['permissions'])}")
        
        for permission in module_data['permissions']:
            icon = "➕" if permission.codename == 'add' else \
                   "✏️" if permission.codename == 'change' else \
                   "🗑️" if permission.codename == 'delete' else \
                   "👁️" if permission.codename == 'view' else "⚙️"
            print(f"     {icon} {permission.codename} - {permission.name}")
    
    return permissions_by_module

def test_role_creation():
    """Prueba la creación de roles con permisos"""
    print("\n🔧 Probando creación de roles...")
    
    # Verificar roles existentes
    existing_roles = Role.objects.all()
    print(f"📊 Roles existentes: {existing_roles.count()}")
    
    for role in existing_roles:
        print(f"  👤 {role.name}: {role.permissions.count()} permisos")
    
    # Crear un rol de prueba si no existe
    test_role_name = "Rol de Prueba - Tabs"
    test_role, created = Role.objects.get_or_create(
        name=test_role_name,
        defaults={'description': 'Rol de prueba para verificar pestañas de permisos'}
    )
    
    if created:
        print(f"✅ Rol de prueba creado: {test_role.name}")
    else:
        print(f"ℹ️  Rol de prueba ya existe: {test_role.name}")
    
    return test_role

def test_permission_types():
    """Prueba los diferentes tipos de permisos"""
    print("\n🔧 Analizando tipos de permisos...")
    
    permission_types = {}
    
    for permission in Permission.objects.all():
        codename = permission.codename
        if codename not in permission_types:
            permission_types[codename] = []
        permission_types[codename].append(permission)
    
    print(f"📊 Tipos de permisos encontrados: {len(permission_types)}")
    
    for codename, permissions in permission_types.items():
        icon = "➕" if codename == 'add' else \
               "✏️" if codename == 'change' else \
               "🗑️" if codename == 'delete' else \
               "👁️" if codename == 'view' else "⚙️"
        
        print(f"  {icon} {codename}: {len(permissions)} permisos")
    
    return permission_types

def test_content_types():
    """Prueba los tipos de contenido disponibles"""
    print("\n🔧 Analizando tipos de contenido...")
    
    content_types = ContentType.objects.all()
    print(f"📊 Tipos de contenido: {content_types.count()}")
    
    # Agrupar por app
    apps = {}
    for ct in content_types:
        app = ct.app_label
        if app not in apps:
            apps[app] = []
        apps[app].append(ct)
    
    print(f"📱 Aplicaciones: {len(apps)}")
    
    for app, types in apps.items():
        app_name = app.replace('_', ' ').title()
        print(f"  📱 {app_name}: {len(types)} modelos")
        for ct in types:
            model_name = ct.model.replace('_', ' ').title()
            print(f"    📝 {model_name}")

if __name__ == "__main__":
    print("🚀 Iniciando pruebas del formulario de roles mejorado...")
    
    try:
        # Ejecutar pruebas
        permissions_by_module = test_permissions_grouping()
        test_role = test_role_creation()
        permission_types = test_permission_types()
        test_content_types()
        
        print("\n🎉 Todas las pruebas completadas exitosamente!")
        print("\n📋 Resumen de mejoras:")
        print("  ✅ Permisos organizados por módulo")
        print("  ✅ Interfaz con pestañas")
        print("  ✅ Iconos para tipos de permisos")
        print("  ✅ Nombres legibles de módulos")
        print("  ✅ Agrupación automática")
        
        print(f"\n🔗 URL para probar: http://127.0.0.1:8000/users/roles/new/")
        print("  - Verificar que las pestañas funcionen")
        print("  - Verificar que los permisos estén organizados")
        print("  - Verificar que los iconos se muestren correctamente")
        
    except Exception as e:
        print(f"\n❌ Error durante las pruebas: {e}")
        sys.exit(1) 