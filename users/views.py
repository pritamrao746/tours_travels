from django.shortcuts import render,redirect


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
	return render(request,'users/destination.html')

def search(request):
	return render(request,'users/destination.html')

