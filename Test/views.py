import pickle
import pandas
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import TestForm
from .models import TestModel


def test_view(request):
    form = TestForm(request.POST or None)
    if form.is_valid():
        form.save()
        loaded_model = pickle.load(
            open('C:/Users/Kodragjini/Documents/Poki/Test/finalized_model.sav', 'rb'))
        qs = TestModel.objects.all().values('a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','gjinia', 'mosha_ne_muaj','etnia', 'verdheza','family')
        format_data = pandas.DataFrame(qs)
        results = loaded_model.predict(format_data)
        result = results[0]
        if result == 1:
            return HttpResponseRedirect('neg')
        else:
            return HttpResponseRedirect('pos')

    return render(request, 'test.html', {'form': form})


def res_positive_view(request):
    return render(request, 'positive.html')


def res_negative_view(request):
    return render(request, 'negative.html')
