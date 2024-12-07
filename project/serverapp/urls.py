from django.urls import path
from . import views

urlpatterns = [
    path('power-calculator/', views.power_calculator, name='power_calculator'),
]

