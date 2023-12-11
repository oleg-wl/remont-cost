from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from pydantic import ValidationError

from .models import Purchases, Types
from .schemas import PurchaseValidation

from .forms import InputForm
from django.db.models import Sum

from .pivot import create_table

class InputView(View):
    def get(self, request):
        message = request.session.get('message', False)
        if message: del(request.session['message'])

        form = InputForm()
        context = {'form': form, 'message': message}

        return render(request, 'form/insert.html', context=context)

    def post(self, request):

        form = InputForm(request.POST)
        if not form.is_valid():
            context = {'form':form}
            return render(request, 'form/insert.html', context=context)
        p = form.save()
        request.session['message'] = '{} добавлено успешно'.format(p.info)
        return redirect('/insert')
        
class index(TemplateView):
    template_name = "form/index.html"


class PurchaisesListView(ListView):
    template_name = "form/view.html"
    context_object_name = "rows"

    def get_queryset(self):
        return Purchases.objects.order_by('-day')

    def get_context_data(self, **kwargs):
        context = super(PurchaisesListView, self).get_context_data(**kwargs)
        context['total_sum'] = Purchases.objects.all().aggregate(sum_all=Sum('amount')).get('sum_all')
        return context

class PurchaisesDetailedView(DetailView):
    model = Purchases

class PurchaisesDeleteView(DeleteView):
    model = Purchases
    success_url = reverse_lazy('form:view')
    fiedls = '__all__'
    

def table(request):

    table = create_table()
    
    return render(request=request, template_name='form/table.html', context={'table':table})
