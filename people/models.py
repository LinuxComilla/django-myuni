from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import get_model
from django.db.models.signals import post_save, pre_delete
from utils import get_user_model, create_profile_for_user, delete_profile_for_user
from managers import *

_temp = __import__(settings.MYUNI_EXTRAS_LOCATION, globals(), locals(), ['utils'], -1)
utils = _temp.utils

ModelWithHexkey = models.get_app('hexkeys').ModelWithHexkey

GENDER_CHOICES = (('M', 'Male'),('F', 'Female'))

class Group(ModelWithHexkey):
	name = models.CharField(max_length=50, unique=True)
	slug = models.CharField(max_length=50, editable=False, unique=True)
	members = models.ManyToManyField('people.Person')
	"""TODO:
		- Fix the related_name on members, it can't be "groups" as that is used by Django's
			User model, which we inherit from in Person. Maybe we could use Django's Group
			model anyway - there's nothing complicated about groups, right?
	"""
	
	def save(self, force_insert=False, force_update=False):
		self.slug = utils.slugify(self.name)
		super(Group, self).save(force_insert, force_update)
	
	def __unicode__(self):
		return "[Group] %s" % self.name

class Role(ModelWithHexkey):
	name = models.CharField(max_length=200, unique=True)
	weight = models.IntegerField()
	objects = RoleManager()
	
	def __unicode__(self):
		return "[Role] %s (%s)" % (self.name, self.weight)
	
	class Meta:
		ordering = ['-weight']

class Salutation(ModelWithHexkey):
	abbr = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.abbr

class PersonStudentsHelper:
	def __init__(self, person):
		self.person = person

	def all(self):
		all_modules = self.person.modules_lectured.all()
		return utils.chain(*[m.students.all() for m in all_modules])
	
	def previous(self):
		all_modules = self.person.modules_lectured.all()
		current_modules = self.person.modules_lectured.current()
		previous_modules = None
		
		for module in current_modules:
			if previous_modules:
				previous_modules = previous_modules.exclude(pk=module.pk)
			else:
				previous_modules = all_modules.exclude(pk=module.pk)
		
		return utils.chain(*[m.students.all() for m in previous_modules])
	
	def current(self):
		current_modules = self.person.modules_lectured.current()
		return utils.chain(*[m.students.all() for m in current_modules])
			

class Person(User):

	"""Model representing a person. Inherits from Django's User object"""
	
	title = models.ForeignKey(Salutation, null=True, blank=True)
	initial = models.CharField(max_length=10, default='', null=True, blank=True)
	supervised_by = models.ManyToManyField('people.Person', related_name='supervisees', blank=True)
	roles = models.ManyToManyField(Role, blank=True)
	course_taken = models.ForeignKey('courses.Course', related_name='students', null=True, blank=True)
	sid = models.IntegerField(null=True, blank=True)
	heaviest_role_weight = models.IntegerField(editable=False, null=True, blank=True)
	objects = PersonManager()
	
	def save(self, force_insert=False, force_update=False):
		if self.pk:
			role = self.roles.heaviest()
			if role:
				self.heaviest_role_weight = role.weight
		super(Person, self).save(force_insert, force_update)
	
	def __unicode__(self):
		"""Cast into a string for printing. '[Person] <person's full name>'."""
		return '[Person] %s' % self.get_full_name()
	
	def get_absolute_url(self):
		"""Return the person's canonical url. (people/<username>/)"""
		return "/people/%s/" % self.username
	
	def get_short_url(self):
		"""Return the Person's /go/ url"""
		return self.get_profile().get_short_url()
	
	def is_student(self):
		"""Return true if the person belongs to the Students group."""
		return Group.objects.get(name='Students') in self.groups.all()
	
	def can_edit(self, moduleinstance):
		"""Return true if the person can edit the given moduleinstance."""
		assert (type(moduleinstance) == ModuleInstance)
		return self in moduleinstance.lecturers.all()
	
	def get_editable_objects(self):
		"""Return a list of objects the person can edit"""
		editable = list(self.modules_convened.all())
		editable += list(self.modules_lectured.all())
		return list(set(editable)) # Uniqify the list of editable objects
		
	def is_staff(self):
		"""Return true if the Person belongs to the 'Students' group."""
		return Group.objects.get(name='Staff') in self.groups.all()
	
	def get_students(self):
		return PersonStudentsHelper(self)
	
	class Meta:
		verbose_name_plural = 'people'
		ordering = ['last_name']

class EmailAddress(ModelWithHexkey):
	"""Class for extra email addresses, referenced in Profile.additional_email_addresses"""
	email = models.EmailField()
	
	def __unicode__(self):
		return self.email

class Profile(ModelWithHexkey):
	"""Object for user-editable information about People"""
	user = models.ForeignKey(Person, editable=False, unique=True)  # To follow this the other way, use '<person>.get_profile()'
	phone = models.CharField(max_length=50, null=True, blank=True)
	fax = models.CharField(max_length=50, null=True, blank=True)
	additional_email_addresses = models.ManyToManyField(EmailAddress, blank=True)
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
	



post_save.connect(create_profile_for_user, sender=get_user_model())
pre_delete.connect(delete_profile_for_user, sender=get_user_model())



