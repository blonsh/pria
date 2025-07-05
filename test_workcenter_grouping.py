#!/usr/bin/env python3
"""
Script de prueba para verificar el agrupamiento del módulo workcenter
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

def test_workcenter_grouping():
    """Prueba el agrupamiento del módulo workcenter"""
    print("🎯 Probando agrupamiento del módulo Centro de Trabajo...")
    
    # Obtener permisos agrupados
    permissions_by_module = get_permissions_by_module()
    
    # Buscar el módulo workcenter agrupado
    workcenter_found = False
    
    for module_key, module_data in permissions_by_module.items():
        if module_key == 'workcenter_combined':
            workcenter_found = True
            print(f"✅ Módulo encontrado: {module_data['module_name']}")
            print(f"📋 Modelos incluidos: {module_data['model_name']}")
            print(f"🔢 Número de permisos: {len(module_data['permissions'])}")
            
            # Mostrar los permisos incluidos
            print("📝 Permisos incluidos:")
            for permission in module_data['permissions']:
                print(f"   - {permission.content_type.app_label}.{permission.content_type.model}: {permission.name}")
            
            break
    
    if not workcenter_found:
        print("❌ No se encontró el módulo workcenter agrupado")
        print("📊 Módulos disponibles:")
        for module_key, module_data in permissions_by_module.items():
            print(f"   - {module_key}: {module_data['module_name']}")
    
    # Verificar que no hay módulos workcenter separados
    separate_workcenter_modules = []
    for module_key, module_data in permissions_by_module.items():
        if module_data['app_label'] == 'workcenter' and module_key != 'workcenter_combined':
            separate_workcenter_modules.append(module_key)
    
    if separate_workcenter_modules:
        print(f"⚠️  Se encontraron módulos workcenter separados: {separate_workcenter_modules}")
    else:
        print("✅ No hay módulos workcenter separados (correcto)")
    
    print("\n🎉 Prueba completada!")

if __name__ == '__main__':
    test_workcenter_grouping() 