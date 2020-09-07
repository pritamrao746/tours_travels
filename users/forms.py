
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):

	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','class':'input-box'}),label='')
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name','class':'input-box'}),label='')
	last_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'input-box'}),label='')
	email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email','class':'input-box'}),label='') 
	password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'input-box'}),label='')
	password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password','class':'input-box'}),label='')
	# phone = forms.CharField(help_text='Phone number')
	class Meta(UserCreationForm.Meta):
		model = User
		fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
		