from django.urls import path
from . import views

urlpatterns=[
path('index/',views.index, name='hom'),
path('createteam/',views.createteam,name='createteam'),
path('',views.home,name='homepage'),
path('search/',views.search,name="jointeam"),
path('profilepage/',views.profilepage,name='profile'),
path('profilepage/pastdrive/',views.pastdrive, name='pastdrive'),
path('profilepage/futuredrive/',views.futuredrive,name='futuredrive')
]