from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import TextMessage

def index(request):
	t1= TextMessage.objects.create(talker="Nick",message="Hi,Yang!")
	t2= TextMessage.objects.create(talker="Yang",message="Hi!Nick")
	t3= TextMessage.objects.create(talker="Swai",message="Hey GUYS!")
	msgs= TextMessage.objects.all()
	return render(request, 'guestbookver1.html',locals())

def yang(request):
        buttonlist=['red','blue','green','yellow']
        return render(request,'yang.html',{'buttonlist':buttonlist})

