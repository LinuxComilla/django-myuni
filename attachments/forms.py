from django import forms
from django.contrib.contenttypes.models import ContentType

from models import Attachment

class AttachmentForm(forms.ModelForm):
	file = forms.FileField(label='Upload file')
	
	def save(self, request, obj, *args, **kwargs):
		self.instance.creator = request.user
		self.instance.content_type = ContentType.objects.get_for_model(obj)
		self.instance.object_id = obj.id
		super(AttachmentForm, self).save(*args, **kwargs)
	
	class Meta:
		model = Attachment
		fields = ('title', 'file',)
