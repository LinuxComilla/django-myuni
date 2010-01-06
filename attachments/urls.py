from django.conf.urls.defaults import *

from models import Attachment
import views

urlpatterns = patterns("",
	
	url(r'attach/$', views.new_attachment, {'template_name': 'uploads/new_upload.html'}, name='uploads_attach'),
	
	url(r'(?P<object_id>[\w]+)/$', 'django.views.generic.list_detail.object_detail',
		{'queryset': Attachment.objects.all(), 'template_name': 'uploads/uploadedfile_detail.html'},
		name='uploads_uploadedfile_detail'),
	
)
