from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.MoneyListView.as_view(), name='money_changelist'),
    path('add/', views.MoneyCreateView.as_view(), name='money_add'),
    path('<int:pk>/', views.MoneyUpdateView.as_view(), name='money_change'),
]