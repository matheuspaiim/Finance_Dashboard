from django.urls import path

from . import views

urlpatterns = [
    path('investments/', views.investments),
    path('tables/', views.tables),
    path('charts/', views.charts),
    path('create_registry/', views.createRegistry, name="create_registry"),
    path('update_registry/<str:pk>/', views.updateRegistry, name="update_registry"),
    path('delete_registry/<str:pk>/', views.deleteRegistry, name="delete_registry"),
]