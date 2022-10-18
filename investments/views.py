from .models import Registry
from django.shortcuts import render, redirect
from .models import *
from .forms import RegistryForm, LoginForm


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
    form = RegistryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tables')

    context = {'form': form}
    return render(request, 'investments/form.html', context)


def register_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def edit(request, registration_pk):
    registry = Registry.objects.get(pk=registration_pk)

    form = RegistryForm(request.POST or None, instance=registry)
    if form.is_valid():
        form.save()
        return redirect("reports")

    context = {'form': form}
    return render(request, '/', context)


def destroy(request, registration_pk):
    material = Registry.objects.get(pk=registration_pk)
    material.delete()
    return redirect("tables")
