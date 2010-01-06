from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/?(.*)', admin.site.root),
	
	url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}, name="index"),
	
	url(r'^colophon', 'django.views.generic.simple.direct_to_template', {'template': 'myuni/colophon.html'}, name="colophon"),
	url(r'^go', include('myuni.hexkeys.urls')),
	
	url(r'^account', include('myuni.account.urls')),
	url(r'^courses', include('myuni.courses.urls')),
	url(r'^modules', include('myuni.modules.urls')),
	url(r'^people', include('myuni.people.urls')),
	
	url(r'^attachments', include('myuni.attachments.urls')),
	
)

if hasattr(settings, 'WORKING_COPY') and settings.WORKING_COPY:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	)
