from django.contrib import admin
from django.urls import path, include
from usuarios.views import landing_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('cuentas/', include('cuentas.urls')),
    path('solicitudes/', include('solicitudes.urls')),
    path('auditoria/', include('auditoria.urls')),
]

# Esto va fuera del listado principal
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

