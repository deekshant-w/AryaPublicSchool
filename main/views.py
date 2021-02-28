from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from main import models as M
from django.db.models import Q
from django.views.decorators.http import require_http_methods
import json

def landing(request):
	AdminControls = M.AdminControls.objects.all()
	data = {}
	admissionsOn = 0
	if(AdminControls):
		admissionsOn = 1
		data = AdminControls[0]
	return render(request, 'landing.html', {'data':data,'admissionsOn':admissionsOn})

def dkTemp(request):
	return render(request, 'dkTemp.html')

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
	print(news)
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


@require_http_methods(["POST"])
def pagesEndPoint(request):
	data = json.loads(request.body)
	if(data.get('safe',False)):
		data = M.newPage.objects.all().order_by('-displayDate')
		return JsonResponse(serializePages(data),safe=False)
	return JsonResponse({'a':'b'})