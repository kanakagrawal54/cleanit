from django.shortcuts import render,redirect
from .forms import NewUserForm
from .models import Userdetails
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
def login(request):
	if request.method=='POST':

		user1=request.POST['firstname']
		password=request.POST['password']
		user =authenticate(username=user1,password=password)
		if user is not None:
			print("kanak");
			#print(user.username)
			return redirect('sigupuser');
		else:
			messages.info(request,"Login id or password is incorrect");
			print("kaju");
			return redirect('login');		
	else:
		print("jaduu");
		return render(request,'user/loginpage.html')		
# Create your views here.
def register(request):
	if request.method=='POST':

		form=NewUserForm(request.POST)
	
		
		name=request.POST.get('username')
		
		#obj.userage=request.POST.get('userage')
		#obj.usergender=request.POST.get('usergender')
		email=request.POST.get('email')
		#obj.usercity=request.POST.get('usercity')
		password=request.POST.get('loginpsw')
		confirm_psw=request.POST.get('confirmpsw')
		if User.objects.filter(username=name).exists():
			messages.error(request,"Username already exist :( try other")
			return redirect('sigupuser')
		elif password!=confirm_psw:
			messages.error(request,"Password and confirm password are different :(")
			return redirect('sigupuser')
		else:
			user=User.objects.create_user(name,email,password)
			user.save()
			print('user created')
			return redirect('login');
					
	else:		
	    form=NewUserForm()
	return render(request,'user/register.html',{'form':form})