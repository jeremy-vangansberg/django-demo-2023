from django.shortcuts import render
from .functions import mutiplicate_by_5

def home_page(request):

    weekdays = [
        'lundi',
        'mardi',
        'mercredi',
        'jeudi',
        'vendredi',
        'samedi',
        'dimanche'
    ]

    context = {
        'test' : mutiplicate_by_5(6),
        'weekdays' : weekdays
        }
    
    return render(request, 'main/home_page.html', context=context)
