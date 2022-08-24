from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.RegistroListView.as_view(), name='registro_changelist'),
    path('add/', views.RegistroCreateView.as_view(), name='registro_add'),
    path('<int:pk>/', views.RegistroUpdateView.as_view(), name='registro_change'),
]