from django.db import models
from django.conf import settings

_temp = __import__(settings.MYUNI_EXTRAS_LOCATION, globals(), locals(), ['utils'], -1)
utils = _temp.utils

ModelWithHexkey = models.get_app('hexkeys').ModelWithHexkey

SEMESTER_TYPES = (
	('autumn', 'Autumn Semester'),
	('spring', 'Spring Semester'),
)

class Year(ModelWithHexkey):
	start = models.DateTimeField()
	end = models.DateTimeField()
	reference = models.CharField(max_length=9, editable=False, unique=True)
	
	def save(self, force_insert=False, force_update=False):
		self.reference = "%d-%d" % (self.start.year, self.end.year)
		super(Year, self).save()
	
	def __unicode__(self):
		return "[Year] %s" % self.reference
	
	def get_absolute_url(self):
		return "/%s/" % self.reference
	
	def get_modules(self):
		q = utils.chain(*[s.modules.all() for s in self.semesters.all()])
		return self.modules.distinct() | q
	
	def get_previous(self):
		try:
			return self.get_previous_by_start()
		except:
			return None
	
	def get_next(self):
		try:
			return self.get_next_by_start()
		except:
			return None
	
	def get_slug(self):
		return "full-year"
	
	def get_name(self):
		return "Full-Year"
	
	class Meta:
		ordering = ['start']
	
	previous = property(get_previous)
	next = property(get_next)
	slug = property(get_slug)
	name = property(get_name)

class Semester(ModelWithHexkey):
	start = models.DateTimeField()
	end = models.DateTimeField()
	year = models.ForeignKey('timeperiods.Year', related_name='semesters')
	type = models.CharField(max_length=20, choices=SEMESTER_TYPES)
	comment = models.CharField(max_length=100, null=True, blank=True)
	
	def __unicode__(self):
		return "[Semester] %s %s" % (self.get_type_display(), self.year.reference)
	
	def get_absolute_url(self):
		return "/%s/%s/" % (self.year.reference, self.type)
	
	def get_slug(self):
		return self.type
	
	def get_name_short(self):
		return self.type.capitalize()
	
	def get_name(self):
		return self.get_type_display()
	
	class Meta:
		ordering = ['start']
	
	slug = property(get_slug)
	name_short = property(get_name_short)
	name = property(get_name)
	

	
	
