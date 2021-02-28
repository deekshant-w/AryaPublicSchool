from django.shortcuts import render
from django.http import HttpResponse
from main import models as M
from django.db.models import Q

def landing(request):
    return render(request, 'landing.html')

def dkTemp(request):
    return render(request, 'dkTemp.html')

def dynamicPage(request, p):
	print(p)
	return render(request, 'dynamicPage.html')

def notice(request):
	notices = M.notice.objects.filter(archieve=False).order_by('-displayDate')
	return render(request, 'notice.html', {'notices':notices})

def information(request):
	information = M.information.objects.filter(archieve=False).order_by('-displayDate')
	return render(request, 'information.html', {'information':information})

def activitiesPage(request):
    return render(request, 'activitiesPage.html')

def admissionPage(request):
    return render(request, 'admissionPage.html')
