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

def destination(request):
	id=2
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
	dest=Destination.objects.get(city__icontains=name) 
	# | Destination.objects.get(state__icontains=name) | Destination.objects.get(city__icontains=name)
	print(dest)
	return render(request,'users/destination.html')

