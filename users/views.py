from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from adminside.models import *
from .forms import UserRegisterForm
from django.http import HttpResponseRedirect
from django.http import JsonResponse
# Create your views here.

def register(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		
		if form.is_valid():
			form.save()
			# print(form.cleaned_data.get('email'))
			# username=form.cleaned_data.get('')
			# messages.success(request,f'{username} your account is created!!')
			return redirect('login')

		# messages.error(request,f'invalid input')
		return render(request,'users/register.html',{'form':form})

	else:
		form=UserRegisterForm()
		return render(request,'users/register.html',{'form':form})
		
		
def home(request):
	return render(request,'users/index.html')


def package(request):
	return render(request,'users/package.html')

def destination(request,id):
	id=id
	dest=Destination.objects.get(id=id)
	packs=dest.package_set.all()
	nights=[]
	price=[]
	travel=[]
	
	for i in packs:
		nights.append(i.number_of_days-1)
		price.append(i.adult_price+i.accomodation.price_per_room)
		mode=i.travel.travelling_mode
		if(mode=="TN"):
			travel.append("Train")
		elif(mode=="FT"):
			travel.append("Flight")
		else:
			travel.append("Bus")
	
	packages=zip(packs,nights,price,travel)


	context={'dest':dest,'packages':packages}
	return render(request,'users/destination.html',context)

def search(request):
	try:
		name=request.POST.get('search','')
		name=name.lstrip()
		name=name.rstrip()
		dest=Destination.objects.filter(city__icontains=name) | Destination.objects.filter(state__icontains=name) | Destination.objects.filter(city__icontains=name)	
		print(dest[0].id)
		return redirect('users-destination', id=dest[0].id)
	except:
		messages.error(request, 'No results found for your search request')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		

def detail_package(request,package_id):

	try:
		package = Package.objects.get(pk=package_id)
		package_name = package.package_name
		destination_name = package.destination.name
		no_of_days = package.number_of_days
		destination_description = package.destination.dtn_description
		package_description = package.description

		# Travelling details
		travel_mode = package.travel.travelling_mode
		travel_price = package.travel.price_per_person

		# Accomodation Details
		hotel_name = package.accomodation.hotel_name
		hotel_description = package.accomodation.hotel_description
		price_per_room = package.accomodation.price_per_room

		# Inclusive
		inclusive = package.inclusive
		exclusive = package.exclusive

		# Itinerary
		itinerary = Itinerary.objects.get(package=package)
		itinerary_description = itinerary.itinerarydescription_set.all() # list of itineary days

		context = {
				'package':package,
				'package_name':package_name,
				'destination_name':destination_name,
				'no_of_days':no_of_days,
				'destination_description':destination_description,
				'package_description':package_description,
				'travel_mode':travel_mode,
				'travel_price':travel_price,
				'hotel_name':hotel_name,
				'hotel_description':hotel_description,
				'price_per_room':price_per_room,
				'inclusive':inclusive,
				'exclusive':exclusive,
				'itinerary_description':itinerary_description
			}

	except:
		return HttpResponse('<H1> An error ocuured in Database , Please try later </H1>')


	return render(request,'users/package.html',context)