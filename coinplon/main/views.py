from django.shortcuts import render
from .functions import mutiplicate_by_5
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserCreationFormCustom

def home_page(request):
    return render(request, 'main/home_page.html')

def about(request):
    # import pudb; pu.db()
    return render(request, 'main/about.html')

@login_required
def special_view(request):
    return render(request, 'main/special_view_page.html')

class SignupPage(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    form_class = UserCreationFormCustom
    
