from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Character, Saga, Place

def accueil(request):
    return render(request, 'blog/accueil.html')

def character_list(request):
    characters = Character.objects.all()
    return render(request, 'blog/character_list.html', {'characters': characters})

def character_detail(request, id):
    character = Character.objects.get(id=id)
    return render(request, 'blog/character_detail.html', {'character': character})

def saga_list(request):
    sagas = Saga.objects.all()
    return render(request, 'blog/saga_list.html', {'sagas': sagas})

def saga_detail(request, id):
    saga = Saga.objects.get(id=id)
    return render(request, 'blog/saga_detail.html', {'saga': saga})

def place_list(request):
    places = Place.objects.all()
    return render(request, 'blog/place_list.html', {'places': places})

def place_detail(request, id):
    place = Place.objects.get(id=id)
    return render (request, 'blog/place_detail.html', {'place': place})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')
