from django.http import HttpResponse
from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from social import exceptions as social_exceptions


class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
	def process_exception(self, request, exception):
		if hasattr(social_exceptions, 'AuthForbidden'):
			return HttpResponse(exception)
		else:
			raise exception
