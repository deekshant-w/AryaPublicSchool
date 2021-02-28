from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    return render(request, 'landing.html')

def dkTemp(request):
    return render(request, 'dkTemp.html')

def dynamicPage(request, p):
	print(p)
	return render(request, 'dynamicPage.html')

def notice(request):
	return render(request, 'notice.html')

def information(request):
	return render(request, 'information.html')

def activitiesPage(request):
    return render(request, 'activitiesPage.html')

def admissionPage(request):
    return render(request, 'admissionPage.html')
