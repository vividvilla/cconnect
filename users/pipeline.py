from models import Profile


def save_profile(backend, user=None, response={}, *args, **kwargs):
	try:
		profile = user.profile
	except Profile.DoesNotExist:
		profile = Profile()
		profile.user = user

	if backend.name == 'google-oauth2' and not profile.avatar:
		if not response['image']['isDefault']:
			profile.avatar = response['image']['url'].split('?')[0]
			profile.save()
