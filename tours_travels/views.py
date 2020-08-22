from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome to our home page</h1>')