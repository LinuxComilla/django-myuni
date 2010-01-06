from django.conf.urls.defaults import *

import views

urlpatterns = patterns("",

	url(r'^/$', views.moduleinstance_list, name="modules_moduleinstance_list"),
	
	url(r'^/(?P<module_code>[a-zA-Z][0-9]{2,2}[a-zA-Z]{3,3})/$', views.module_detail, name="modules_module_detail"),
	
	url(r'^/(?P<year>[0-9]{4,4}\-[0-9]{4,4})/$', views.moduleinstance_list, name="modules_moduleinstance_list_by_year"),
	url(r'^/(?P<year>[0-9]{4,4}\-[0-9]{4,4})/(?P<semester>[\w-]+)/$', views.moduleinstance_list),
	
	url(r'^/(?P<module_code>[\w]+)/(?P<year>[0-9-]+)/$', views.moduleinstance_detail),
	url(r'^/(?P<module_code>[\w]+)/(?P<year>[0-9-]+)/(?P<semester>[\w]+)/$', views.moduleinstance_detail),
	
)
