from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def ImportPage(request):
    context = {'ImportPage': All_Fields.objects.all().order_by('-id')}

    # contextLimit = {'ImportPage': All_Fields.objects.all().order_by('-id')[:5]}
    return render(request, 'essentials/index.html', context)

def ImageRetrieve(request):
    Images = Image.objects.all()
    return render(request,'essentials/index.html', {'Images': Images})

def Stories(request):
    context = {'Stories': All_Fields.objects.filter(content_type=2).order_by('-id')}
    return render(request, 'essentials/golpo.html', context)

def Poems(request):
    context = {'Poems': All_Fields.objects.filter(content_type=1).order_by('-id')}
    return render(request, 'essentials/kobita.html', context)

def RommoRochona(request):
    context = {'RommoRochona': All_Fields.objects.filter(content_type=3).order_by('-id')}
    return render(request, 'essentials/rommorochona.html', context)

def Winter(request):
    context = {'Winter': All_Fields.objects.filter(edition=1)}
    return render(request, 'archives/winter.html', context)

def Spring(request):
    context = {'Spring': All_Fields.objects.filter(edition=2)}
    return render(request, 'archives/spring.html', context)

def Rainy(request):
    context = {'Rainy': All_Fields.objects.filter(edition=3)}
    return render(request, 'archives/rain.html', context)

def Puja(request):
    context = {'Puja': All_Fields.objects.filter(edition=4)}
    return render(request, 'archives/puja.html', context)

def Special(request):
    context = {'Special': All_Fields.objects.filter(edition=5)}
    return render(request, 'archives/special.html', context)
