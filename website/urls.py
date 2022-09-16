from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('', TemplateView.as_view(template_name='website/index.html')),
    path('index.html', TemplateView.as_view(template_name='website/index.html')),
    path('delete.html', TemplateView.as_view(template_name='website/delete.html')),
]