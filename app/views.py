from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
from django.db.models import Q

def display_topics(request):
    QLTO =Topic.objects.all()
    QLTO=Topic.objects.all().order_by('topic_name')
    d={'topics':QLTO}
    return render(request,'display_topics.html',context=d)

def display_Webpage(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.filter(name__endswith='y')
    QLWO=Webpage.objects.filter(url__endswith='url')
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(Q(name__startswith='r')& Q(url__contains='h'))
    d={'Webpage':QLWO}
    return render(request,'display_Webpage.html',context=d)

def display_AcessRecord(request):
    QLAO=AcessRecord.objects.all()
    QLAO=AcessRecord.objects.all().order_by('-author')
    QLAO=AcessRecord.objects.all()
    d={'AcessRecord':QLAO}
    return render(request,'display_AcessRecord.html',d)







def update_Webpage(request):
    QLWO=Webpage.objects.all()
    d={'Webpage':QLWO}
    #Webpage.objects.filter(topic_name='cricket').update(name='Ben Stokes')
    #Webpage.objects.filter(topic_name='tennis').update(name='saniya mirza')
    #Webpage.objects.filter(topic_name='kabbadi').update(name='surender gill')
    #CTO=Webpage.objects.get_or_create(topic_name='cricket')[0]
    #CTO.save()
    #CTO=Webpage.objects.update_or_create(topic_name='cricket',defaults={'name':'dhoni'})
    QLWO=Webpage.objects.all()
    Webpage.objects.filter(topic_name='rubby').update(url='https://dan carter.com')
    Webpage.objects.filter(topic_name='cricket').update(url='https://ben.com')
    Webpage.objects.filter(name='saniya mirza').update(url='https://saniya.in')

    return render(request,'display_Webpage.html',d)

