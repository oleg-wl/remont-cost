import datetime

from django.db import models

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
