from django.http import Http404, HttpRequest
from django.shortcuts import render
from .models import client

# Create your views here.

def checklocale(domain):
    eng = '.com'
    no  = '.no'

    if domain.endswith(eng):
        return 'en-US'
    else:
        return 'nb-NO'

def index(request):
    locale = checklocale(request.get_host()),
    return render(request, 'index.html', {
        'page': client.entries({'content_type': 'page', 'fields.slug': 'index', 'locale': locale})[0],
        'nav': client.entries({'content_type': 'menu', 'locale': locale})
    })

def page(request, slug):
    try:
        locale = checklocale(request.get_host()),
        page = client.entries({
            'content_type': 'page', 'fields.slug': slug, 'locale': locale})[0]
        return render(request, 'page.html', {
            'page': page,
            'nav': client.entries({'content_type': 'menu', 'locale': 'nb-NO'})
        })
    except IndexError:
        raise Http404()
