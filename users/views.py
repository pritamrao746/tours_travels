from django.shortcuts import render,redirect,HttpResponse
from adminside.models import *
from .forms import UserRegisterForm
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
	n=packs.count()
	nights=[]
	price=[]
	
	for i in packs:
		nights.append(i.number_of_days-1)
		price.append(i.adult_price+i.accomodation.price_per_room)
	
	packages=zip(packs,nights,price)
	

	context={'dest':dest,'packages':packages}
	return render(request,'users/destination.html',context)

def search(request):
	name=request.POST.get('search','')
	name=name.lstrip()
	name=name.rstrip()
	dest=Destination.objects.filter(city__icontains=name) | Destination.objects.filter(state__icontains=name) | Destination.objects.filter(city__icontains=name)	
	print(dest[0].id)
	return redirect('users-destination', id=dest[0].id)
	

