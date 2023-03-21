from django.shortcuts import render
from .functions import mutiplicate_by_5
from django.contrib.auth.decorators import login_required

def home_page(request):
    return render(request, 'main/home_page.html')

def about(request):
    # import pudb; pu.db()
    return render(request, 'main/about.html')

@login_required
def special_view(request):
    return render(request, 'main/special_view_page.html')
