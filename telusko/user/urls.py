from django.urls import path
from . import views

urlpatterns=[
path('signup/',views.register, name='sigupuser'),
path('',views.login,name='login')
]