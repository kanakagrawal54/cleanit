from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Drivedetails, Allpastdrives, Allfuturedrives
from .forms import Newdrive
from django.contrib.auth.models import User, auth
from django.utils.timezone import datetime
from datetime import date
# Create your views here.
def home(request):
	return render(request,'cal/homenew.html');

def index(request):
	searchresult=request.GET.get('searchbar').lower()
	#postlist=Drivedetails.objects.filter(venue__contains=searchresult)
	postlist= [item for item in Drivedetails.objects.all() if searchresult in item.teamname.lower() or searchresult in item.venue.lower()]
	return render(request,'cal/drivevenueselected.html',{'posts':postlist});	
def search(request):
	postlist=Drivedetails.objects.all()
	return render(request,'cal/driveinfo.html',{'posts':postlist});


def createteam(request):
	if request.method=='POST':
		form=Newdrive(request.POST)
		teamname=request.POST.get('teamname')
		venue=request.POST.get('venue')
		date=request.POST.get('date')
		body=request.POST.get('body')
		obj=Drivedetails.objects.create(teamname=teamname,venue=venue,body=body,date=date)
		obj.save()
		obj=Allfuturedrives.objects.create(teamname=teamname,venue=venue,body=body,date=date)
		obj.save()
		return redirect('./')
	else:
		form=Newdrive()
		return render(request,'cal/createteampage.html',{'form':form})

def profilepage(request):
	postlist=Drivedetails.objects.all()
	post=[]
	for i in range(3):
		post.append(postlist[i]);
	return render(request,'cal/profile.html',{'posts':post});
def pastdrive(request):
	postlist=Allfuturedrives.objects.filter(date__lte=date.today())
	for event in postlist:
		obj=Allpastdrives.objects.create(teamname=event.teamname,venue=event.venue,date=event.date,body=event.body)
		obj.save()
		Allfuturedrives.objects.filter(date__lte=date.today()).delete()	
	postlist=Allpastdrives.objects.all()
	return render(request,'cal/pastdrive.html',{'posts':postlist});
def futuredrive(request):
	postlist=Allfuturedrives.objects.filter(date__lte=date.today())
	for event in postlist:
		obj=Allpastdrives.objects.create(teamname=event.teamname,venue=event.venue,date=event.date,body=event.body)
		obj.save()
	Allfuturedrives.objects.filter(date__lte=date.today()).delete()	
	postlist=Allfuturedrives.objects.all()
	return render(request,'cal/futuredrive.html',{'posts':postlist});	