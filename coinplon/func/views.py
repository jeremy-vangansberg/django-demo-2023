from django.shortcuts import render
from .models import Functionnality
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class FunctionnalityListView(ListView):
    model = Functionnality
    template_name = "func/func_list.html"
    context_object_name = "func_list"

class FunctionnalityDetailView(DetailView):
    model = Functionnality
    template_name = "func/func_detail.html"

class FunctionnalityCreateView(CreateView, LoginRequiredMixin):
    model = Functionnality
    template_name = "func/func_create.html"
    fields = ["name", "description"] # == "__all__"
    success_url = reverse_lazy('func_list')