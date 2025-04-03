from django.http import HttpResponseRedirect
from django.shortcuts import render
import os
from django.conf import settings
import onnxruntime as ort

from .forms import TestForm
from .models import TestModel

model_path = os.path.join(settings.BASE_DIR, "Test", "model.onnx")

def test_view(request):
    form = TestForm(request.POST or None)
    if form.is_valid():
        form.save()
                
        # Load the ONNX model
        session = ort.InferenceSession(model_path)

        qs = TestModel.objects.values(
            'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10',
            'mosha_ne_muaj', 'gjinia', 'etnia', 'verdheza', 'family'
        ).last()

        format_data = [list(qs.values())]
        
        # Run inference
        results = session.run(None, {'input': format_data})

        result = results[0][0]
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
