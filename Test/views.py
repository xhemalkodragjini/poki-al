import pickle
import pandas as pd
import numpy as np
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import TestForm
from .models import TestModel


def test_view(request):
    form = TestForm(request.POST or None)
    if form.is_valid():
        form.save()
        loaded_model = pickle.load(open('m.sav', 'rb'))
        qs = TestModel.objects.all().values('a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7',
                                            'a8', 'a9', 'a10', 'mosha_ne_muaj','gjinia',
                                            'etnia', 'verdheza',
                                            'family')
        format_data = pd.DataFrame(qs)
        results = loaded_model.predict(format_data)
        result = results[-1]
        if result == 1:
            return HttpResponseRedirect('neg')
        elif result == 0:
            return HttpResponseRedirect('pos')
        else:
            return HttpResponseRedirect('/')

    return render(request, 'test.html', {'form': form})


def res_positive_view(request):
    return render(request, 'positive.html')


def res_negative_view(request):
    return render(request, 'negative.html')
