from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
    PlanEstudio, SemestrePlan, MateriaPlan, Competencia,
    ObjetivoEducativo, PerfilEgreso, VersionPlanEstudio
)
from .forms import (
    PlanEstudioForm, SemestrePlanForm, MateriaPlanForm, CompetenciaForm,
    ObjetivoEducativoForm, PerfilEgresoForm, VersionPlanEstudioForm
)
from django.utils.decorators import method_decorator


@login_required
def dashboard_planes_estudio(request):
    """
    Dashboard principal del módulo de planes de estudios.
    """
    # Estadísticas generales
    total_planes = PlanEstudio.objects.count()
    planes_activos = PlanEstudio.objects.filter(estado='ACTIVO').count()
    planes_borrador = PlanEstudio.objects.filter(estado='BORRADOR').count()
    
    # Planes recientes
    planes_recientes = PlanEstudio.objects.select_related('carrera', 'work_center').order_by('-fecha_creacion')[:5]
    
    # Planes por estado
    planes_por_estado = PlanEstudio.objects.values('estado').annotate(
        count=Count('id')
    ).order_by('estado')
    
    context = {
        'total_planes': total_planes,
        'planes_activos': planes_activos,
        'planes_borrador': planes_borrador,
        'planes_recientes': planes_recientes,
        'planes_por_estado': planes_por_estado,
    }
    
    return render(request, 'planes_estudio/dashboard.html', context)


class PlanEstudioListView(LoginRequiredMixin, ListView):
    """
    Vista para listar todos los planes de estudios.
    """
    model = PlanEstudio
    template_name = 'planes_estudio/plan_estudio_list.html'
    context_object_name = 'planes'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = PlanEstudio.objects.select_related('carrera', 'work_center').order_by('-fecha_creacion')
        
        # Filtros
        search = self.request.GET.get('search')
        estado = self.request.GET.get('estado')
        carrera = self.request.GET.get('carrera')
        
        if search:
            queryset = queryset.filter(
                Q(nombre__icontains=search) |
                Q(carrera__nombre__icontains=search) |
                Q(work_center__name__icontains=search)
            )
        
        if estado:
            queryset = queryset.filter(estado=estado)
        
        if carrera:
            queryset = queryset.filter(carrera_id=carrera)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estados'] = PlanEstudio.ESTADO_CHOICES
        context['carreras'] = PlanEstudio.objects.values_list('carrera__nombre', flat=True).distinct()
        return context


class PlanEstudioDetailView(LoginRequiredMixin, DetailView):
    """
    Vista para mostrar los detalles de un plan de estudios.
    """
    model = PlanEstudio
    template_name = 'planes_estudio/plan_estudio_detail.html'
    context_object_name = 'plan'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plan = self.get_object()
        
        # Obtener semestres ordenados
        context['semestres'] = plan.semestres.all().prefetch_related('materias__materia')
        
        # Estadísticas del plan
        context['total_materias'] = sum(
            semestre.materias.count() for semestre in context['semestres']
        )
        context['creditos_actuales'] = plan.get_creditos_actuales()
        
        # Objetivos educativos
        context['objetivos'] = plan.objetivos_educativos.all()
        
        # Perfil de egreso
        try:
            context['perfil_egreso'] = plan.perfil_egreso
        except PerfilEgreso.DoesNotExist:
            context['perfil_egreso'] = None
        
        return context


class PlanEstudioCreateView(LoginRequiredMixin, CreateView):
    """
    Vista para crear un nuevo plan de estudios.
    """
    model = PlanEstudio
    form_class = PlanEstudioForm
    template_name = 'planes_estudio/plan_estudio_form.html'
    success_url = reverse_lazy('planes_estudio:plan_list')
    
    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        messages.success(self.request, _('Plan de estudios creado exitosamente.'))
        return super().form_valid(form)


class PlanEstudioUpdateView(LoginRequiredMixin, UpdateView):
    """
    Vista para editar un plan de estudios.
    """
    model = PlanEstudio
    form_class = PlanEstudioForm
    template_name = 'planes_estudio/plan_estudio_form.html'
    
    def get_success_url(self):
        return reverse_lazy('planes_estudio:plan_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, _('Plan de estudios actualizado exitosamente.'))
        return super().form_valid(form)


class PlanEstudioDeleteView(LoginRequiredMixin, DeleteView):
    """
    Vista para eliminar un plan de estudios.
    """
    model = PlanEstudio
    template_name = 'planes_estudio/plan_estudio_confirm_delete.html'
    success_url = reverse_lazy('planes_estudio:plan_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, _('Plan de estudios eliminado exitosamente.'))
        return super().delete(request, *args, **kwargs)


# Vistas para Semestres
@login_required
def semestre_list(request, plan_id):
    """
    Vista para listar los semestres de un plan de estudios.
    """
    plan = get_object_or_404(PlanEstudio, pk=plan_id)
    semestres = plan.semestres.all().order_by('numero_semestre')
    
    context = {
        'plan': plan,
        'semestres': semestres,
    }
    return render(request, 'planes_estudio/semestre_list.html', context)


@login_required
def semestre_create(request, plan_id):
    """
    Vista para crear un nuevo semestre.
    """
    plan = get_object_or_404(PlanEstudio, pk=plan_id)
    
    if request.method == 'POST':
        form = SemestrePlanForm(request.POST)
        if form.is_valid():
            semestre = form.save(commit=False)
            semestre.plan_estudio = plan
            semestre.save()
            messages.success(request, _('Semestre creado exitosamente.'))
            return redirect('planes_estudio:semestre_list', plan_id=plan_id)
    else:
        form = SemestrePlanForm()
    
    context = {
        'plan': plan,
        'form': form,
    }
    return render(request, 'planes_estudio/semestre_form.html', context)


@login_required
def semestre_update(request, plan_id, semestre_id):
    """
    Vista para editar un semestre.
    """
    plan = get_object_or_404(PlanEstudio, pk=plan_id)
    semestre = get_object_or_404(SemestrePlan, pk=semestre_id, plan_estudio=plan)
    
    if request.method == 'POST':
        form = SemestrePlanForm(request.POST, instance=semestre)
        if form.is_valid():
            form.save()
            messages.success(request, _('Semestre actualizado exitosamente.'))
            return redirect('planes_estudio:semestre_list', plan_id=plan_id)
    else:
        form = SemestrePlanForm(instance=semestre)
    
    context = {
        'plan': plan,
        'semestre': semestre,
        'form': form,
    }
    return render(request, 'planes_estudio/semestre_form.html', context)


# Vistas para Materias
@login_required
def materia_list(request, plan_id, semestre_id):
    """
    Vista para listar las materias de un semestre.
    """
    plan = get_object_or_404(PlanEstudio, pk=plan_id)
    semestre = get_object_or_404(SemestrePlan, pk=semestre_id, plan_estudio=plan)
    materias = semestre.materias.all().order_by('orden')
    
    context = {
        'plan': plan,
        'semestre': semestre,
        'materias': materias,
    }
    return render(request, 'planes_estudio/materia_list.html', context)


@permission_required('planes_estudio.add_materiaplan', raise_exception=True)
@login_required
def materia_create(request, plan_id, semestre_id):
    """
    Vista para crear una nueva materia en un semestre.
    """
    plan = get_object_or_404(PlanEstudio, pk=plan_id)
    semestre = get_object_or_404(SemestrePlan, pk=semestre_id, plan_estudio=plan)
    
    if request.method == 'POST':
        form = MateriaPlanForm(request.POST)
        if form.is_valid():
            materia = form.save(commit=False)
            materia.semestre = semestre
            materia.save()
            form.save_m2m()  # Para los prerrequisitos
            messages.success(request, _('Materia agregada exitosamente.'))
            return redirect('planes_estudio:materia_list', plan_id=plan_id, semestre_id=semestre_id)
    else:
        form = MateriaPlanForm()
    
    context = {
        'plan': plan,
        'semestre': semestre,
        'form': form,
    }
    return render(request, 'planes_estudio/materia_form.html', context)


@permission_required('planes_estudio.change_materiaplan', raise_exception=True)
@login_required
def materia_update(request, plan_id, semestre_id, materia_id):
    """
    Vista para editar una materia.
    """
    plan = get_object_or_404(PlanEstudio, pk=plan_id)
    semestre = get_object_or_404(SemestrePlan, pk=semestre_id, plan_estudio=plan)
    materia = get_object_or_404(MateriaPlan, pk=materia_id, semestre=semestre)
    
    if request.method == 'POST':
        form = MateriaPlanForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            messages.success(request, _('Materia actualizada exitosamente.'))
            return redirect('planes_estudio:materia_list', plan_id=plan_id, semestre_id=semestre_id)
    else:
        form = MateriaPlanForm(instance=materia)
    
    context = {
        'plan': plan,
        'semestre': semestre,
        'materia': materia,
        'form': form,
    }
    return render(request, 'planes_estudio/materia_form.html', context)


@permission_required('planes_estudio.delete_materiaplan', raise_exception=True)
@login_required
def materia_delete(request, plan_id, semestre_id, materia_id):
    """
    Vista para eliminar una materia de un semestre.
    """
    plan = get_object_or_404(PlanEstudio, pk=plan_id)
    semestre = get_object_or_404(SemestrePlan, pk=semestre_id, plan_estudio=plan)
    materia = get_object_or_404(MateriaPlan, pk=materia_id, semestre=semestre)

    if request.method == 'POST':
        materia.delete()
        messages.success(request, _('Materia eliminada exitosamente.'))
        return redirect('planes_estudio:materia_list', plan_id=plan_id, semestre_id=semestre_id)

    context = {
        'plan': plan,
        'semestre': semestre,
        'materia': materia,
    }
    return render(request, 'planes_estudio/materia_confirm_delete.html', context)


# Vistas para Competencias
class CompetenciaListView(LoginRequiredMixin, ListView):
    """
    Vista para listar todas las competencias.
    """
    model = Competencia
    template_name = 'planes_estudio/competencia_list.html'
    context_object_name = 'competencias'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Competencia.objects.all().order_by('nombre')
        
        search = self.request.GET.get('search')
        tipo = self.request.GET.get('tipo')
        
        if search:
            queryset = queryset.filter(
                Q(nombre__icontains=search) |
                Q(descripcion__icontains=search)
            )
        
        if tipo:
            queryset = queryset.filter(tipo_competencia=tipo)
        
        return queryset


class CompetenciaCreateView(LoginRequiredMixin, CreateView):
    """
    Vista para crear una nueva competencia.
    """
    model = Competencia
    form_class = CompetenciaForm
    template_name = 'planes_estudio/competencia_form.html'
    success_url = reverse_lazy('planes_estudio:competencia_list')
    
    def form_valid(self, form):
        messages.success(self.request, _('Competencia creada exitosamente.'))
        return super().form_valid(form)


# Vistas para Objetivos Educativos
@login_required
def objetivo_list(request, plan_id):
    """
    Vista para listar los objetivos educativos de un plan.
    """
    plan = get_object_or_404(PlanEstudio, pk=plan_id)
    objetivos = plan.objetivos_educativos.all().order_by('orden')
    
    context = {
        'plan': plan,
        'objetivos': objetivos,
    }
    return render(request, 'planes_estudio/objetivo_list.html', context)


@login_required
def objetivo_create(request, plan_id):
    """
    Vista para crear un nuevo objetivo educativo.
    """
    plan = get_object_or_404(PlanEstudio, pk=plan_id)
    
    if request.method == 'POST':
        form = ObjetivoEducativoForm(request.POST)
        if form.is_valid():
            objetivo = form.save(commit=False)
            objetivo.plan_estudio = plan
            objetivo.save()
            messages.success(request, _('Objetivo educativo creado exitosamente.'))
            return redirect('planes_estudio:objetivo_list', plan_id=plan_id)
    else:
        form = ObjetivoEducativoForm()
    
    context = {
        'plan': plan,
        'form': form,
    }
    return render(request, 'planes_estudio/objetivo_form.html', context)


# Vistas para Perfil de Egreso
@login_required
def perfil_egreso_detail(request, plan_id):
    """
    Vista para mostrar/editar el perfil de egreso de un plan.
    """
    plan = get_object_or_404(PlanEstudio, pk=plan_id)
    
    try:
        perfil = plan.perfil_egreso
    except PerfilEgreso.DoesNotExist:
        perfil = None
    
    if request.method == 'POST':
        if perfil:
            form = PerfilEgresoForm(request.POST, instance=perfil)
        else:
            form = PerfilEgresoForm(request.POST)
        
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.plan_estudio = plan
            perfil.save()
            messages.success(request, _('Perfil de egreso guardado exitosamente.'))
            return redirect('planes_estudio:perfil_egreso_detail', plan_id=plan_id)
    else:
        if perfil:
            form = PerfilEgresoForm(instance=perfil)
        else:
            form = PerfilEgresoForm()
    
    context = {
        'plan': plan,
        'perfil': perfil,
        'form': form,
    }
    return render(request, 'planes_estudio/perfil_egreso_form.html', context)


# Vista de documentación
@login_required
def documentacion_view(request):
    """
    Vista para mostrar la documentación del módulo de planes de estudios.
    """
    return render(request, 'planes_estudio/documentacion.html')


# Vistas AJAX para funcionalidades dinámicas
@login_required
def get_materias_by_carrera(request):
    """
    Vista AJAX para obtener materias por carrera.
    """
    carrera_id = request.GET.get('carrera_id')
    if carrera_id:
        from core.models import Materia
        materias = Materia.objects.filter(carrera_id=carrera_id).values('id', 'nombre', 'codigo')
        return JsonResponse({'materias': list(materias)})
    return JsonResponse({'materias': []})


@login_required
def get_semestres_by_plan(request):
    """
    Vista AJAX para obtener semestres por plan de estudios.
    """
    plan_id = request.GET.get('plan_id')
    if plan_id:
        semestres = SemestrePlan.objects.filter(plan_estudio_id=plan_id).values('id', 'numero_semestre', 'nombre')
        return JsonResponse({'semestres': list(semestres)})
    return JsonResponse({'semestres': []})
