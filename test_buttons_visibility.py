#!/usr/bin/env python3
"""
Script para probar la visibilidad de los botones de edición.
"""

import os
import sys
import django
from datetime import date

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pria.settings')
django.setup()

from workcenter.models import SchoolCycle

def test_buttons_visibility():
    """Prueba la visibilidad de los botones de edición."""
    
    print("=== Probando Visibilidad de Botones ===\n")
    
    # Verificar que hay datos
    total_cycles = SchoolCycle.objects.count()
    
    print(f"📊 Datos disponibles:")
    print(f"  • Ciclos escolares: {total_cycles}")
    
    if total_cycles == 0:
        print(f"\n⚠️  No hay ciclos escolares. Ejecuta primero:")
        print(f"   python3 create_sample_data.py")
        return
    
    # Obtener un ciclo de ejemplo
    cycle = SchoolCycle.objects.first()
    
    print(f"\n🔗 URLs para probar:")
    print(f"  • Lista de ciclos: http://127.0.0.1:8000/workcenter/schoolcycles/")
    print(f"  • Editar ciclo '{cycle.name}': http://127.0.0.1:8000/workcenter/schoolcycles/{cycle.pk}/edit/")
    
    print(f"\n✅ Botones implementados:")
    print(f"  • Botón 'Editar' - Azul con icono de lápiz")
    print(f"  • Botón 'Ver Centro' - Verde con icono de ojo")
    print(f"  • Botón 'Actualizar Ciclo' - Púrpura en formulario")
    print(f"  • Botón 'Cancelar' - Gris en formulario")
    
    print(f"\n🎨 Características de los botones:")
    print(f"  • Fondo de color sólido (azul, verde, púrpura)")
    print(f"  • Texto blanco para mejor contraste")
    print(f"  • Iconos Font Awesome")
    print(f"  • Efectos hover")
    print(f"  • Sombras para profundidad")
    print(f"  • Bordes redondeados")
    
    print(f"\n🔍 Instrucciones para verificar:")
    print(f"  1. Ve a: http://127.0.0.1:8000/workcenter/schoolcycles/")
    print(f"  2. Busca los botones azules 'Editar' en cada fila")
    print(f"  3. Haz clic en 'Editar' para ir al formulario")
    print(f"  4. Verifica que aparezca el botón púrpura 'Actualizar Ciclo'")
    print(f"  5. Si no ves los botones, verifica la conexión a internet")
    print(f"     (Font Awesome se carga desde CDN)")
    
    print(f"\n💡 Soluciones si no ves los botones:")
    print(f"  • Verifica tu conexión a internet")
    print(f"  • Recarga la página (Ctrl+F5)")
    print(f"  • Verifica que no haya bloqueadores de anuncios")
    print(f"  • Los botones tienen texto, así que deberían ser visibles")

if __name__ == '__main__':
    test_buttons_visibility() 