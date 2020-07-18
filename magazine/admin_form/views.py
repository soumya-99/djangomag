from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def ImportPage(request):
    context = {'ImportPage': All_Fields.objects.all().order_by('-id')}
    # contextLimit = {'ImportPage': All_Fields.objects.all().order_by('-id')[:5]}
    return render(request, 'essentials/index.html', context)

def Admin_Form(request):
    if (request.method == "GET"):
        form = AdminForm()
        return render(request, 'form/form_input.html', {'form': form})
    else:
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')

# def Image_Form(request):
#     if (request.method == "GET"):
#         form = ImageForm()
#         return render(request, 'form/image.html', {'form': form})
#     else:
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             img_obj = form.instance
#             return render(request, 'form/image.html', {'form': form, 'img_obj': img_obj})
#         else:
#             form = ImageForm()
#         return render(request, 'essentials/index.html', {'form': form})


def Image_Form(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'form/image.html', {'form': form})
    else:
        form = ImageForm()
    return render(request, 'form/image.html', {'form': form})



# def Image_Form(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'form/image.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = ImageForm()
#     return render(request, 'form/image.html', {'form': form})



def ImageRetrieve(request):
    if request.method == 'GET':
        # context = {'ImageRetrieve': Image.objects.all().order_by('-id')}
        Images = Image.objects.all().order_by('-id')
        return render(request,'essentials/index.html', {'imgs': Images})

# def ImageRetrieve(request):
#     img = Image.objects.filter(file_type='image').order_by('-id')
#     return render(request,'essentials/index.html',{"img":img})

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
