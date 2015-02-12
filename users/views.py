from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
# Create your views here.

def index(request):
	if request.user.is_authenticated():
		return redirect('home')
	return render(request, 'users/index.html')

@login_required
def home(request):
	return render(request, 'users/home.html',
		{
			'username': request.user.username,
			'email': request.user.email
		}
	)

@login_required
def profile(request):
	pass

@login_required
def edit_profile(request):
	return HttpResponse("welcome new user")

@login_required
def signout(request):
	logout(request)
	return redirect('index')

def auth_error(request):
	return render(request, 'auth_error.html')
