from django.views.generic.edit import ListView, CreateView, UpdateView
from .models import Registro
from django.urls import reverse_lazy


# Create your views here.
class RegistroListView(ListView):
    model = Registro
    context_object_name = 'registro'

    @classmethod
    def as_view(cls):
        pass


class RegistroCreateView(CreateView):
    model = Registro
    fields = [('descricao', 'selecao', 'escolha', 'data_entrada', 'quantia', 'categoria')]
    success_url = reverse_lazy('registro_changelist')


class RegistroUpdateView(CreateView):
    model = Registro
    fields = [('descricao', 'selecao', 'escolha', 'data_entrada', 'quantia', 'categoria')]
    success_url = reverse_lazy('registro_changelist')
