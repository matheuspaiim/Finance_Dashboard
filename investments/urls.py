from django.urls import path

from . import views

urlpatterns = [
    path('create_registry/', views.createRegistry, name="create_registry"),
    path('update_registry/<str:pk>/', views.updateRegistry, name="update_registry"),
    path('delete_registry/<str:pk>/', views.deleteRegistry, name="delete_registry"),
]