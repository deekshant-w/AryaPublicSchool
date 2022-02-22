from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from main import models as M
from django.db.models import Q
from django.views.decorators.http import require_http_methods
import json
import datetime
from django.http import HttpResponseNotFound, HttpResponse

def landing(request):
	data = {}
	admissionsOn = False

	AdminControls = M.AdminControls.objects.all()
	if(AdminControls and AdminControls[0].admissionsOn):
		admissionsOn = True
		data['admission'] = AdminControls[0]

	noticeData = M.notice.objects.filter(archieve=False).order_by('-displayDate')
	data["noticeCount"] = M.notice.objects.count()
	try:
		data["notices"] = noticeData[:5]
	except:
		data["notices"] = []

	try:
		data["lastNotice"] = noticeData[0]
	except:
		data["lastNotice"] = False

	newsData = M.news.objects.filter(archieve=False).order_by('-displayDate')
	data["newsCount"] = M.news.objects.count()
	try:
		data["news"] = newsData[:5]
	except:
		data["news"] = []

	try:
		data['lastNews'] = newsData[0]
	except:
		data['lastNews'] = False

	data['carouselImages'] = M.CarouselImages.objects.all()

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
		responce = render(request, "404.html")
		responce.status_code = 404
		return responce

def notice(request):
	notices = M.notice.objects.filter(archieve=False).order_by('-displayDate')
	return render(request, 'notice.html', {'notices':notices})

def news(request):
	news = M.news.objects.filter(archieve=False).order_by('-displayDate')
	return render(request, 'news.html', {'information':news})

def activitiesPage(request):
	return render(request, 'activitiesPage.html')

def admissionPage(request):
	data = M.AdmissionPage.objects.all()
	if len(data):
		data = data[0].data
	else:
		data = ""
	return render(request, 'admissionPage.html', {'data':data})

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
