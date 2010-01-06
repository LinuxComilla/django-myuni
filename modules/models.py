from django.db import models
from django.forms import ValidationError
from django.conf import settings
from django import forms

_temp = __import__(settings.MYUNI_EXTRAS_LOCATION, globals(), locals(), ['utils'], -1)
utils = _temp.utils

from managers import *

import datetime

ModelWithHexkey = models.get_app('hexkeys').ModelWithHexkey

class Module(ModelWithHexkey):
	code = models.CharField(max_length=6, unique=True)
	courses = models.ManyToManyField('courses.Course', related_name='modules')
	compulsory_for = models.ManyToManyField('courses.Course', blank=True, related_name='compulsory_modules')
	name = models.CharField(max_length=200)
	credits = models.IntegerField(max_length=4)
	level = models.IntegerField(max_length=2)
	
	def __unicode__(self):
		return "[Module] %s" % self.code
	
	class Meta:
		ordering = ['code', 'name']

class ModuleInstance(ModelWithHexkey):
	class ConvenerNotAllowed(Exception):
		pass
	class LecturerNotAllowed(Exception):
		pass
	
	module = models.ForeignKey('modules.Module', related_name='instances')
	year = models.ForeignKey('timeperiods.Year', related_name='modules', null=True, blank=True)
	semester = models.ForeignKey('timeperiods.Semester', related_name='modules', null=True, blank=True)
	convener = models.ForeignKey('people.Person', null=True, related_name='modules_convened')
	tutors = models.ManyToManyField('people.Person', related_name='modules_tutored')
	lecturers = models.ManyToManyField('people.Person', related_name='modules_lectured')
	students = models.ManyToManyField('people.Person', related_name='modules_taken')
	url = models.URLField(null=True, blank=True)
	credits_override = models.IntegerField(max_length=4, null=True, blank=True)
	objects = ModuleInstanceManager()
	
	def __unicode__(self):
		if self.year:
			return "[ModuleInstance] %s (%s)" % (self.module.code, self.year)
		elif self.semester:
			return "[ModuleInstance] %s (%s)" % (self.module.code, self.semester)
	
	def save(self, force_insert=False, force_update=False):
		if not self.year and not self.semester:
			raise ValidationError, "ModuleInstance must be assigned to either a year or a semester"
		if self.year and self.semester:
			raise ValidationError, "ModuleInstance cannot be assigned to both a year and a semester"
		groups = self.convener.groups.all()
		gs = []
		for group in groups:
			gs.append(group.name)
		if not set(settings.REQUIRED_GROUPS_FOR_CONVENERS).issubset(set(gs)):
			raise self.ConvenerNotAllowed, "Convener '%s' must be a member of groups: %s" % (self.convener, settings.REQUIRED_GROUPS_FOR_CONVENERS)
		if self.pk:
			for lecturer in self.lecturers.all():
				groups = lecturer.groups.all()
				gs = []
				for group in groups:
					gs.append(group.name)
				if not set(settings.REQUIRED_GROUPS_FOR_LECTURERS).issubset(set(gs)):
					raise self.LecturerNotAllowed, "Lecturer '%s' must be a member of groups: %s" % (lecturer, settings.REQUIRED_GROUPS_FOR_LECTURERS)
		super(ModuleInstance, self).save()
	
	def get_duration(self):
		if self.year:
			return 'year'
		elif self.semester:
			return 'semester'
		else:
			raise self.DoesNotExist
	
	def get_absolute_url(self):
		t = self.get_duration()
		if t == 'year':
			return '/modules/%s/%s/' % (self.module.code, self.year.reference)
		elif t == 'semester':
			return '/modules/%s/%s/%s/' % (self.module.code, self.semester.year.reference, self.semester.type)
	
	def is_current(self):
		return (self in ModuleInstance.objects.current())
	
	def get_credits(self):
		return self.credits_override or self.module.credits
	
	def get_year(self):
		if self.year:
			return self.year
		else:
			return self.semester.year
	
	def get_semester(self):
		if self.semester:
			return self.semester
		else:
			return None
	
	def get_editors(self):
		editors = list(self.lecturers.all())
		editors.append(self.convener)
		return list(set(editors))  # Uniqify the list of editors
	
	def get_code(self):
		return self.module.code
		
	def get_name(self):
		return self.module.name
	
	duration = property(get_duration)
	current = property(is_current)
	credits = property(get_credits)
	editable_by = property(get_editors)
	code = property(get_code)
	name = property(get_name)
	
	class Meta:
		unique_together = (('module', 'year'), ('module', 'semester'))
		ordering = ['module']

class ModuleInstanceForm(forms.ModelForm):
	class Meta:
		model = ModuleInstance

	def __init__(self, *args, **kwargs):
		group_model = models.get_model('people', 'group')
		super(ModuleInstanceForm, self).__init__(*args, **kwargs)
		self.fields['convener'].queryset = utils.chain(*[group_model.objects.get(name=name).members.all() for name in settings.REQUIRED_GROUPS_FOR_CONVENERS])
		self.fields['lecturers'].queryset = utils.chain(*[group_model.objects.get(name=name).members.all() for name in settings.REQUIRED_GROUPS_FOR_LECTURERS])
		self.fields['tutors'].queryset = utils.chain(*[group_model.objects.get(name=name).members.all() for name in settings.REQUIRED_GROUPS_FOR_TUTORS])
		self.fields['students'].queryset = utils.chain(*[group_model.objects.get(name=name).members.all() for name in settings.REQUIRED_GROUPS_FOR_STUDENTS])
