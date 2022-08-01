"""Finance_Dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html', TemplateView.as_view(template_name='website/index.html')),
    path('404.html', TemplateView.as_view(template_name='website/404.html')),
    path('charts.html', TemplateView.as_view(template_name='website/charts.html')),
    path('forgot-password.html', TemplateView.as_view(template_name='account/forgot-password.html')),
    path('login.html', TemplateView.as_view(template_name='account/login.html')),
    path('register.html', TemplateView.as_view(template_name='account/register.html')),
    path('tables.html', TemplateView.as_view(template_name='website/tables.html')),
    path('', TemplateView.as_view(template_name='website/index.html'))
]
