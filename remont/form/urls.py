from django.urls import path

from . import views

app_name = 'form'
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('view/', views.PurchaisesListView.as_view(), name='view'),
    path('view/<int:pk>', views.PurchaisesDetailedView.as_view(), name='detail'),
    path('view/<int:pk>/delete/', views.PurchaisesDeleteView.as_view(), name='delete'),
    path('insert/', views.InputView.as_view(), name='insert'),
    path('table/', views.table, name='table'),
]