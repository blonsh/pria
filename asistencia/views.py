from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.core.files.storage import default_storage
from django.conf import settings
import csv
import io
from datetime import datetime, timedelta
from .models import Asistencia
from .forms import AsistenciaForm, BuscarAsistenciaForm

@login_required
@permission_required('asistencia.add_asistencia', raise_exception=True)
def registrar_asistencia(request):
    """Vista para registrar asistencia"""
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            asistencia = form.save(commit=False)
            asistencia.save()
            messages.success(request, 'Asistencia registrada exitosamente')
            return redirect('asistencia:historial_asistencia')
    else:
        form = AsistenciaForm()
    
    return render(request, 'asistencia/registrar.html', {
        'form': form,
        'title': 'Registrar Asistencia'
    })

@login_required
def historial_asistencia(request):
    """Vista para ver el historial de asistencia"""
    form = BuscarAsistenciaForm(request.GET)
    asistencias = Asistencia.objects.all().order_by('-fecha', 'alumno__user__last_name')
    
    if form.is_valid():
        fecha_inicio = form.cleaned_data.get('fecha_inicio')
        fecha_fin = form.cleaned_data.get('fecha_fin')
        alumno = form.cleaned_data.get('alumno')
        
        if fecha_inicio:
            asistencias = asistencias.filter(fecha__gte=fecha_inicio)
        if fecha_fin:
            asistencias = asistencias.filter(fecha__lte=fecha_fin)
        if alumno:
            asistencias = asistencias.filter(alumno=alumno)
    
    paginator = Paginator(asistencias, 20)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'asistencia/historial.html', {
        'form': form,
        'page_obj': page_obj,
        'title': 'Historial de Asistencia'
    })

@login_required
def reporte_asistencia(request):
    """Vista para generar reportes de asistencia"""
    if request.method == 'POST':
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        
        if not fecha_inicio or not fecha_fin:
            messages.error(request, 'Por favor seleccione fechas válidas')
            return redirect('asistencia:reporte_asistencia')
        
        # Generar reporte en CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="reporte_asistencia.csv"'
        writer = csv.writer(response)
        
        # Encabezados
        writer.writerow([
            'Fecha',
            'Alumno',
            'Estado',
            'Hora de Entrada',
            'Hora de Salida',
            'Docente'
        ])
        
        # Datos
        asistencias = Asistencia.objects.filter(
            fecha__range=[fecha_inicio, fecha_fin]
        ).order_by('fecha', 'alumno__user__last_name')
        
        for asistencia in asistencias:
            writer.writerow([
                asistencia.fecha.strftime('%Y-%m-%d'),
                asistencia.alumno.user.get_full_name(),
                asistencia.get_estado_display(),
                asistencia.hora_entrada.strftime('%H:%M') if asistencia.hora_entrada else '',
                asistencia.hora_salida.strftime('%H:%M') if asistencia.hora_salida else '',
                asistencia.docente.user.get_full_name() if asistencia.docente else '',
            ])
        
        return response
    
    return render(request, 'asistencia/reporte.html', {
        'title': 'Reporte de Asistencia'
    })

@require_POST
@login_required
@permission_required('asistencia.change_asistencia', raise_exception=True)
def actualizar_estado(request, pk):
    """Actualizar el estado de una asistencia"""
    asistencia = get_object_or_404(Asistencia, pk=pk)
    nuevo_estado = request.POST.get('estado')
    
    if nuevo_estado in dict(Asistencia.ESTADOS):
        asistencia.estado = nuevo_estado
        asistencia.save()
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False, 'error': 'Estado inválido'}, status=400)

@login_required
@permission_required('asistencia.view_asistencia', raise_exception=True)
def estadisticas_asistencia(request):
    """Vista para mostrar estadísticas de asistencia"""
    hoy = timezone.now().date()
    semana = hoy - timedelta(days=7)
    
    # Estadísticas de la semana
    asistencias_semana = Asistencia.objects.filter(
        fecha__gte=semana,
        fecha__lte=hoy
    ).values('estado').annotate(total=Count('id'))
    
    # Porcentaje de asistencia
    total = sum(item['total'] for item in asistencias_semana)
    porcentajes = {
        estado: (count / total * 100 if total > 0 else 0)
        for estado, count in asistencias_semana
    }
    
    return render(request, 'asistencia/estadisticas.html', {
        'estadisticas': asistencias_semana,
        'porcentajes': porcentajes,
        'title': 'Estadísticas de Asistencia'
    })
