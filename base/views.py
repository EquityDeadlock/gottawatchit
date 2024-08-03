from django.shortcuts import render
from django.http import HttpResponse
from .models import Media

def index(request) -> HttpResponse:
    query = Media.objects.all()
    context = {'medias' : query}
    return render(request, 'base/index.html', context)

def content(request, id) -> HttpResponse:
    query = Media.objects.get(id=id) 
    context = {'media': query}
    return render(request, 'base/content.html', context)

def register(request) -> HttpResponse:
    return render(request, 'base/register.html')
