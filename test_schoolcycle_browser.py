#!/usr/bin/env python3
"""
Script para abrir el navegador y probar la funcionalidad de ciclos escolares.
"""

import webbrowser
import time
import subprocess
import sys
import os

def test_schoolcycle_browser():
    """Abre el navegador para probar la funcionalidad de ciclos escolares."""
    
    print("=== Probando Funcionalidad de Ciclos Escolares en el Navegador ===\n")
    
    # URLs a probar
    urls = [
        "http://127.0.0.1:8000/workcenter/",
        "http://127.0.0.1:8000/workcenter/schoolcycles/",
        "http://127.0.0.1:8000/workcenter/schoolcycles/new/",
    ]
    
    print("🌐 Abriendo navegador para probar:")
    print(f"  1. Dashboard: {urls[0]}")
    print(f"  2. Lista de ciclos: {urls[1]}")
    print(f"  3. Crear ciclo: {urls[2]}")
    
    # Abrir cada URL
    for i, url in enumerate(urls, 1):
        print(f"\n📱 Abriendo {i}/3: {url}")
        webbrowser.open(url)
        time.sleep(2)  # Pausa entre aperturas
    
    print(f"\n✅ Navegador abierto con las páginas de ciclos escolares")
    print(f"   Prueba las siguientes funcionalidades:")
    print(f"   • En el dashboard, haz clic en 'Ver todos los ciclos'")
    print(f"   • En la lista, verifica las estadísticas")
    print(f"   • Prueba los botones de editar y ver centro")
    print(f"   • Verifica los estados de los ciclos")
    print(f"   • Prueba la navegación entre secciones")

if __name__ == '__main__':
    test_schoolcycle_browser() 