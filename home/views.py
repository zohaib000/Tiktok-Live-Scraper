from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.http import JsonResponse
from .models import *
from django.http import JsonResponse
import time
from .scraper import searchLive

is_scraping=True

def check_ajax(r):
    if r.headers.get('X-Requested-With') == 'XMLHttpRequest':
        is_ajax = True
    else:
        is_ajax = False
    return is_ajax

class home(View):
    def get(self, request):
        return render(request, 'home/index.html')

# chrome profiles handling
class tiktok(View):
    def get(self,request):
        return render(request, 'home/tiktok.html')
    
    def post(self, request):
        global is_scraping
        # ? if request from ajax then we need to update the record
        if check_ajax(request):
            action=request.POST.get("action")
            if action=="start":
                is_scraping=True
                keyword=request.POST.get("keyword")
                searchLive(keyword)
                if is_scraping:
                   return JsonResponse({'status': "Data Scraped successfully!"})
            elif action=="stop":
                is_scraping=False
                return JsonResponse({'status': "Action Stopped ! Data Scrapped Successfully !"})

        # ? handle request to create new profiles
        return render(request, "home/tiktok.html", {"status": "Profiles successfully created !"})


def Contact(request):
    return render(request, 'home/contact.html')


def About(request):
    return render(request, 'home/about.html')


def Terms(request):
    return render(request, 'home/terms.html')
