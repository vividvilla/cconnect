from django.contrib.auth.models import User

from models import Profile, Phone, Link, Department

class UserController:
	def __init__(self, user):
		self.user = user

	def add_link(self, data):
		new_link = Link(user=self.user, name=data.get('name'), url=data.get('url'))
		new_link.save()

	def add_phone(self, data):
		new_phone = Phone(user=self.user, phone=data.get('phone'))
		new_phone.save()

	def update_profile(self, data):
		self.user.username = data.get('username', self.user.username)
		self.user.first_name = data.get('first_name', self.user.first_name)
		self.user.last_name = data.get('last_name', self.user.last_name)
		self.user.save()

	def update_company_info(self, data):
		profile = Profile()
		profile.user = self.user
		print data.get('department')

		if data.get('personal_email'):
			profile.personal_email = data.get('personal_email')

		if data.get('designation'):
			profile.designation = data.get('designation')

		if data.get('department'):
			department = Department.objects.filter(id=data.get('department'))[0]
			profile.department = department

		if data.get('bio'):
			profile.bio = data.get('bio')

		if data.get('date_joined'):
			profile.date_joined = data.get('date_joined')

		profile.save()
