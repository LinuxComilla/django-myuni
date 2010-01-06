from django.db.models import get_model
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth.models import User, SiteProfileNotAvailable

def get_profile_model():
	if hasattr(settings, "AUTH_PROFILE_MODULE") and settings.AUTH_PROFILE_MODULE:
		model = get_model(*settings.AUTH_PROFILE_MODULE.split('.'))
		if model is None:
			raise SiteProfileNotAvailable
	else:
		raise SiteProfileNotAvailable
	return model

def get_user_model():
	if hasattr(settings, "CUSTOM_USER_MODEL") and settings.CUSTOM_USER_MODEL:
		model = get_model(*settings.CUSTOM_USER_MODEL.split('.'))
		if model is None:
			raise ImproperlyConfigured, "CUSTOM_USER_MODEL '%s' not available" % settings.CUSTOM_USER_MODEL
	else:
		model = User
	return model

def create_profile_for_user(sender, instance, created, **kwargs):
	try:
		get_profile_model().objects.get(user=instance)
	except (get_profile_model().DoesNotExist, AssertionError):
		get_profile_model()(user=instance).save()

def delete_profile_for_user(sender, instance, **kwargs):
	try:
		profile = get_profile_model().objects.get(user=instance)
		profile.delete()
	except (get_profile_model().DoesNotExist, AssertionError):
		pass
