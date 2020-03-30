import pickle
import pandas
from django.shortcuts import render

from .forms import TestForm


def test_view(request):
    form = TestForm
    loaded_model = pickle.load(open('C:/Users/Kodragjini/Documents/Autistic/AutisticProject/AutisticTest/finalized_model.sav', 'rb'))

    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            result_data = form.cleaned_data
            format_data = pandas.DataFrame(result_data, index=[1])
            result = loaded_model.predict(format_data)
            final_result = None
            if result == 1:
                final_result = "Rezultatet e testit parashikojne shenja te spektrit te autizmit. Ju keshillojme te " \
                               "konsultoheni me nje mjek specialist. "
            else:
                final_result = "Rezultatet e testit nuk parashikojne shenja te spektrit te autizmit. "
            return render(request, 'test.html', {'result': final_result})

    return render(request, 'test.html', {'form': form})
