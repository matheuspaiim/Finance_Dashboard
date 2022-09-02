from .models import Registry
from django.shortcuts import render, redirect
from .models import *
from .forms import RegistryForm


# Create your views here.
def investments(request):
    return render(request, 'investments/investments.html')


def tables(request):
    return render(request, 'investments/tables.html')


def charts(request):
    return render(request, 'investments/charts.html')


def createRegistry(request):
    form = RegistryForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = RegistryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'investments/form.html', context)


def updateRegistry(request, pk):
    registry = Registry.objects.get(id=pk)
    form = RegistryForm(instance=registry)

    if request.method == 'POST':
        form = RegistryForm(request.POST, instance=registry)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'investments/form.html', context)


def deleteRegistry(request, pk):
    registry = Registry.objects.get(id=pk)
    if request.method == "POST":
        registry.delete()
        return redirect('/')

    context = {'item': registry}
    return render(request, 'investments/delete.html', context)
