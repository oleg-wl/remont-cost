from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView, DetailView, View

from .models import Purchases, Types


class index(TemplateView):
    template_name = "form/index.html"


class Purch_view(ListView):
    template_name = "form/view.html"
    context_object_name = "rows"

    def get_queryset(self):
        return Purchases.objects.all()


def view(request):
    q = Purchases.objects.all()
    total_sum = sum(q.values_list("amount", flat=True))

    return render(request, "form/view.html", context={"rows": q, "total": total_sum})


def insert(request):
    t = Types.objects.all()
    return render(request, "form/insert.html", context={"types_all": t})


def add(request):
    type_id = request.POST["b"]
    info = request.POST["info"]
    date = request.POST["date"]
    amount = request.POST["amount"]
    
    try:
        add = Purchases(
        day=date, amount=amount, info=info, types=Types.objects.get(pk=type_id)
    )
        add.save()
        message = "Запись добавлена успешно"
    
    except:
        message = "Ошибка добавления записи"