from django.db import models

question_choices = (
    ("0", "Po"),
    ("1", "Jo")
)

question_choices2 = (
    ("1", "Po"),
    ("0", "Jo")
)

gender_choices = (
    ("", ""),
    ("1", "Mashkull"),
    ("0", "Femer")
)


class TestModel(models.Model):
    a1 = models.CharField(max_length=128, choices=question_choices)
    a2 = models.CharField(max_length=128, choices=question_choices)
    a3 = models.CharField(max_length=128, choices=question_choices)
    a4 = models.CharField(max_length=128, choices=question_choices)
    a5 = models.CharField(max_length=128, choices=question_choices)
    a6 = models.CharField(max_length=128, choices=question_choices)
    a7 = models.CharField(max_length=128, choices=question_choices)
    a8 = models.CharField(max_length=128, choices=question_choices)
    a9 = models.CharField(max_length=128, choices=question_choices)
    a10 = models.CharField(max_length=128, choices=question_choices)
    gjinia = models.CharField(max_length=128, choices=gender_choices, default="")
    mosha_ne_muaj = models.IntegerField()
    etnia = models.IntegerField(default=5)
    verdheza = models.CharField(max_length=128, choices=question_choices2)
    family = models.CharField(max_length=128, choices=question_choices2)
