from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
from .models import article
from .forms import articleForm
api = "a261b0143330491ba79352a9cb4a0f29"


def index(request):

    form = articleForm(request.POST)

    if form.is_valid():
        form.save()
        form = articleForm()

        title   = request.POST.get('title')
        source  = request.POST.get('source')

        article.title   = title
        article.source  = source   

    context = {

        'form' : form

    }
    
    
    return render(request,"home.html",context)

def create(request):

    obj = article.objects.get(title = 'yico')
    
    title    = obj.title
    source   = obj.source

    url = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}".format(source,api)

    response = requests.get(url)

    jsondict = response.json()

    # newstitle = jsondict['articles'][2]['title']

    context = {

        'title'    : title,
        # 'newstitle': newstitle,
        'source'   : source
    }


    return render(request,"results.html",context)
