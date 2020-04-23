from django.db import models

# Create your models here.
class Userdetails(models.Model):
	username=models.CharField(max_length=60)
	userage=models.IntegerField()
	usergender=models.CharField(max_length=20)
	email=models.EmailField()
	usercity=models.CharField(max_length=50)
	loginpsw=models.CharField(max_length=50)