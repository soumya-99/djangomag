from django.urls import path
from . import views

urlpatterns = [
    path('', views.ImportPage, name='index'),
    path('', views.ImageRetrieve, name='imgs'),
    path('rommorochona/', views.RommoRochona, name='rommo'),
    path('winter/', views.Winter, name='winter'),
    path('spring/', views.Spring, name='spring'),
    path('rainy/', views.Rainy, name='rain'),
    path('puja/', views.Puja, name='puja'),
    path('special/', views.Special, name='special'),
    path('stories/', views.Stories, name='stories'),
    path('poems/', views.Poems, name='poems'),
    path('form/', views.Admin_Form, name='imp_page'),
    path('imageform/', views.Image_Form, name='imageform'),
]