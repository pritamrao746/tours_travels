from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from adminside.models import *
from users.models import *
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
	dests=Destination.objects.all()[:4]
	packs=Package.objects.all().order_by('number_of_times_booked')[:3]
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


	context={'dests':dests,'packages':packages}
	
	return render(request,'users/index.html',context)

def destination(request,id):
	id=id
	dest=Destination.objects.get(id=id)
	packs=dest.package_set.all()
	nights=[]
	price=[]
	dtn_image_url_list = []
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


		# Getting the small image of a particular package related to some destination
		destination_img_object = i.destination.destinationimages_set.all()[0] #destination images object
		img = dtn_image_url_list.append(destination_img_object.small_image.url)
	
	
	packages=zip(packs,nights,price,travel,dtn_image_url_list)


	# Images For caraousel purpose
	images = dest.destinationimages_set.all()[0] #destination images object
	caraousel1 = images.caraousel1.url
	caraousel2 = images.caraousel2.url
	caraousel3 = images.caraousel3.url



	context={'dest':dest,'packages':packages,'caraousel1':caraousel1,'caraousel2':caraousel2,'caraousel3':caraousel3}
	
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
	if request.user.is_authenticated:
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

			# Images
			images = package.destination.destinationimages_set.all()[0] #destination images object
			package_image = images.caraousel1.url

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
					'itinerary_description':itinerary_description,
					'package_image':package_image
				}

		except:
			return HttpResponse('<H1> An error ocuured in Database , Please try later </H1>')


		return render(request,'users/package.html',context)
	else:
		return redirect('login')


def bookings(request):
	user_id=request.user.id
	context = {}
	if request.method == 'POST':
		user=user_id
		package=request.POST['package_id']
		package=Package.objects.get(pk=package)
		number_of_adults = request.POST['adults']
		number_of_children =request.POST['children']
		number_of_rooms =request.POST['rooms']
		booking_date=request.POST['date']
		include_travelling=request.POST.get('travel')
		if include_travelling:
			include_travelling=True
			total_amount=(package.adult_price * int(number_of_adults)) + (package.child_price * int(number_of_children)) + (package.travel.price_per_person *(int(number_of_adults)+int(number_of_children)))+(package.accomodation.price_per_room*int(number_of_rooms))
			print(total_amount)
		else:
			include_travelling=False
			total_amount=(package.adult_price * int(number_of_adults)) + (package.child_price * int(number_of_children)) + (package.accomodation.price_per_room*int(number_of_rooms))
			print(total_amount)
		bookings=UserBookings(user=request.user,package=package,number_of_adults=number_of_adults,number_of_children=number_of_children,number_of_rooms=number_of_rooms,booking_date=booking_date,include_travelling=include_travelling,paid=False,total_amount=total_amount)
		bookings.save()
		#ye users home abhi ke liye hai..iske jagah pe payment gatway daldena
		return redirect('users-home')
		#redirect to payment gateway
		#after successfull payment, save the value of paid as true in user bookings and then redirect to home page
		#and mail the package and booking-details to user
	else:
		return redirect('users-home')
	
     