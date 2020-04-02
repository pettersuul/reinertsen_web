from django.http import Http404, HttpRequest
from django.shortcuts import render
from .models import client

# Create your views here.

def checklocale(domain):
    eng = '.com'
    no  = '.no'

    if domain.get_host().endswith(eng):
        return 'en-US'
    else:
        return 'nb-NO'

def getnav(input):
    output = client.entries({
        'content_type': 'menu',
        'locale': checklocale(input)
        })
    return output

def getindex(input):
    output = client.entries({
        'content_type': 'page',
        'fields.slug': 'index',
        'locale': checklocale(input)
        })[0]
    return output

def getpage(input, slug):
    output = client.entries({
        'content_type': 'page',
        'fields.slug': slug,
        'locale': checklocale(input)
        })[0]
    return output

def getreference(input, slug):
    output = client.entries({
        'content_type': 'reference',
        'fields.slug': slug,
        'locale': checklocale(input)
        })[0]
    return output

def getpersons():
    output = client.entries({
        'content_type': 'person',
        'locale': 'nb-NO'
        })
    return output

def index(request):
    try:
        return render(request, 'index.html', {
            'page': getindex(request),
            'nav': getnav(request),
            'front': True
        })
    except IndexError:
        raise Http404()

def page(request, slug):
    try:
        return render(request, 'page.html', {
            'page': getpage(request, slug),
            'nav': getnav(request)
        })
    except IndexError:
        raise Http404()

def references_list(request):
    try:
        return render(request, 'reference_list.html', {
            'page': getpage(request, 'references'),
            'nav': getnav(request)
        })
    except IndexError:
        raise Http404()

def references_single(request, slug):
    try:
        return render(request, 'reference_single.html', {
            'page': getreference(request, slug),
            'nav': getnav(request)
        })
    except IndexError:
        raise Http404()

def contact(request):
    try:
        return render(request, 'contact.html', {
            'page': getpage(request, 'contact'),
            'nav': getnav(request)
        })
    except IndexError:
        raise Http404()
