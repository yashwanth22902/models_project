from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topics(request):
    QLTO =Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',context=d)

def display_Webpage(request):
    QLWO=Webpage.objects.all()
    d={'Webpage':QLWO}
    return render(request,'display_Webpage.html',context=d)

def display_AcessRecord(request):
    QLAO=AcessRecord.objects.all()
    d={'AcessRecord':QLAO}
    return render(request,'display_AcessRecord.html',d)

