from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Department(models.Model):
	name = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	department = models.ForeignKey(Department)
	position = models.CharField(max_length=100)
	updated = models.DateTimeField(auto_now=True)

class UserLink(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=20)
	url = models.URLField()
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)

class UserPhone(models.Model):
	user = models.ForeignKey(User)
	phone = models.IntegerField(max_length=10, unique=True,
		validators=[RegexValidator(regex='^\d{10}$',
			message='Invalid phone number',
			code='Invalid number')])
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
