from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

_temp = __import__(settings.MYUNI_EXTRAS_LOCATION, globals(), locals(), ['utils'], -1)
utils = _temp.utils

ModelWithHexkey = models.get_app('hexkeys').ModelWithHexkey

class CourseType(ModelWithHexkey):
	name = models.CharField(max_length=50)
	details = models.CharField(max_length=200, null=True, blank=True)
	slug = models.SlugField(max_length=20, editable=False)
	
	def save(self, force_insert=False, force_update=False):
		self.slug = slugify(self.name)
		super(CourseType, self).save(force_insert, force_update)
	
	def __unicode__(self):
		return self.name
	
class Course(ModelWithHexkey):
	code = models.CharField(max_length=10, unique=True)
	school = models.ForeignKey('schools.School', related_name='courses')
	name = models.CharField(max_length=200)
	type = models.ForeignKey('courses.CourseType')
	url = models.URLField(null=True, blank=True)
	
	def __unicode__(self):
		return self.code
	
	def get_absolute_url(self):
		return "/courses/%s/" % self.code
	
	class Meta:
		verbose_name_plural = "courses"
		ordering = ['school', 'code', 'name']
