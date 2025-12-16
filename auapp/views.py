from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from random import choice
from django.core.mail import send_mail


# Create your views here.
def home(request):
	if request.user.is_authenticated:
		msg = "Welcome "+ str(request.user.username)
		return render(request,"home.html",{'msg':msg})
	else:
		return redirect("ulogin")

def usignup(request):
	if request.user.is_authenticated:
		msg = "Welcome "+str(request.user.username)
		return render(request,"home.html",{'msg':msg})
	elif request.method == "POST":
		un = request.POST.get("un")
		try:
			usr = User.objects.get(username=un)
			msg = un + " already registered"
			return render(request,"usignup.html",{'msg':msg})
		except User.DoesNotExist:
			text = "abcdefghijklmnopqrstuvwxyz"
			text = text + text.upper()
			text = text + "0123456789"
			text = text + "{}#^$@%*()<>"
			txt = list(text)

			pw = ""
			for i in range(8):
				pw = pw + choice(txt)
		
			print(pw)
			subject = "Welcome to kamal classes"
			msg = "Your password is "+ str(pw)
			from_email = "classeskamalsir@gmail.com"
			to_email=[str(un)]
			send_mail(subject,msg,from_email,to_email)
			usr = User.objects.create_user(username=un,password=pw)
			usr.save()
			return redirect("ulogin")
	else:
		return render(request,"usignup.html")
			

def ulogin(request):
	if request.user.is_authenticated:
		msg = "Welcome "+str(request.user.username)
		return render(request,"home.html",{'msg':msg})
	elif request.method=="POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		usr = authenticate(username=un,password=pw)
		if usr is None:
			msg = "Invalid login"
			return render(request,"ulogin.html",{'msg':msg})
		else:
			login(request,usr)
			return redirect("home")
	else:
		return render(request,"ulogin.html")

def ulogout(request):
	logout(request)
	return redirect("ulogin")
