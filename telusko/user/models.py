from django.db import models

# Create your models here.
class Userdetails(models.Model):
	username=models.CharField(max_length=60)
	userage=models.IntegerField(blank=True,null=True)
	usergender=models.CharField(max_length=20,blank=True,null=True)
	email=models.EmailField()
	usercity=models.CharField(max_length=50,blank=True,null=True)
	loginpsw=models.CharField(max_length=50)