from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser
from .models import ActivityLog

class ActivityLogMiddleware(MiddlewareMixin):
    """
    Middleware para registrar automáticamente las actividades de los usuarios.
    """
    
    def process_request(self, request):
        # Solo registrar para usuarios autenticados
        if not hasattr(request, 'user') or isinstance(request.user, AnonymousUser):
            return None
        
        # Obtener información de la solicitud
        ip_address = self.get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        # Almacenar información para usar en process_response
        request.activity_log_info = {
            'ip_address': ip_address,
            'user_agent': user_agent,
        }
        
        return None
    
    def process_response(self, request, response):
        # Solo registrar para usuarios autenticados y respuestas exitosas
        if not hasattr(request, 'user') or isinstance(request.user, AnonymousUser):
            return response
        
        if response.status_code != 200:
            return response
        
        # Determinar la acción basada en el método HTTP
        action = self.get_action_from_request(request)
        if not action:
            return response
        
        # Determinar el módulo basado en la URL
        module = self.get_module_from_url(request.path)
        if not module:
            return response
        
        # Crear descripción
        description = self.create_description(request, action, module)
        
        # Registrar la actividad
        try:
            ActivityLog.log_activity(
                user=request.user,
                action=action,
                module=module,
                object_type='HTTP Request',
                description=description,
                ip_address=request.activity_log_info.get('ip_address'),
                user_agent=request.activity_log_info.get('user_agent'),
                additional_data={
                    'method': request.method,
                    'path': request.path,
                    'status_code': response.status_code,
                }
            )
        except Exception as e:
            # No interrumpir la respuesta por errores en el logging
            pass
        
        return response
    
    def get_client_ip(self, request):
        """Obtener la dirección IP del cliente."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def get_action_from_request(self, request):
        """Determinar la acción basada en el método HTTP y la URL."""
        method = request.method
        path = request.path
        
        if method == 'GET':
            if 'login' in path:
                return 'LOGIN'
            elif 'logout' in path:
                return 'LOGOUT'
            elif 'create' in path or 'new' in path:
                return 'VIEW'
            else:
                return 'VIEW'
        elif method == 'POST':
            if 'create' in path or 'new' in path:
                return 'CREATE'
            elif 'update' in path or 'edit' in path:
                return 'UPDATE'
            elif 'delete' in path:
                return 'DELETE'
            elif 'login' in path:
                return 'LOGIN'
            else:
                return 'UPDATE'
        elif method == 'DELETE':
            return 'DELETE'
        elif method == 'PUT':
            return 'UPDATE'
        elif method == 'PATCH':
            return 'UPDATE'
        
        return None
    
    def get_module_from_url(self, path):
        """Determinar el módulo basado en la URL."""
        if 'users' in path:
            return 'USERS'
        elif 'alumnos' in path:
            return 'ALUMNOS'
        elif 'docentes' in path:
            return 'DOCENTES'
        elif 'asistencia' in path:
            return 'ASISTENCIA'
        elif 'planes-estudio' in path or 'planes_estudio' in path:
            return 'PLANES_ESTUDIO'
        elif 'workcenter' in path:
            return 'WORKCENTER'
        elif 'matriculas' in path:
            return 'MATRICULAS'
        elif 'reportes' in path:
            return 'REPORTES'
        elif 'logs' in path:
            return 'SYSTEM'
        elif 'control-escolar' in path:
            return 'CONTROL_ESCOLAR'
        else:
            return 'SYSTEM'
    
    def create_description(self, request, action, module):
        """Crear una descripción legible de la actividad."""
        method = request.method
        path = request.path
        
        if action == 'LOGIN':
            return f"Inició sesión en el sistema"
        elif action == 'LOGOUT':
            return f"Cerro sesión en el sistema"
        elif action == 'VIEW':
            return f"Consultó {self.get_module_display(module)}"
        elif action == 'CREATE':
            return f"Creó un nuevo registro en {self.get_module_display(module)}"
        elif action == 'UPDATE':
            return f"Actualizó un registro en {self.get_module_display(module)}"
        elif action == 'DELETE':
            return f"Eliminó un registro en {self.get_module_display(module)}"
        else:
            return f"Realizó {action} en {self.get_module_display(module)}"
    
    def get_module_display(self, module):
        """Obtener el nombre legible del módulo."""
        module_names = {
            'USERS': 'Gestión de Usuarios',
            'ALUMNOS': 'Gestión de Alumnos',
            'DOCENTES': 'Gestión de Docentes',
            'ASISTENCIA': 'Control de Asistencia',
            'PLANES_ESTUDIO': 'Planes de Estudio',
            'WORKCENTER': 'Centro de Trabajo',
            'MATRICULAS': 'Matrículas',
            'REPORTES': 'Reportes',
            'CONTROL_ESCOLAR': 'Control Escolar',
            'SYSTEM': 'Sistema',
        }
        return module_names.get(module, module) 