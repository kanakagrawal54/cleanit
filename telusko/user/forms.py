from django import forms

class NewUserForm(forms.Form):
	username=forms.CharField(label='User Name', max_length=50, widget=forms.TextInput(attrs={'placeholder':"Enter your name."}))
	email=forms.EmailField(label='Email',max_length=50,widget=forms.TextInput(attrs={'placeholder':"Enter your Email."}))
	loginpsw=forms.CharField(label='Password',max_length=50,help_text="Password should be 8 letter long.",widget=forms.PasswordInput(attrs={'placeholder':"Password should be 8 letter long."}))
	confirmpsw=forms.CharField(label="Confirm password",max_length=50,widget=forms.TextInput(attrs={'placeholder':"Re-enter the password."}))