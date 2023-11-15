import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Types(models.Model):
    type_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.type_name
    

class Purchases(models.Model):
    day = models.DateTimeField()
    amount = models.FloatField()
    types = models.ForeignKey(Types, on_delete=models.CASCADE)
    info = models.CharField(max_length=200)
    
    def __str__(self):
        return self.info
    
 
t = [
    'Услуги',
    'Кэшбек',
    'Сантехника',
    'Материалы',
    'Работы'
]

for n, i in enumerate(t):
    n = Types(type_name=i)
    n.save()

m = Purchases(day = timezone.now(), amount = 100.1, types = Types.objects.get(pk = 21), info = 'test discription')
m.save()