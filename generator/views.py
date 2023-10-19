from django.shortcuts import render
import random

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    thepassword = ""

    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+=-'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')
