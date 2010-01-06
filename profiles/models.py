from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, pre_delete

from utils import get_user_model, create_profile_for_user, delete_profile_for_user

_temp = __import__(settings.MYUNI_EXTRAS_LOCATION, globals(), locals(), ['utils'], -1)
utils = _temp.utils

ModelWithHexkey = models.get_app('hexkeys').ModelWithHexkey

from myuni.people.models import Person

class Profile(ModelWithHexkey):
	user = models.ForeignKey(Person, unique=True)
	phone = models.CharField(max_length=50, null=True, blank=True)
	fax = models.CharField(max_length=50, null=True, blank=True)
	additional_email_addresses = models.ManyToManyField('profiles.EmailAddress', blank=True)
	address1 = models.CharField(max_length=200, null=True, blank=True)
	address2 = models.CharField(max_length=200, null=True, blank=True)
	post_code = models.CharField(max_length=10, null=True, blank=True)
	personal_info = models.TextField(null=True, blank=True)
	research_info = models.TextField(null=True, blank=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
	
	def get_absolute_url(self):
		return self.user.get_absolute_url()
	
	def __unicode__(self):
		return '[Profile] %s' % self.user.get_full_name()
	
class EmailAddress(root_object):
	"""Class for extra email addresses, referenced in Profile.additional_email_addresses"""
	email = models.EmailField()
	
	def __unicode__(self):
		return self.email


post_save.connect(create_profile_for_user, sender=get_user_model())
pre_delete.connect(delete_profile_for_user, sender=get_user_model())
