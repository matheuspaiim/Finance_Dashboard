from .models import Registry
from django.shortcuts import render, redirect
from .models import *
from .forms import RegistryForm


# Create your views here.
def investments(request):
    return render(request, 'investments/investments.html')


def tables(request):
    listing = Registry.objects.all()

    context = {'listing': listing}
    return render(request, 'investments/tables.html', context)


def charts(request):
    return render(request, 'investments/charts.html')


def registry(request, pk_test):
    registry = Registry.objects.get(id=pk_test)

    context = {'registry': registry}
    return render(request, 'accounts/customer.html', context)


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
    registries = Registry.objects.get(id=pk)
    form = RegistryForm(instance=registries)

    if request.method == 'POST':
        form = RegistryForm(request.POST, instance=registries)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'investments/form.html', context)


def deleteRegistry(request, pk):
    registries = Registry.objects.get(id=pk)
    if request.method == "POST":
        registries.delete()
        return redirect('/')

    context = {'item': registries}
    return render(request, 'investments/delete.html', context)
