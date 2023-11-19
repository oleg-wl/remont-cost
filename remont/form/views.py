from shlex import join
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import TemplateView, ListView, DetailView, View

from pydantic import ValidationError
from .models import Purchases, Types
from .schemas import PurchaseValidation


class index(TemplateView):
    template_name = "form/index.html"


class Purch_view(ListView):
    template_name = "form/view.html"
    context_object_name = "rows"

    def get_queryset(self):
        return Purchases.objects.all()


def view(request):
    q = Purchases.objects.order_by('-day')
    total_sum = sum(q.values_list("amount", flat=True))

    return render(request, "form/view.html", context={"rows": q, "total": total_sum})


def insert(request):
    t = Types.objects.all()

    message = request.session.get('message', False)
    if message: del(request.session['message'])


    return render(request, "form/insert.html", context={"types_all": t,
                                                        'message':message})


def add(request):

    type_id = request.POST["b"]
    info = request.POST["info"]
    date = request.POST["date"]
    amount = request.POST["amount"]
    
    try:
        data = PurchaseValidation(type_id=type_id, info=info, date=date, amount=amount)
        add = Purchases(
        day=data.date, amount=data.amount, info=data.info, types=Types.objects.get(pk=data.type_id)
    )
        request.session['message'] = "Запись добавлена успешно"
        add.save()
    
    except ValidationError as valerr:
        errlist = [e.get('msg') for e in valerr.errors()]
        request.session['message'] = ' ,'.join(errlist)

    except Exception as e:
        request.session['message'] = "Ошибка добавления записи"
        print(e)

    return redirect('/insert')