from django.shortcuts import render
from .models import Functionnality
from django.views.generic import ListView

class FunctionnalityListView(ListView):
    model = Functionnality
    template_name = "func/func_list.html"
    context_object_name = "func_list"
