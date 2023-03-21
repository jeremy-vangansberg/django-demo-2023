from django.shortcuts import render
from .forms import ApiForm
from requests import Request, Session
import os

def api_view(request):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': os.getenv('API_SECRET_KEY')
    }
    session = Session()
    session.headers.update(headers)
    info = None

    form = ApiForm(request.POST)
    if request.method == 'POST':
        if form.is_valid() :
            response = session.get(url, params=form.cleaned_data)
            info = response.text
    return render(request, 'api/api_page.html', context={
        'form': form,
        'info': info}
        )