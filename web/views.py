from django.http import Http404, HttpRequest
from django.shortcuts import render
from .models import client

# FUNCTIONS

def checklocale(domain):
    eng = '.com'
    no  = '.no'

    if domain.get_host().endswith(eng):
        return 'en-US', 'en'
    else:
        return 'nb-NO', 'no'

def getnav(input):
    output = client.entries({
        'content_type': 'menu',
        'locale': checklocale(input)[0]
        })
    return output

def getindex(input):
    output = client.entries({
        'content_type': 'page',
        'fields.slug': 'index',
        'locale': checklocale(input)[0]
        })[0]
    return output

def getpage(input, slug):
    output = client.entries({
        'content_type': 'page',
        'fields.slug': slug,
        'locale': checklocale(input)[0]
        })[0]
    return output

def getsubpage(input, slug):
    output = client.entries({
        'content_type': 'subpage',
        'fields.slug': slug,
        'locale': checklocale(input)[0]
        })[0]
    return output

def getreference(input, slug):
    output = client.entries({
        'content_type': 'reference',
        'fields.slug': slug,
        'locale': checklocale(input)[0]
        })[0]
    return output

def getlisting(input, slug):
    output = client.entries({
        'content_type': 'listing',
        'fields.slug': slug,
        'locale': checklocale(input)[0]
        })[0]
    return output

def getperson(input, slug):
    output = client.entries({
        'content_type': 'person',
        'fields.slug': slug,
        'locale': checklocale(input)[0]
        })[0]
    return output

# VIEWS

def index(request):
    try:
        return render(request, 'index.html', {
            'page': getindex(request),
            'nav': getnav(request),
            'locale': checklocale(request)[0],
            'lang': checklocale(request)[1],
            'front': True
        })
    except IndexError:
        raise Http404()

def contact_en(request):
    try:
        return render(request, 'contact.html', {
            'page': getpage(request, 'contact'),
            'lang': checklocale(request)[1],
            'nav': getnav(request)
        })
    except IndexError:
        raise Http404()

def contact_no(request):
    try:
        return render(request, 'contact.html', {
            'page': getpage(request, 'kontakt'),
            'lang': checklocale(request)[1],
            'nav': getnav(request)
        })
    except IndexError:
        raise Http404()

def page(request, slug):
    try:
        return render(request, 'page.html', {
            'page': getpage(request, slug),
            'lang': checklocale(request)[1],
            'nav': getnav(request)
        })
    except IndexError:
        raise Http404()

def subpage(request, slug, parent):
    try:
        return render(request, 'subpage.html', {
            'page': getsubpage(request, slug),
            'parent' : getpage(request, parent),
            'lang': checklocale(request)[1],
            'nav': getnav(request)
        })
    except:
        pass
    try:
        return render(request, 'subpage.html', {
            'page': getreference(request, slug),
            'parent' : getpage(request, parent),
            'lang': checklocale(request)[1],
            'nav': getnav(request)
        })
    except:
        pass
    try:
        return render(request, 'subpage.html', {
            'page': getlisting(request, slug),
            'parent' : getpage(request, parent),
            'lang': checklocale(request)[1],
            'nav': getnav(request)
        })
    except IndexError:
        raise Http404()
