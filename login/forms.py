from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        help_texts = {
            'username': 'Requerido. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_.',
            'password1': 'La contraseña no puede ser demasiado similar a otra información personal. Debe contener al menos 8 caracteres y no puede ser completamente numérica.',
            'password2': 'Introduce la misma contraseña que antes, para verificar.',
        }
