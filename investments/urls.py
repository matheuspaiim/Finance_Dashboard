from django.urls import path
from investments import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('form', views.forms, name='form'),
    path('tables', views.tables, name='tables'),
    path('charts', views.charts, name='charts'),
    path('investments', views.investments, name='investments'),
    path('login', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot', views.forgot, name='forgot'),

    path('register_login/', views.register_login, name='register_login'),
    path('registration/', views.registration, name='registration'),
    path('edit/<int:register_pk>/edit', views.edit, name='edit'),
    path('delete/<int:register_pk>', views.destroy, name='delete'),

]