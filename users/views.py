from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from forms import UserBasicProfileForm
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
	user = request.user
	basic_profile_form = UserBasicProfileForm(initial={
			'username': user.username,
			'email': user.email,
			'first_name': user.first_name,
			'last_name': user.last_name
		})

	if 'basic_profile_form' in request.POST:
		print 'submitted'
		basic_profile_form = UserBasicProfileForm(request.POST)
		if basic_profile_form.is_valid():
			return HttpResponse("updated")
		else:
			print 'invalid', basic_profile_form.errors

	return render(request, 'users/edit_profile.html', {
		'basic_profile_form' : basic_profile_form,
		'user' : user
		})

@login_required
def signout(request):
	logout(request)
	return redirect('index')

def auth_error(request):
	return render(request, 'auth_error.html')
