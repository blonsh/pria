import argparse
import os
import subprocess
import sys
import logging
from pathlib import Path
from datetime import datetime

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/init.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ProjectInitializer:
    def __init__(self, env='development'):
        self.env = env
        self.project_root = Path(__file__).parent.parent
        self.env_file = self.project_root / '.env'
        self.log_dir = self.project_root / 'logs'
        self.media_dir = self.project_root / 'media'
        self.static_dir = self.project_root / 'staticfiles'

    def setup_directories(self):
        """Configura los directorios necesarios"""
        for dir_path in [self.log_dir, self.media_dir, self.static_dir]:
            dir_path.mkdir(exist_ok=True)
            os.chmod(dir_path, 0o755)
        logger.info("Directorios configurados exitosamente")

    def setup_environment(self):
        """Configura el entorno de desarrollo"""
        if not self.env_file.exists():
            env_example = self.project_root / '.env.example'
            if env_example.exists():
                env_example.copy(self.env_file)
                logger.info("Archivo .env creado desde .env.example")
            else:
                logger.error("No se encontró archivo .env.example")
                sys.exit(1)

        # Configurar variables de entorno
        os.environ['DJANGO_ENV'] = self.env
        os.environ['PYTHONPATH'] = str(self.project_root)

    def install_dependencies(self):
        """Instala las dependencias necesarias"""
        req_file = 'requirements-prod.txt' if self.env == 'production' else 'requirements.txt'
        try:
            subprocess.run(['pip', 'install', '-r', req_file], check=True)
            logger.info("Dependencias instaladas exitosamente")
        except subprocess.CalledProcessError as e:
            logger.error(f"Error instalando dependencias: {e}")
            sys.exit(1)

    def run_migrations(self):
        """Ejecuta las migraciones de la base de datos"""
        try:
            subprocess.run(['python', 'manage.py', 'migrate'], check=True)
            logger.info("Migraciones completadas exitosamente")
        except subprocess.CalledProcessError as e:
            logger.error(f"Error en migraciones: {e}")
            sys.exit(1)

    def create_superuser(self):
        """Crea un superusuario si no existe"""
        try:
            result = subprocess.run(
                ['python', 'manage.py', 'shell', '-c', 
                 "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(is_superuser=True).exists())"],
                capture_output=True,
                text=True
            )
            
            if 'False' in result.stdout:
                logger.info("No se encontró superusuario. Creando uno nuevo...")
                subprocess.run(['python', 'manage.py', 'createsuperuser'])
            else:
                logger.info("Superusuario ya existe")
        except subprocess.CalledProcessError as e:
            logger.error(f"Error creando superusuario: {e}")
            sys.exit(1)

    def collect_static(self):
        """Recopila archivos estáticos"""
        try:
            subprocess.run(['python', 'manage.py', 'collectstatic', '--noinput'], check=True)
            logger.info("Archivos estáticos recopilados exitosamente")
        except subprocess.CalledProcessError as e:
            logger.error(f"Error en archivos estáticos: {e}")
            sys.exit(1)

    def start_server(self):
        """Inicia el servidor de desarrollo o producción"""
        if self.env == 'production':
            try:
                subprocess.run(['gunicorn', 'core.wsgi:application', '--bind', '0.0.0.0:8000', '--workers', '3', '--threads', '2'], check=True)
            except subprocess.CalledProcessError as e:
                logger.error(f"Error iniciando Gunicorn: {e}")
                sys.exit(1)
        else:
            try:
                subprocess.run(['python', 'manage.py', 'runserver', '0.0.0.0:8000'], check=True)
            except subprocess.CalledProcessError as e:
                logger.error(f"Error iniciando servidor de desarrollo: {e}")
                sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Script de inicialización para PRIA')
    parser.add_argument('--env', choices=['development', 'production'], default='development',
                        help='Entorno de ejecución')
    parser.add_argument('--skip-deps', action='store_true',
                        help='Saltar instalación de dependencias')
    parser.add_argument('--skip-migrations', action='store_true',
                        help='Saltar migraciones')
    parser.add_argument('--skip-static', action='store_true',
                        help='Saltar recopilación de archivos estáticos')
    
    args = parser.parse_args()

    initializer = ProjectInitializer(args.env)
    
    try:
        initializer.setup_environment()
        initializer.setup_directories()
        
        if not args.skip_deps:
            initializer.install_dependencies()
            
        if not args.skip_migrations:
            initializer.run_migrations()
            initializer.create_superuser()
            
        if not args.skip_static:
            initializer.collect_static()
            
        initializer.start_server()
        
    except Exception as e:
        logger.error(f"Error durante la inicialización: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
