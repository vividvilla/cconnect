from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from forms import UserBasicProfileForm, UserCompanyInfoForm, \
	UserLinksForm, UserPhoneForm
from controller import UserController

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
	return HttpResponse('welcome')

@login_required
def edit_profile(request):
	user = request.user
	controller = UserController(user)

	basic_profile_form = UserBasicProfileForm(initial={
			'username': user.username,
			'email': user.email,
			'first_name': user.first_name,
			'last_name': user.last_name
		})

	if hasattr(user, 'profile'):
		company_info_form = UserCompanyInfoForm(initial={
			'personal_email': user.profile.personal_email,
			'designation': user.profile.designation,
			'department': user.profile.department
		})
	else:
		company_info_form = UserCompanyInfoForm()

	add_link_form = UserLinksForm()
	user_links = user.link_set.all()
	add_phone_form = UserPhoneForm()
	user_phones = user.phone_set.all()

	if 'basic_profile_form' in request.POST:
		basic_profile_form = UserBasicProfileForm(request.POST)
		if basic_profile_form.is_valid():
			controller.update_profile(request.POST)
			return HttpResponse('updated')

	if 'company_info_form' in request.POST:
		company_info_form = UserCompanyInfoForm(request.POST)
		if company_info_form.is_valid():
			controller.update_company_info(request.POST)
			return HttpResponse('updated company info')

	if 'add_link_form' in request.POST:
		add_link_form = UserLinksForm(request.POST)
		if add_link_form.is_valid():
			controller.add_link(request.POST)
			return HttpResponse('added link')

	if 'add_phone_form' in request.POST:
		add_phone_form = UserPhoneForm(request.POST)
		if add_phone_form.is_valid():
			controller.add_phone(request.POST)
			return HttpResponse('added phone number')

	return render(request, 'users/edit_profile.html', {
		'basic_profile_form' : basic_profile_form,
		'company_info_form' : company_info_form,
		'add_link_form' : add_link_form,
		'add_phone_form' : add_phone_form,
		'user' : user,
		'links' : user_links,
		'phones' : user_phones
		})

@login_required
def signout(request):
	logout(request)
	return redirect('index')

def auth_error(request):
	return render(request, 'auth_error.html')
