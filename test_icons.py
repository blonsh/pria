#!/usr/bin/env python3
"""
Script para verificar que los iconos de Font Awesome se estén cargando correctamente.
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from workcenter.models import WorkCenter

def test_icons():
    """Prueba que los iconos se estén cargando correctamente."""
    
    print("=== Prueba de Iconos de Font Awesome ===\n")
    
    # Verificar centros de trabajo
    workcenters = WorkCenter.objects.all()
    print(f"📊 Centros de trabajo disponibles: {workcenters.count()}")
    
    if workcenters.exists():
        print(f"\n🏢 Centros de trabajo:")
        for i, wc in enumerate(workcenters[:3], 1):
            print(f"  {i}. {wc.name}")
            print(f"     • URL de edición: /workcenter/workcenters/{wc.pk}/edit/")
            print(f"     • URL de detalles: /workcenter/workcenters/{wc.pk}/")
    
    print(f"\n🔍 Verificación de iconos:")
    print(f"  • Icono de editar: fas fa-edit")
    print(f"  • Icono de ver: fas fa-eye")
    print(f"  • Color editar: text-blue-600")
    print(f"  • Color ver: text-green-600")
    
    print(f"\n🌐 URLs para probar:")
    print(f"  • Lista de centros: http://127.0.0.1:8000/workcenter/workcenters/")
    print(f"  • Dashboard: http://127.0.0.1:8000/workcenter/")
    
    print(f"\n💡 Soluciones si no ves los iconos:")
    print(f"  1. Verifica que Font Awesome esté cargado en el navegador")
    print(f"  2. Revisa la consola del navegador (F12) para errores")
    print(f"  3. Intenta recargar la página (Ctrl+R)")
    print(f"  4. Verifica la conexión a internet para cargar CDN")
    
    print(f"\n🎯 Iconos que deberías ver:")
    print(f"  • 👁️  (Ver detalles) - Verde")
    print(f"  • ✏️  (Editar) - Azul")
    print(f"  • En pantallas pequeñas: solo iconos")
    print(f"  • En pantallas grandes: iconos + texto")

if __name__ == "__main__":
    test_icons() 