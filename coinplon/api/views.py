from django.shortcuts import render
from .forms import ApiForm
from requests import Request, Session

def api_view(request):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'YOUR_API_KEY'
    }

    form = ApiForm(request.POST)
    if request.method == 'POST':
        if form.is_valid() :
            print(form.cleaned_data)
    return render(request, 'api/api_page.html', context={'form': form})