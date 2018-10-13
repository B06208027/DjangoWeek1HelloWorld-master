from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import TextMessage
import datetime

def index(request):
        if 'ok' in request.POST:
                talker = request.POST['talker']
                message = request.POST['message']
                date_time=datetime.datetime.now()
                TextMessage.objects.create(talker=talker,message=message,date_time=date_time)
                msgs=TextMessage.objects.all()                        
        msgs=TextMessage.objects.all()
        return render(request, 'guestbookver1.html',locals())

def yang(request):
        buttonlist=['red','blue','green','yellow']
        return render(request,'yang.html',{'buttonlist':buttonlist})
