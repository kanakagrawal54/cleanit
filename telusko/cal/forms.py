from django import forms

class Newdrive(forms.Form):
	teamname=forms.CharField(label="Teamname",max_length=50)
	date=forms.DateField(label="Date")
	venue=forms.CharField(label='Venue',max_length=100)
	body=forms.CharField(label="Body",max_length=200)