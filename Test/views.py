import pickle
from django.http import HttpResponseRedirect
from django.shortcuts import render
import os
from django.conf import settings

from .forms import TestForm
from .models import TestModel

model_path = os.path.join(settings.BASE_DIR, "Test", "m.sav")

def test_view(request):
    form = TestForm(request.POST or None)
    if form.is_valid():
        form.save()
        loaded_model = pickle.load(open(model_path, 'rb'))
        qs = TestModel.objects.all().values('a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7',
                                            'a8', 'a9', 'a10', 'mosha_ne_muaj','gjinia',
                                            'etnia', 'verdheza',
                                            'family')
        format_data = [list(item.values()) for item in qs]
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
