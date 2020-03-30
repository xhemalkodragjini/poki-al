from django import forms
from django.forms import RadioSelect
from .models import TestModel

question_choices = (
    ("0", "Po"),
    ("1", "Jo")
)

question_choices2 = (
    ("1", "Po"),
    ("0", "Jo")
)


class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = '__all__'
        labels = {
            'a1': 'Degjon shpesh zhurma qe te tjeret nuk i degjojne',
            'a2': 'Shpesh perqendrohet ne te gjithe pikturen se sa ne detaje te vecanta',
            'a3': 'E ka te lehte te beje disa gjera ne te njejten kohe',
            'a4': "Mund t'i rikthehet aktivitetit qe po kryente edhe nese ka nje nderprerje nga dikush apo dicka",
            'a5': 'E ka te lehte te nenkuptoje dicka qe dikush i thote',
            'a6': 'E dallon nese dikush po merzitet nga biseda qe ai/ajo po ben',
            'a7': 'Kur lexon nje history, e ka te veshtire te kuptoje qellimet e personazheve',
            'a8': 'I pelqen te mbledhe informacion per kategorine e dickaje (lloji i makines, lloji i kafshes, bimes, '
                  'etj.',
            'a9': 'E ka te lehte te kuptoje cfare dikush po mendon apo ndjen, nga mimika e tij/saj',
            'a10': 'E ka te veshtire te kuptoje qellimet e njerezve',
            'verdheza': 'Shenja te verdhezes: ',
            'family': 'Familar/I aferm me autizem'
        }
        widgets = {
            'a1': RadioSelect,
            'a2': RadioSelect,
            'a3': RadioSelect,
            'a4': RadioSelect,
            'a5': RadioSelect,
            'a6': RadioSelect,
            'a7': RadioSelect,
            'a8': RadioSelect,
            'a9': RadioSelect,
            'a10': RadioSelect,
            'gjinia': RadioSelect,
            'etnia': forms.HiddenInput(),
            'verdheza': RadioSelect,
            'family': RadioSelect
        }

    def clean(self, *args, **kwargs):
        for i in range(10):
            name = "a" + str(i)
            name = self.cleaned_data.get(str(name))
        gjinia = self.cleaned_data.get('gjinia')
        mosha_ne_muaj = self.cleaned_data.get('mosha ne muaj')
        etnia = self.cleaned_data.get('etnia')
        verdheza = self.cleaned_data.get('verdheza')
        family = self.cleaned_data.get('family')
