#!/usr/bin/env python3
"""
Script de prueba para verificar el agrupamiento del módulo users
en el formulario de roles.
"""

import os
import sys
import django
from django.conf import settings

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from users.views import get_permissions_by_module

def test_users_grouping():
    """Prueba el agrupamiento del módulo users"""
    print("🎯 Probando agrupamiento del módulo Usuarios...")
    
    # Obtener permisos agrupados
    permissions_by_module = get_permissions_by_module()
    
    # Buscar el módulo users agrupado
    users_found = False
    
    for module_key, module_data in permissions_by_module.items():
        if module_key == 'users_combined':
            users_found = True
            print(f"✅ Módulo encontrado: {module_data['module_name']}")
            print(f"📋 Modelos incluidos: {module_data['model_name']}")
            print(f"🔢 Número de permisos: {len(module_data['permissions'])}")
            
            # Mostrar los permisos incluidos
            print("📝 Permisos incluidos:")
            for permission in module_data['permissions']:
                print(f"   - {permission.content_type.app_label}.{permission.content_type.model}: {permission.name}")
            
            break
    
    if not users_found:
        print("❌ No se encontró el módulo users agrupado")
        print("📊 Módulos disponibles:")
        for module_key, module_data in permissions_by_module.items():
            print(f"   - {module_key}: {module_data['module_name']}")
    
    # Verificar que no hay módulos users separados
    separate_users_modules = []
    for module_key, module_data in permissions_by_module.items():
        if module_data['app_label'] == 'users' and module_key != 'users_combined':
            separate_users_modules.append(module_key)
    
    if separate_users_modules:
        print(f"⚠️  Se encontraron módulos users separados: {separate_users_modules}")
    else:
        print("✅ No hay módulos users separados (correcto)")
    
    # Mostrar todos los módulos agrupados
    print("\n📊 Módulos agrupados actuales:")
    for module_key, module_data in permissions_by_module.items():
        if '_combined' in module_key:
            print(f"  - {module_data['module_name']}: {module_data['model_name']}")
    
    print("\n🎉 Prueba completada!")

if __name__ == '__main__':
    test_users_grouping() 