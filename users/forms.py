from django import forms
from django.core.validators import RegexValidator
from models import Department

class UserBasicProfileForm(forms.Form):
	first_name = forms.CharField(label='First name', max_length=100)
	last_name = forms.CharField(label='Last name', max_length=100)
	username = forms.CharField(label='Username', max_length=100,
		validators=[RegexValidator(regex="^(?=.{3,30}$)[a-zA-Z0-9'._-]+$",
		message='Invalid username', code='Invalid username')])

class UserCompanyInfoForm(forms.Form):
	personal_email = forms.EmailField(label="Personal email")
	designation = forms.CharField(label="Designation")
	department = forms.ModelChoiceField(queryset=Department.objects.all())

class UserLinksForm(forms.Form):
	name = forms.CharField(label="Name")
	url = forms.URLField(label="URL")
