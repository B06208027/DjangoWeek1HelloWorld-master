from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import TextMessage
import pytz,datetime

def index(request):
        if 'ok' in request.POST:
                talker = request.POST['talker']
                message = request.POST['message']
                #local=pytz.timezone('Asia/Taipei')
                date_time=datetime.datetime.now()
                #local_dt=local.localize(date_time1,is_dst=None)
                #date_time=date_time1.replace(tzinfo=local)
                TextMessage.objects.create(talker=talker,message=message,date_time=date_time)
                msgs=TextMessage.objects.all()                        
        msgs=TextMessage.objects.all()
        return render(request, 'guestbookver1.html',locals())

def yang(request):
        buttonlist=['red','blue','green','yellow']
        return render(request,'yang.html',{'buttonlist':buttonlist})
