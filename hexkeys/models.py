from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from utils import generateReference

class Hexkey(models.Model):
	key = models.CharField(max_length=20, unique=True, null=True)
	
	#object_id = models.CharField(max_length=20, null=True, blank=True)
	content_type = models.ForeignKey(ContentType, null=True, blank=True)
	object = generic.GenericForeignKey('content_type','key')
	
	def save(self, *args, **kwargs):
		super(self.__class__, self).save(*args, **kwargs)
		if not self.key:
			self.key = generateReference(self.id)
			self.save()
	
	def __unicode__(self):
		return self.key or '<unassigned hexkey>'

class ModelWithHexkey(models.Model):
	id = models.CharField(max_length=20, primary_key=True, editable=False)
	
	def get_hexkey_obj(self):
		return Hexkey.objects.get(key=self.id)
	
	def save(self, *args, **kwargs):
		if not self.id:
			key = Hexkey()
			key.content_type = ContentType.objects.get_for_model(self)
			key.save()
			self.id = key.key
		super(ModelWithHexkey, self).save(*args, **kwargs)
	
	class Meta:
		abstract = True

class TestModel(ModelWithHexkey):
	
	name = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.name
