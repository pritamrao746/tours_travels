from django.shortcuts import render,HttpResponse

# Create your views here.

def itinerary(request):
    return HttpResponse('<h1>Create Itinerary</h1>')

def destination(request):
    return HttpResponse('<h1>Create destination</h1>')

def travel(request):
    return HttpResponse('<h1>Create travel</h1>')

def accomodation(request):
    return HttpResponse('<h1>Create accomodation</h1>')