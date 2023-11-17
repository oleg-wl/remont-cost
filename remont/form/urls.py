from django.urls import path

from . import views

app_name = 'form'
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('view/', views.view, name='view'),
    path('insert/', views.insert, name='insert'),
    path('add/', views.add, name='add')
]