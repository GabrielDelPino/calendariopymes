# login/urls.py

# login/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Redirigir a la vista de inicio de sesión al acceder a la raíz
    path('home/', views.home, name='home'),  # Ruta para la página de inicio
]









