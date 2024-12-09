from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from API import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('home/viaturas/', views.viaturas, name='viaturas'),
    path('viaturas/checkout/', views.checkout, name='checkout'),
]

# Configuração para servir arquivos estáticos
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Configuração para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:  # Apenas em ambiente de desenvolvimento
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)