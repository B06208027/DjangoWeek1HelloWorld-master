from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
        loop1={'name':'Yang','msg':'hi,my name is Yang'}
        loop2={'name':'Swai','msg':'hello!Nice to meet you,I am Swai'}
        mine=[loop1,loop2]
        return render(request, 'guestbookver1.html',locals())

def yang(request):
        buttonlist=['red','blue','green','yellow']
        return render(request,'yang.html',{'buttonlist':buttonlist})

