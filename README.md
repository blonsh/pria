# PRIA - Plataforma de Registro e Información Académica

## Descripción
PRIA es una plataforma de gestión escolar que facilita la administración educativa de manera organizada, eficiente y adaptable. La plataforma está diseñada para ser modular y escalable, permitiendo una gestión integral de los recursos educativos.

## Estructura del Proyecto

```
pria/
├── pria/                     # Configuración principal de Django
│   ├── settings.py          # Configuración principal
│   ├── urls.py             # URLs principales
│   └── wsgi.py             # Configuración WSGI
├── core/                    # Aplicación principal
│   ├── models.py           # Modelos principales
│   ├── views.py            # Vistas principales
│   ├── urls.py             # URLs de la aplicación
│   └── templates/          # Templates principales
├── users/                   # Módulo de Gestión de Usuarios
│   ├── models.py           # Modelos de usuarios y roles
│   ├── forms.py            # Formularios de usuarios
│   ├── views.py            # Vistas de usuarios
│   ├── urls.py             # URLs de usuarios
│   └── templates/          # Templates de usuarios
│       ├── dashboard.html  # Dashboard de usuarios
│       ├── role_form.html  # Formulario de roles
│       └── user_form.html  # Formulario de usuarios
├── workcenter/              # Módulo de Gestión del Centro de Trabajo
│   ├── models.py           # Modelos de centro de trabajo
│   ├── forms.py            # Formularios de centro de trabajo
│   ├── views.py            # Vistas de centro de trabajo
│   ├── urls.py             # URLs de centro de trabajo
│   └── templates/          # Templates de centro de trabajo
│       ├── dashboard.html  # Dashboard de centro de trabajo
│       ├── workcenter_form.html  # Formulario de centro de trabajo
│       ├── classroom_form.html   # Formulario de aulas
│       ├── schoolcycle_form.html # Formulario de ciclos
│       └── schoolperiod_form.html # Formulario de periodos
├── static/                  # Archivos estáticos
│   ├── css/                # Estilos CSS
│   ├── js/                 # Scripts JavaScript
│   └── images/             # Imágenes
└── templates/              # Templates base
    └── base.html           # Template base
```

## Requisitos

- Python 3.8+
- PostgreSQL 12+
- Dependencias del proyecto (ver requirements.txt)

## Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPO]
cd pria
```

2. Crear un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Crear archivo de configuración:
```bash
cp .env.example .env
# Editar .env con tus credenciales de base de datos
```

5. Aplicar migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Crear superusuario:
```bash
python manage.py createsuperuser
```

7. Iniciar el servidor:
```bash
python manage.py runserver
```

## Características Principales

### Gestión de Usuarios
- Sistema de roles y permisos
- Gestión de usuarios
- Asignación de roles
- Permisos por módulo

### Gestión del Centro de Trabajo
- Creación y gestión de centros de trabajo
- Gestión de aulas
- Gestión de ciclos escolares
- Gestión de periodos escolares

## Variables de Entorno

Crear un archivo `.env` con las siguientes variables:

```
DB_NAME=pria
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DJANGO_SECRET_KEY=your_secret_key
```

## Licencia

MIT License - Ver LICENSE para más detalles

## Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Soporte

Para soporte o consultas, contactar a:
- Email: soporte@pria.com
- Teléfono: +52 123 456 7890
