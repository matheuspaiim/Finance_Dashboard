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
    registry = Registry.objects.all()

    context = {
        'registry': registry
    }
    return render(request, 'investments/investments.html', context)


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
    registry = Registry.objects.get(id=id)
    return render(request, 'investments/', {"Registry": registry})


def delete(request, registry_id):
    registry = Registry.objects.get(id=registry_id)
    registry.delete()
    return redirect("tables")
