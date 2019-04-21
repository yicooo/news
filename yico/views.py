from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
from .models import article
from .forms import articleForm
api = "a261b0143330491ba79352a9cb4a0f29"


def index(request):

    form = articleForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = articleForm()
          
    # url = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}".format(source,api)

    # response = requests.get(url)

    # jsondict = response.json()

    # newstitle = jsondict['articles'][2]['title']



    context = {

        'form' : form,
        #'title'    : title,
        # 'newstitle': newstitle,
        #'source'   : source

    }
    
    
    return render(request,"home.html",context)

def create(request):

    title = 'selam'
    source = request.GET.get('q',' ')
    newstitle = 'selam'

    url = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}".format(source,api)

    response = requests.get(url)

    jsondict = response.json()

    newstitle = jsondict['articles'][2]['title']

    context = {

        'title'     : title,
        'source'    : source,
        'newstitle' : newstitle
        
    }


    return render(request,"results.html",context)
