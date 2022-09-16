from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('password/', views.password),
    path('forgot-password.html', TemplateView.as_view(template_name='accounts/forgot-password.html')),
    path('login.html', TemplateView.as_view(template_name='accounts/login.html')),
    path('register.html', TemplateView.as_view(template_name='accounts/register.html')),
]
