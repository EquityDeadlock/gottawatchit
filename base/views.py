from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Media
from .forms import MediaForm

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

def createMedia(request: HttpRequest) -> HttpResponse:
    form = MediaForm()
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/create_media.html', context)

def updateMedia(request: HttpRequest, id) -> HttpResponse:
    media = Media.objects.get(id=id)
    form = MediaForm(instance=media)

    if request.method == 'POST':
        form = MediaForm(request.POST, instance=media)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/update_media.html', context)

