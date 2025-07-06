# 🎓 PRIA - Plataforma de Registro e Información Académica

[![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Descripción

**PRIA** es una plataforma integral de gestión escolar que facilita la administración educativa de manera organizada, eficiente y adaptable. La plataforma está diseñada para ser modular y escalable, permitiendo una gestión integral de los recursos educativos, planes de estudios, materias y usuarios.

### 🎯 Características Principales

- **📚 Gestión de Planes de Estudios** - Creación y administración completa de planes académicos
- **📖 Gestión de Materias** - Asignación y configuración de materias por semestre
- **👥 Gestión de Usuarios** - Sistema de roles y permisos avanzado
- **🏫 Gestión de Centros de Trabajo** - Administración de centros educativos
- **📊 Dashboard Interactivo** - Estadísticas y métricas en tiempo real
- **🎨 Interfaz Moderna** - UI/UX mejorada con iconos y animaciones
- **📱 Responsive Design** - Compatible con dispositivos móviles

## 🏗️ Estructura del Proyecto

```
PRIA - Plataforma de registro e Información académica/
├── 📁 core/                    # Aplicación principal
│   ├── models.py              # Modelos principales
│   ├── views.py               # Vistas principales
│   ├── urls.py                # URLs de la aplicación
│   ├── forms.py               # Formularios principales
│   ├── decorators.py          # Decoradores personalizados
│   └── templates/             # Templates principales
│       ├── base.html          # Template base
│       ├── home.html          # Página de inicio
│       ├── login.html         # Página de login
│       └── register_user.html # Registro de usuarios
├── 📁 users/                   # Módulo de Gestión de Usuarios
│   ├── models.py              # Modelos de usuarios y roles
│   ├── forms.py               # Formularios de usuarios
│   ├── views.py               # Vistas de usuarios
│   ├── urls.py                # URLs de usuarios
│   └── templates/             # Templates de usuarios
│       ├── dashboard.html     # Dashboard de usuarios
│       ├── role_form.html     # Formulario de roles
│       └── user_form.html     # Formulario de usuarios
├── 📁 planes_estudio/          # Módulo de Planes de Estudios
│   ├── models.py              # Modelos de planes, semestres, materias
│   ├── forms.py               # Formularios de planes y materias
│   ├── views.py               # Vistas de planes de estudios
│   ├── urls.py                # URLs de planes de estudios
│   └── templates/             # Templates de planes de estudios
│       ├── dashboard.html     # Dashboard de planes de estudios
│       ├── plan_estudio_list.html    # Lista de planes
│       ├── plan_estudio_detail.html  # Detalle de plan
│       ├── plan_estudio_form.html    # Formulario de plan
│       ├── materia_list.html         # Lista de materias
│       ├── materia_form.html         # Formulario de materia
│       └── documentacion.html        # Documentación
├── 📁 workcenter/              # Módulo de Gestión del Centro de Trabajo
│   ├── models.py              # Modelos de centro de trabajo
│   ├── forms.py               # Formularios de centro de trabajo
│   ├── views.py               # Vistas de centro de trabajo
│   ├── urls.py                # URLs de centro de trabajo
│   └── templates/             # Templates de centro de trabajo
│       ├── dashboard.html     # Dashboard de centro de trabajo
│       ├── workcenter_form.html     # Formulario de centro de trabajo
│       ├── classroom_form.html      # Formulario de aulas
│       ├── schoolcycle_form.html    # Formulario de ciclos
│       └── schoolperiod_form.html   # Formulario de periodos
├── 📁 alumnos/                 # Módulo de Gestión de Alumnos
│   ├── models.py              # Modelos de alumnos
│   ├── forms.py               # Formularios de alumnos
│   ├── views.py               # Vistas de alumnos
│   ├── urls.py                # URLs de alumnos
│   └── templates/             # Templates de alumnos
├── 📁 docentes/                # Módulo de Gestión de Docentes
│   ├── models.py              # Modelos de docentes
│   ├── forms.py               # Formularios de docentes
│   ├── views.py               # Vistas de docentes
│   ├── urls.py                # URLs de docentes
│   └── templates/             # Templates de docentes
├── 📁 asistencia/              # Módulo de Gestión de Asistencia
│   ├── models.py              # Modelos de asistencia
│   ├── forms.py               # Formularios de asistencia
│   ├── views.py               # Vistas de asistencia
│   ├── urls.py                # URLs de asistencia
│   └── templates/             # Templates de asistencia
├── 📁 static/                  # Archivos estáticos
│   ├── css/                   # Estilos CSS
│   ├── js/                    # Scripts JavaScript
│   └── images/                # Imágenes
├── 📁 templates/               # Templates base
│   └── base.html              # Template base
├── 📁 scripts/                 # Scripts de utilidad
│   ├── setup_project.sh       # Script de configuración
│   ├── start.sh               # Script de inicio
│   └── install.sh             # Script de instalación
└── 📁 logs/                    # Archivos de log
```

## 🚀 Características Detalladas

### 📚 **Gestión de Planes de Estudios**
- ✅ **Creación de Planes** - Formularios intuitivos para crear planes de estudios
- ✅ **Gestión de Semestres** - Organización de materias por semestres
- ✅ **Asignación de Materias** - Asignación de materias a semestres específicos
- ✅ **Estados de Planes** - Control de estados (Activo, Borrador, Inactivo)
- ✅ **Competencias y Objetivos** - Gestión de competencias y objetivos educativos
- ✅ **Perfil de Egreso** - Definición del perfil de egreso del plan
- ✅ **Documentación** - Guías y documentación integrada

### 📖 **Gestión de Materias**
- ✅ **Creación de Materias** - Formularios con validación avanzada
- ✅ **Tipos de Materia** - Obligatorias, Optativas, Electivas
- ✅ **Configuración de Horas** - Teoría, Práctica, Independiente
- ✅ **Sistema de Créditos** - Gestión automática de créditos
- ✅ **Asignación a Semestres** - Organización por semestres
- ✅ **Búsqueda y Filtros** - Búsqueda avanzada de materias

### 👥 **Gestión de Usuarios**
- ✅ **Sistema de Roles** - Roles personalizables con permisos
- ✅ **Gestión de Permisos** - Permisos granulares por módulo
- ✅ **Dashboard de Usuarios** - Interfaz administrativa
- ✅ **Formularios Avanzados** - Validación y UX mejorada

### 🏫 **Gestión de Centros de Trabajo**
- ✅ **Creación de Centros** - Gestión de centros educativos
- ✅ **Gestión de Aulas** - Administración de espacios físicos
- ✅ **Ciclos Escolares** - Control de ciclos académicos
- ✅ **Periodos Escolares** - Gestión de periodos dentro de ciclos

### 🎨 **Interfaz de Usuario Mejorada**
- ✅ **Iconos Descriptivos** - Iconos temáticos para cada sección
- ✅ **Animaciones Suaves** - Transiciones y efectos visuales
- ✅ **Diseño Responsive** - Compatible con móviles y tablets
- ✅ **Dashboard Interactivo** - Estadísticas en tiempo real
- ✅ **Navegación Intuitiva** - Breadcrumbs y navegación clara
- ✅ **Formularios Modernos** - Validación en tiempo real

## 📋 Requisitos del Sistema

### **Requisitos Mínimos**
- **Python:** 3.8 o superior
- **Django:** 4.2.7
- **Base de Datos:** PostgreSQL 12+ (recomendado) o SQLite
- **Navegador:** Chrome, Firefox, Safari, Edge (versiones recientes)

### **Requisitos Recomendados**
- **Python:** 3.12
- **Base de Datos:** PostgreSQL 14+
- **Memoria RAM:** 4GB mínimo, 8GB recomendado
- **Almacenamiento:** 10GB de espacio libre

## 🛠️ Instalación y Configuración

### **1. Clonar el Repositorio**
```bash
git clone [URL_DEL_REPO]
cd "PRIA - Plataforma de registro e Información académica"
```

### **2. Crear Entorno Virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### **3. Instalar Dependencias**
```bash
pip install -r requirements.txt
```

### **4. Configurar Variables de Entorno**
Crear archivo `.env` en la raíz del proyecto:
```env
# Configuración de Base de Datos
DB_NAME=pria
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# Configuración de Django
DJANGO_SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Configuración de Email (opcional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

### **5. Configurar Base de Datos**
```bash
# Crear base de datos PostgreSQL
createdb pria

# Aplicar migraciones
python manage.py makemigrations
python manage.py migrate
```

### **6. Crear Superusuario**
```bash
python manage.py createsuperuser
```

### **7. Crear Datos de Ejemplo (Opcional)**
```bash
# Crear datos de ejemplo para testing
python create_sample_data.py
python create_sample_carreras.py
python create_sample_materias.py
python create_sample_planes_estudio.py
```

### **8. Iniciar el Servidor**
```bash
python manage.py runserver
```

## 🚀 Inicio Rápido

### **Usando Scripts Automatizados**

#### **Instalación Completa**
```bash
chmod +x scripts/install.sh
./scripts/install.sh
```

#### **Inicio del Servidor**
```bash
chmod +x scripts/start.sh
./scripts/start.sh
```

#### **Configuración del Proyecto**
```bash
chmod +x scripts/setup_project.sh
./scripts/setup_project.sh
```

## 📊 URLs Principales

### **🔐 Autenticación**
- **Login:** `http://localhost:8000/login/`
- **Registro:** `http://localhost:8000/register/`
- **Dashboard Principal:** `http://localhost:8000/`

### **📚 Planes de Estudios**
- **Dashboard:** `http://localhost:8000/planes-estudio/`
- **Lista de Planes:** `http://localhost:8000/planes-estudio/planes/`
- **Crear Plan:** `http://localhost:8000/planes-estudio/planes/crear/`
- **Documentación:** `http://localhost:8000/planes-estudio/documentacion/`

### **📖 Materias**
- **Lista de Materias:** `http://localhost:8000/planes-estudio/planes/{plan_id}/semestres/{semestre_id}/materias/`
- **Crear Materia:** `http://localhost:8000/planes-estudio/planes/{plan_id}/semestres/{semestre_id}/materias/crear/`

### **👥 Gestión de Usuarios**
- **Dashboard de Usuarios:** `http://localhost:8000/users/`
- **Lista de Usuarios:** `http://localhost:8000/users/usuarios/`
- **Gestión de Roles:** `http://localhost:8000/users/roles/`

### **🏫 Centros de Trabajo**
- **Dashboard de Centros:** `http://localhost:8000/workcenter/`
- **Lista de Centros:** `http://localhost:8000/workcenter/centros/`
- **Gestión de Aulas:** `http://localhost:8000/workcenter/aulas/`

## 🎨 Características de UX/UI

### **✨ Mejoras Implementadas**
- **Iconos Descriptivos** - Iconos temáticos para cada sección
- **Animaciones Suaves** - Transiciones y efectos visuales
- **Dashboard Interactivo** - Estadísticas en tiempo real
- **Formularios Modernos** - Validación en tiempo real
- **Navegación Intuitiva** - Breadcrumbs y navegación clara
- **Estados Visuales** - Badges y indicadores de estado
- **Responsive Design** - Compatible con dispositivos móviles

### **🎯 Funcionalidades Avanzadas**
- **Búsqueda Avanzada** - Filtros múltiples y búsqueda inteligente
- **Paginación** - Navegación eficiente en listas grandes
- **Validación en Tiempo Real** - Feedback inmediato en formularios
- **Estados Vacíos** - Mensajes informativos cuando no hay datos
- **Acciones Rápidas** - Botones de acción directa

## 🔧 Scripts de Utilidad

### **Scripts Disponibles**
- `create_sample_data.py` - Crear datos de ejemplo
- `create_sample_carreras.py` - Crear carreras de ejemplo
- `create_sample_materias.py` - Crear materias de ejemplo
- `create_sample_planes_estudio.py` - Crear planes de estudio de ejemplo
- `cleanup_pria.py` - Limpiar datos de prueba
- `check_dependencies.py` - Verificar dependencias
- `check_environment.py` - Verificar configuración del entorno

### **Uso de Scripts**
```bash
# Crear datos de ejemplo
python create_sample_data.py

# Verificar dependencias
python scripts/check_dependencies.py

# Limpiar datos de prueba
python cleanup_pria.py
```

## 🧪 Testing

### **Ejecutar Tests**
```bash
# Tests unitarios
python manage.py test

# Tests específicos
python manage.py test planes_estudio
python manage.py test users
python manage.py test workcenter
```

### **Tests de Navegador**
```bash
# Tests de funcionalidad
python test_final_functionality.py
python test_home_page.py
python test_buttons_browser.py
```

## 📈 Estadísticas del Proyecto

- **📁 Módulos:** 6 módulos principales
- **📄 Templates:** 50+ templates
- **🔧 Scripts:** 15+ scripts de utilidad
- **📊 Modelos:** 20+ modelos de datos
- **🎨 Características UX:** 15+ mejoras implementadas

## 🤝 Contribución

### **Cómo Contribuir**

1. **Fork** el proyecto
2. **Crea** una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre** un Pull Request

### **Guías de Contribución**
- Sigue las convenciones de código de Django
- Incluye tests para nuevas funcionalidades
- Documenta cambios importantes
- Mantén la consistencia en el diseño

## 📞 Soporte

### **Contacto**
- **Email:** soporte@pria.com
- **Teléfono:** +52 123 456 7890
- **Documentación:** Incluida en la aplicación

### **Reportar Problemas**
- Usa el sistema de Issues de GitHub
- Incluye información detallada del problema
- Adjunta capturas de pantalla si es necesario

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- **Django Community** - Por el excelente framework
- **Tailwind CSS** - Por los estilos modernos
- **Font Awesome** - Por los iconos
- **Contribuidores** - Por sus valiosas contribuciones

---

**🎓 PRIA** - Transformando la gestión educativa con tecnología moderna y diseño intuitivo.

*Desarrollado con ❤️ para la comunidad educativa*
