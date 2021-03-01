from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from main import models as M
from django.db.models import Q
from django.views.decorators.http import require_http_methods
import json
import datetime

def landing(request):
	data = {}
	admissionsOn = False
	
	AdminControls = M.AdminControls.objects.all()
	if(AdminControls and AdminControls[0].admissionsOn):
		admissionsOn = True
		data['admission'] = AdminControls[0]

	noticeData = M.notice.objects.filter(archieve=False).order_by('-displayDate')
	data["notices"] = noticeData[:5]
	data["noticeCount"] = M.notice.objects.count()
	data["lastNotice"] = noticeData[0]
	
	newsData = M.news.objects.filter(archieve=False).order_by('-displayDate')
	data["news"] = newsData[:5]
	data["newsCount"] = M.news.objects.count()
	data['lastNews'] = newsData[0]

	return render(request, 'landing.html', {'data':data,'admissionsOn':admissionsOn})

def dkTemp(request):
	a = datetime.datetime.now() - datetime.timedelta(days=2,hours=2)
	return render(request, 'dkTemp.html',{'a':a})

def dynamicPage(request, p):
	p = p.lower().strip()
	page = M.newPage.objects.filter(archieve=False, url__in = [p,f'/{p}',f'{p}/',f'/{p}/'])
	if(page):
		return render(request, 'dynamicPage.html', {'page':page[0]})
	else:
		return HttpResponse("404 Page Not Found")

def notice(request):
	notices = M.notice.objects.filter(archieve=False).order_by('-displayDate')
	return render(request, 'notice.html', {'notices':notices})

def news(request):
	news = M.news.objects.filter(archieve=False).order_by('-displayDate')
	return render(request, 'news.html', {'information':news})

def activitiesPage(request):
	return render(request, 'activitiesPage.html')

def admissionPage(request):
	return render(request, 'admissionPage.html')

def serializePages(data):
	res = []
	for page in data:
		temp = {}
		if(page.url.startswith("/")):
			temp['url'] = page.url
		else:
			temp['url'] = "/"+page.url
		temp['heading'] = page.heading.title()
		res.append(temp)
	return res


@require_http_methods(["GET"])
def pagesEndPoint(request):
	data = M.newPage.objects.all().order_by('?')
	return JsonResponse(serializePages(data),safe=False)
