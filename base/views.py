from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Media
from .forms import MediaForm
from .models import Tag
from .forms import TagForm

def index(request: HttpRequest) -> HttpResponse:
    q = request.GET.get('q')  
    if q:
        medias = Media.objects.filter(tags__name=q) 
    else:
        medias = Media.objects.all()
    tags = Tag.objects.all()
    context = {'medias' : medias, 'tags': tags}
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

def deleteMedia(request: HttpRequest, id) -> HttpResponse:
    media = Media.objects.get(id=id)
    if request.method == 'POST':
        media.delete()
        return redirect('home')
    context = {'obj': media}
    return render(request, 'base/delete.html', context)

def createTag(request: HttpRequest) -> HttpResponse:
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/create_tag.html', context)
