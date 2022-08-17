from django.views.generic.edit import ListView, CreateView, UpdateView
from .models import Money
from django.urls import reverse_lazy


# Create your views here.
class MoneyListView(ListView):
    model = Money
    context_object_name = 'money'

    @classmethod
    def as_view(cls):
        pass


class MoneyCreateView(CreateView):
    model = Money
    fields = [('description', 'revenue', 'expense', 'date', 'amount', 'category')]
    success_url = reverse_lazy('money_changelist')


class MoneyUpdateView(CreateView):
    model = Money
    fields = [('description', 'revenue', 'expense', 'date', 'amount', 'category')]
    success_url = reverse_lazy('money_changelist')
