import datetime
from django import forms

from .models import Types, Purchases

class BasicFolm(forms.Form):
    charfield = forms.CharField()
    intfield = forms.IntegerField()
    datefield = forms.DateField()

class InputForm(forms.ModelForm):
    day = forms.DateField(required=True, initial=datetime.datetime.today, label='Дата')
    amount = forms.FloatField(label='Сумма')
    types = forms.ModelChoiceField(queryset=Types.objects.all(),empty_label=None, label='Вид расхода')
    info = forms.CharField(label='Описание')

    class Meta:
        model = Purchases
        fields = '__all__'