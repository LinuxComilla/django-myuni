from django.db import models
from django.conf import settings

_temp = __import__(settings.MYUNI_EXTRAS_LOCATION, globals(), locals(), ['utils'], -1)
utils = _temp.utils

ModelWithHexkey = models.get_app('hexkeys').ModelWithHexkey
class School(ModelWithHexkey):
	name = models.CharField(max_length=200, unique=True)
	url = models.URLField()
	
	def __unicode__(self):
		return self.name
	
	def get_absolute_url(self):
		return "/schools/%s/" % self.id
	
	class Meta:
		verbose_name_plural = "schools"
		ordering = ['name']
