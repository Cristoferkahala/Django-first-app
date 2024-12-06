from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from API import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('viaturas/', views.viaturas, name='viaturas'),
    path('viaturas/checkout/', views.checkout, name='checkout')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)