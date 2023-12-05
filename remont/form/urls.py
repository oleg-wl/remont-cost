from django.urls import path

from . import views

app_name = 'form'
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('view/', views.PurchaisesListView.as_view(), name='view'),
    path('insert/', views.InputView.as_view(), name='insert'),
]