from django.shortcuts import render
from django.forms.widgets import EmailInput
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import  CreateUserForm, OrgForm
from .decorators import unauthenticated_user

from django.contrib.auth import get_user_model

from django_email_verification import send_email 
# from .forms import CutomerForm

# def index(request):
    
#     return render(request,'P1/register_index.html')
    
    
    
    
    
    
def sendEmail(request):
   password = request.POST.get('password')
   username = request.POST.get('username')
   email = request.POST.get('email')
   user = get_user_model().objects.create(username=username,password=password, email = email)
   send_email(user)
   return render(request,'confim_template.html')
    
def	RegisterPage(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            user.is_active = False
            
            send_email(user)
            
            messages.success(request,'Account was created for '+ username)
            return redirect('mydemo')
        
    context ={'form':form}
    return render(request, 'P1/register.html',context)


def mydemo(request):
    form = OrgForm()
    if request.method == 'POST':
        form = OrgForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
			
        print('test')
        
    context = {'form':form}
    
    return render(request,'P1/test.html',context)
        
        
@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
    #  getting this from the html page
		username = request.POST.get('username')    
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'P1/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

# @login_required(login_url='login')
def home(request):
    
	return render(request, 'P1/nav.html')

	
# Create your views here.
