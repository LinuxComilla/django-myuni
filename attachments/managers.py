from django.db import models

class AttachmentManager(models.Manager):
	def get_for_object(self, obj):
		"""
		Create a queryset matching all attachments associated with the given object.
		"""
		ctype = ContentType.objects.get_for_model(obj)
		return self.filter(content_type=ctype, object_id=obj.pk)
