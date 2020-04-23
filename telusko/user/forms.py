from django import forms

class NewUserForm(forms.Form):
	username=forms.CharField(label='UserName', max_length=50)
	userage=forms.IntegerField(label='UserAge')
	usergender=forms.CharField(label='UserGender',max_length=20)
	email=forms.EmailField(label='UserEmail')
	usercity=forms.CharField(label='UserCity',max_length=50)
	loginpsw=forms.CharField(label='UserPassword',max_length=50)