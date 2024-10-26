from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            tn=request.POST['tn']
            To=Topic.objects.get_or_create(topic_name=tn)
            return HttpResponse('topic name is successfully created')
        else:
            return HttpResponse('invalid data')
    
    return render(request,'insert_topic.html',d)
def insert_webpage(request):
    EWFO=Webpageform()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=Webpageform(request.POST)
        if WFDO.is_valid():
            tn=request.POST.get('topic_name')
            To=Topic.objects.get(topic_name=tn)
            n=request.POST['name']
            e=request.POST['email']
            u=request.POST['url']
            WO=Webpages.objects.get_or_create(topic_name=To,name=n,email=e,url=u)
            return HttpResponse('successfully inserted data into Webpage model')
        else:
            return HttpResponse('Invalid data')
    
    return render(request,'insert_webpage.html',d)
def display_webpage(request):
    d={'EFO':checkboxform()} 
    
    return render(request,'display_webpage.html',d)
    
