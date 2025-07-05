from django.core.management.base import BaseCommand
from workcenter.models import WorkCenter

class Command(BaseCommand):
    help = 'Lista todos los centros de trabajo registrados en el sistema'

    def handle(self, *args, **options):
        work_centers = WorkCenter.objects.all().order_by('name')
        
        if work_centers.exists():
            self.stdout.write(
                self.style.SUCCESS(f'\n📊 Total de centros de trabajo: {work_centers.count()}\n')
            )
            
            for i, center in enumerate(work_centers, 1):
                self.stdout.write(
                    f'{i}. {center.name}'
                )
                self.stdout.write(
                    f'   📍 Dirección: {center.address}'
                )
                self.stdout.write(
                    f'   👨‍💼 Director: {center.director_name}'
                )
                self.stdout.write(
                    f'   📋 Control Escolar: {center.school_control_name}'
                )
                self.stdout.write(
                    f'   🏫 Aulas: {center.classroom_set.count()} | Ciclos: {center.schoolcycle_set.count()}'
                )
                self.stdout.write('')
        else:
            self.stdout.write(
                self.style.WARNING('⚠️  No hay centros de trabajo registrados en el sistema.')
            ) 