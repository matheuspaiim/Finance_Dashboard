from .models import Registry
from django.shortcuts import render, redirect
from .models import *
from .forms import RegistryForm


# Create your views here.


def home(request):
    return render(request, 'website/index.html')


def form(request):
    data = {}
    data['form'] = RegistryForm()
    return render(request, 'investments/tables.html', data)


def create(request):
    form = RegistryForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = RegistryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'investments/form.html', context)


def view(request, pk):
    data = {}
    data['db'] = Registry.objects.get(pk=pk)
    return render(request, 'investments/tables.html', data)


def update(request, pk):
    registries = Registry.objects.get(id=pk)
    form = RegistryForm(instance=registries)

    if request.method == 'POST':
        form = RegistryForm(request.POST, instance=registries)
        if form.is_valid():
            form.save()
            return redirect('website/index.html')

    context = {'form': form}
    return render(request, 'investments/form.html', context)


def delete(request, pk):
    registries = Registry.objects.get(id=pk)
    if request.method == "POST":
        registries.delete()
        return redirect('/')

    context = {'item': registries}
    return render(request, 'investments/delete.html', context)
