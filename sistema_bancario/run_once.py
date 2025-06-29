import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_bancario.settings")
django.setup()

from django.contrib.auth import get_user_model
from django.core.management import call_command

# Ejecutar migraciones
print("Aplicando migraciones...")
call_command("migrate")

# Ejecutar collectstatic para Render
print("Reuniendo archivos estáticos...")
call_command("collectstatic", interactive=False)

# Crear superusuario solo si no existe
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    print("Creando superusuario...")
    User.objects.create_superuser("admin", "admin@example.com", "admin123")
else:
    print("El superusuario ya existe.")
