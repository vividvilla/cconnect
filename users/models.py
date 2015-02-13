from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Department(models.Model):
	name = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

class Profile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	bio = models.TextField(null=True, blank=True)
	personal_email = models.EmailField(max_length=224, null=True, blank=True)
	department = models.ForeignKey(Department, null=True, blank=True)
	designation = models.CharField(max_length=100, null=True, blank=True)
	updated = models.DateTimeField(auto_now=True)

class Link(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=20)
	url = models.URLField()
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)

class Phone(models.Model):
	user = models.ForeignKey(User)
	phone = models.CharField(max_length=10)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
