from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
	
	url(r'^(?P<hexkey>.+)/$', views.redirect, name='hexkeys_redirect'),
	
)
