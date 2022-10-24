from django.http import HttpResponseRedirect
from django.utils.dateparse import parse_datetime
from django.shortcuts import render, redirect
from .models import *
from .forms import LoginForm


# Create your views here.


def index(request):
    return render(request, 'website/index.html')


def forms(request):
    return render(request, 'investments/form.html')


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'accounts/register.html')


def forgot(request):
    return render(request, 'accounts/forgot-password.html')


def charts(request):
    return render(request, 'investments/charts.html')


def tables(request):
    registry = Registry.objects.all()

    context = {
        'registry': registry
    }
    return render(request, 'investments/tables.html', context)


def investments(request):
    investment = Investments.objects.all()

    context = {
        'investment': investment
    }
    return render(request, 'investments/investments_table.html', context)


def investments_add(request):
    if request.method == "POST":
        if request.POST.get('tipo') and \
                request.POST.get('nome') and \
                request.POST.get('taxa') and \
                request.POST.get('taxa_corretagem') and \
                request.POST.get('data_compra') and \
                request.POST.get('data_vencimento') and \
                request.POST.get('banco') and \
                request.POST.get('corretora') and \
                request.POST.get('quantidade'):
            investment = Investments()
            investment.tipo = request.POST.get('tipo')
            investment.nome = request.POST.get('nome')
            investment.taxa = parse_datetime(request.POST.get('taxa'))
            investment.taxa_corretagem = request.POST.get('taxa_corretagem')
            investment.data_compra = request.POST.get('data_compra')
            investment.data_vencimento = request.POST.get('data_vencimento')
            investment.banco = request.POST.get('banco')
            investment.corretora = request.POST.get('corretora')
            investment.quantidade = request.POST.get('quantidade')
            investment.save()
            return HttpResponseRedirect('/')
    else:
        return render(request, 'investments/investments.html')


def registration(request):
    if request.method == "POST":
        if request.POST.get('descricao') and \
                request.POST.get('escolha') and \
                request.POST.get('data_entrada') and \
                request.POST.get('quantia') or \
                request.POST.get('categoria'):
            registry = Registry()
            registry.descricao = request.POST.get('descricao')
            registry.escolha = request.POST.get('escolha')
            registry.data_entrada = parse_datetime(request.POST.get('data_entrada'))
            registry.quantia = request.POST.get('quantia')
            registry.categoria = request.POST.get('categoria')
            registry.save()
            return HttpResponseRedirect('/')
    else:
        return render(request, 'investments/form.html')


def register_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def edit(request, id):
    tables = Registry.objects.get(id=id)
    return render(request, 'investments/', {"Registry": tables})


def delete(request, registry_pk):
    tables = Registry.objects.get(pk=registry_pk)
    tables.delete()
    return redirect("tables")
