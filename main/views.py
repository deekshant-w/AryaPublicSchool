from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    return render(request, 'landing.html')

def dkTemp(request):
    return render(request, 'dkTemp.html')
