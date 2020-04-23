from django.shortcuts import render,redirect
from .forms import NewUserForm
from .models import Userdetails
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth

def login(request):
	if request.method=='POST':
		user1=request.POST['firstname']
		password=request.POST['password']
		user=Userdetails(username=user1,loginpsw=password)

		if user is not None:
			print("kanak");
			return redirect('/./');
		else:
			print("kaju");
			return redirect('login');		
	else:
		print("jaduu");
		return render(request,'user/loginpage.html')		
# Create your views here.
def register(request):
	if request.method=='POST':

		form=NewUserForm(request.POST)
	
		obj=Userdetails()
		obj.username=request.POST.get('username')
		obj.userage=request.POST.get('userage')
		obj.usergender=request.POST.get('usergender')
		obj.email=request.POST.get('email')
		obj.usercity=request.POST.get('usercity')
		obj.loginpsw=request.POST.get('loginpsw')
		obj.save()
		print('user created')
		return HttpResponseRedirect('/')
					
	else:		
	    form=NewUserForm()
	return render(request,'user/register.html',{'form':form})