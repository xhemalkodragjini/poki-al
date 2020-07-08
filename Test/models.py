from django.db import models

question_choices = (
    ("1", "Po"),
    ("0", "Jo")
)
question_choices2 = (
    ("1", "Po"),
    ("0", "Jo")
)

question_choices3 = (
    ("0", "Po"),
    ("1", "Jo")
)

gender_choices = (
    ("0", "Femer"),
    ("1", "Mashkull")
)


class TestModel(models.Model):
    a1 = models.CharField(max_length=128, choices=question_choices, blank=False, default= None)
    a2 = models.CharField(max_length=128, choices=question_choices3, blank=False, default= None)
    a3 = models.CharField(max_length=128, choices=question_choices3, blank=False, default= None)
    a4 = models.CharField(max_length=128, choices=question_choices3, blank=False, default= None)
    a5 = models.CharField(max_length=128, choices=question_choices3, blank=False, default= None)
    a6 = models.CharField(max_length=128, choices=question_choices3, blank=False, default= None)
    a7 = models.CharField(max_length=128, choices=question_choices, blank=False, default= None)
    a8 = models.CharField(max_length=128, choices=question_choices, blank=False, default= None)
    a9 = models.CharField(max_length=128, choices=question_choices3, blank=False, default= None)
    a10 = models.CharField(max_length=128, choices=question_choices, blank=False, default= None)
    mosha_ne_muaj = models.CharField(max_length=3, blank=False, default=None)
    gjinia = models.CharField(max_length=128, choices=gender_choices, blank=False, default=None)
    etnia = models.IntegerField(default=5)
    verdheza = models.CharField(max_length=128, choices=question_choices2, blank=False, default= None)
    family = models.CharField(max_length=128, choices=question_choices2, blank=False, default= None)
