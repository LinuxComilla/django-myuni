from django.db import models

from django.contrib.auth.models import User

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

import settings

import managers

ModelWithHexkey = models.get_app('hexkeys').ModelWithHexkey

class Attachment(ModelWithHexkey):
	"""
	Stores an attachment file, which is attached to any object in the database
	"""
	title = models.CharField(max_length=200)
	creator = models.ForeignKey(User)
	file = models.FileField(upload_to=settings.ATTACHMENTS_UPLOAD_PATH)
	
	object_id = models.PositiveIntegerField(null=True, blank=True)
	content_type = models.ForeignKey(ContentType, null=True, blank=True)
	object = generic.GenericForeignKey('content_type','object_id')
	
	objects = managers.AttachmentManager()
	
	def __unicode__(self):
		return self.title
