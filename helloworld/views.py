from django.shortcuts import render,redirect , render_to_response   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from guestbook.models import TextMessage
import pytz,datetime

#def guestbook(request):
       # if 'ok' in request.POST:
        #        talker = request.POST['talker']
         #       message = request.POST['message']
          #      #local=pytz.timezone('Asia/Taipei')
        #     date_time=datetime.datetime.now()
                #local_dt=local.localize(date_time1,is_dst=None)
                #date_time=date_time1.replace(tzinfo=local)
         #       TextMessage.objects.create(talker=talker,message=message,date_time=date_time)
          #      msgs=TextMessage.objects.all()                        
        #msgs=TextMessage.objects.all()
        #return render(request, 'guestbookver1.html',locals())-->

#def index(request):
#	if 'search' in request.POST:
##		msgs=TextMessage.objects.filter(message__icontains=message)
#		return render(reqeust,'guestbookver1.html',locals())
#p       if 'ok' in request.POST:
 #       	talker = request.POST['talker']
  #              message = request.POST['message']
                #local=pytz.timezone('Asia/Taipei')
   #             date_time=datetime.datetime.now()
                #local_dt=local.localize(date_time1,is_dst=None)
                #date_time=date_time1.replace(tzinfo=local)
    #            TextMessage.objects.create(talker=talker,message=message,date_time=date_time)
     #           msgs=TextMessage.objects.all()                        
      #  msgs=TextMessage.objects.all()

#def homepage(request):
 #       return render(request,'homepage.html')


#def yang(request):
 #       buttonlist=['red','blue','green','yellow']
  #      return render(request,'yang.html',{'buttonlist':buttonlist})

#def hello(request):
 #       return render_to_response('hello.html')

#def login(request):
#	if request.user.is_authenticated:
#		return redirect('/guestbook')
#	username=request.POST.get('username','')
#	password=request.POST.get('password','')
#	user=auth.authenticate(username=username,password=password)
#	if user is not None and user.is_active:
#		auth.login(request,user)
#		mes='登入成功'
#		return redirect('/guestbook')		
#	else:
#		mes='尚未登入'
#		return render(request,"login.html",locals())
#def logout(request):
 #       auth.logout(request)
 #       return HttpResponseRedirect('/')

#def register(request):
#	if request.method=="POST":
#		username=request.POST['username']
#		password=request.POST['password']
#		email=request.POST['email']
#		firstname=request.POST['firstname']
#		lastname=request.POST['lastname']
#			user=None
#		
#		if user is not None:
#			msg="Username used by another"
#		else:
#			user=User.objects.create_user(username ,email, password )
#			user.first_name=firstname
#			user.last_name=lastname
#			user.save()
#			msg="You Had Registered Succeessfully!"
#			return render(request , "homepage.html",locals())
#	return render(request , "register.html",locals()) 

#def adminsite(reqeust):
#	if 'edit' in request.POST:
#		idex=request.POST['idex']
#		message=request.POST['message']
#		newmessage=request.POST['newmessage']
#		TextMessage.objects.filter(id=idex,message=message).update(message=newmessage)
#		msgs=TextMessage.objects.all()
#		return render(request,'adminsite.html',locals())
#	if 'delete' in request.POST:
#		idex=request.POST['idex']
#		message=request.POST['message']
#		TextMessage.objects.filter(id=idex,message=message).delete()
#		msgs=TextMessage.objects.all()
#		return render(request,'adminsite.html',locals())
#	msgs=TextMessage.objects.all()
#	return render(request,'adminsite.html',locals())

def index(request):
    if 'search' in request.POST:
        message = request.POST['message']
        msgs=TextMessage.objects.filter(message__icontains=message)
        return render(request,'guestbookver1.html',locals())

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
    return render(request,'guestbookver1.html',locals())


def adminsite(request):
    if 'edit' in request.POST:
        idex=request.POST['idex']
        message=request.POST['message']
        newmessage=request.POST['newmessage']
        TextMessage.objects.filter(id=idex,message=message).update(message=newmessage)
        msgs=TextMessage.objects.all()
        return render(request,'adminsite.html',locals())
    if 'delete' in request.POST:
        idex=request.POST['idex']
        message=request.POST['message']
        TextMessage.objects.filter(id=idex,message=message).delete()
        msgs=TextMessage.objects.all()
        return render(request,'adminsite.html',locals())
    msgs=TextMessage.objects.all()
    return render(request,'adminsite.html',locals())

def homepage(request):
    return render(request,'homepage.html')


def yang(request):
    buttonlist=['red','blue','green','yellow']
    return render(request,'yang.html',{'buttonlist':buttonlist})

def hello(request):
    return render_to_response('hello.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/index')
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None and user.is_active:
        auth.login(request,user)
        mes='登入成功'
        return redirect('/index')
		
    else:
        mes='尚未登入'
        return render(request,"login.html",locals())
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        try:
            user = User.objects.get(username=username)
        except:
            user=None
		
        if user is not None:
            message="Username used by another"
        else:
            user=User.objects.create_user(username ,email, password )
            user.first_name=firstname
            user.last_name=lastname
            user.save()
            message="You Had Registered Succeessfully!"
            return render(request , "homepage.html",locals())
    return render(request , "register.html",locals()) 
        