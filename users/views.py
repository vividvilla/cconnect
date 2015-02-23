from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from forms import UserBasicProfileForm, UserProfileForm, \
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
	anchor = ''
	success = False

	basic_profile_form = UserBasicProfileForm(initial={
		'username': user.username,
		'email': user.email,
		'first_name': user.first_name,
		'last_name': user.last_name})

	if hasattr(user, 'profile'):
		profile_form = UserProfileForm(initial={
			'personal_email': user.profile.personal_email,
			'designation': user.profile.designation,
			'department': user.profile.department,
			'bio': user.profile.bio,
			'date_joined': user.profile.date_joined
		})
	else:
		profile_form = UserProfileForm()

	add_link_form = UserLinksForm()
	user_links = user.link_set.all()
	add_phone_form = UserPhoneForm()
	user_phones = user.phone_set.all()

	if 'basic_profile_form' in request.POST:
		anchor = '#basic-profile'
		basic_profile_form = UserBasicProfileForm(request.POST)
		if basic_profile_form.is_valid():
			success = True
			controller.update_profile(request.POST)

	if 'profile_form' in request.POST:
		anchor = '#other-profile'
		profile_form = UserProfileForm(request.POST)
		if profile_form.is_valid():
			success = True
			controller.update_company_info(request.POST)

	if 'add_link_form' in request.POST:
		anchor = '#social-links'
		add_link_form = UserLinksForm(request.POST)
		if add_link_form.is_valid():
			success = True
			controller.add_link(request.POST)

	if 'add_phone_form' in request.POST:
		anchor = '#phone-no'
		add_phone_form = UserPhoneForm(request.POST)
		if add_phone_form.is_valid():
			success = True
			controller.add_phone(request.POST)

	return render(request, 'users/edit_profile.html', {
		'basic_profile_form': basic_profile_form,
		'profile_form': profile_form,
		'add_link_form': add_link_form,
		'add_phone_form': add_phone_form,
		'user': user,
		'links': user_links,
		'phones': user_phones,
		'anchor': anchor,
		'success': success
	})


@login_required
def delete_profile_data(request):
	data_type = request.GET.get('data-type', '')
	data_id = request.GET.get('data-id', '')

	print data_type, data_id
	forbidden_resource = True
	items = []

	if data_type == 'link':
		items = request.user.link_set.all()
	elif data_type == 'phone':
		items = request.user.phone_set.all()

	print items
	for item in items:
		print item.id, data_id, type(item.id), type(data_id)
		if item.id == int(data_id):
			forbidden_resource = False
			item.delete()

	if forbidden_resource:
		return HttpResponse(status=403)
	else:
		return HttpResponse(status=204)


@login_required
def signout(request):
	logout(request)
	return redirect('index')


def auth_error(request):
	return render(request, 'auth_error.html')
