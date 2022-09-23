from django.forms import ModelForm
from .models import Registry


class RegistryForm(ModelForm):
    class Meta:
        model = Registry
        fields = ['descricao', 'escolha', 'data_entrada', 'quantia', 'categoria']
