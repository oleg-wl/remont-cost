from django.urls import path

from . import views

app_name = 'form'
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('view/', views.Purch_view.as_view(), name='view')
]