from django.shortcuts import render,HttpResponse
from . import mail as mail_f

def home(request):
    return HttpResponse('<h1>Welcome to our home page</h1>')

def mail(request):
	mail_f.verification_mail()
	return HttpResponse('<h1>mail is sent</h1>')
