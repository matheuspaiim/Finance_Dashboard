from django.urls import path
from django.views.generic import TemplateView
from investments.views import home, form, create, view

urlpatterns = [
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('charts.html', TemplateView.as_view(template_name='investments/charts.html')),
    path('form.html', TemplateView.as_view(template_name='investments/form.html')),
    path('tables.html', TemplateView.as_view(template_name='investments/tables.html')),
    path('investments.html', TemplateView.as_view(template_name='investments/investments.html')),
    path('create/charts.html', TemplateView.as_view(template_name='investments/charts.html')),
    path('create/form.html', TemplateView.as_view(template_name='investments/form.html')),
    path('create/tables.html', TemplateView.as_view(template_name='investments/tables.html')),
    path('create/investments.html', TemplateView.as_view(template_name='investments/investments.html')),
]