from django.forms import ModelForm
from .models import Login, Investments
from django import forms


class LoginForm(ModelForm):
    class Meta:
        model = Login
        exclude = ()

        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control form-control-user', 'placeholder': 'Nome', 'autofocus': ''}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Sobrenome'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Email'}),
            'senha': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Senha'}),
            'repetir_senha': forms.TextInput(
                attrs={'class': 'form-control form-control-user', 'placeholder': 'Repetir Senha'}),
        }