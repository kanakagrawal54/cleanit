from django.db import models

# Create your models here.
class Drivedetails(models.Model):
	teamname=models.CharField(max_length=50)
	date=models.DateField()
	venue=models.CharField(max_length=100)
	body=models.TextField()

	def __str__(self):
		return self.teamname

class Allpastdrives(models.Model):
	teamname=models.CharField(max_length=50)
	date=models.DateField()
	venue=models.CharField(max_length=100)
	body=models.TextField()
	def __str__(self):
		return self.teamname

class Allfuturedrives(models.Model):
	teamname=models.CharField(max_length=50)
	date=models.DateField()
	venue=models.CharField(max_length=100)
	body=models.TextField()
	def __str__(self):
		return self.teamname
