from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_view, name='test'),
    path('pos', views.res_positive_view, name='positive'),
    path('neg', views.res_negative_view, name='negative'),
]
