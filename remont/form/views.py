from django.shortcuts import render
from django.http import HttpResponse 

from django.views.generic import TemplateView, ListView

from .models import Purchases, Types

# Create your views here.

class index(TemplateView):
    template_name = 'form/index.html'

class Purch_view(ListView):
    template_name = 'form/view.html'
    context_object_name = 'rows'
    
    def get_queryset(self):
        return Purchases.objects.all()
    
