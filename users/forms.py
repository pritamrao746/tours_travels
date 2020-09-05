
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from phone_field import PhoneField


class UserRegisterForm(UserCreationForm):
	username = forms.CharField(label='Your name')
	first_name = forms.CharField(help_text='First name')
	last_name=forms.CharField()
	email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}) ,help_text='Enter a valid email address') 
	password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),label='password')
	password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'confirm password'}),label='confirm password')
	# phone = forms.CharField(help_text='Phone number')
	class Meta(UserCreationForm.Meta):
		model = User
		fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
		