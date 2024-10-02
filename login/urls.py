# login/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Ruta para la vista de inicio de sesión
    path('home/', views.home, name='home'),  # Ruta para la página de inicio
]








