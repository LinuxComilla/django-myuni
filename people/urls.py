from django.conf.urls.defaults import *

import views

urlpatterns = patterns("",
	
	url(r'^/$', views.person_list, name="people_person_list"),
	url(r'^/(?P<ordering>by\-role|by\-first\-name|by\-last\-name)/$', views.person_list, name="people_person_list_ordered"),
	
	url(r'^/groups/(?P<group_slug>[\w-]+)/$', views.person_list_by_group, name="people_person_list_by_group"),
	url(r'^/groups/(?P<group_slug>[\w-]+)/(?P<ordering>by\-role|by\-first\-name|by\-last\-name)/$', views.person_list_by_group, name="people_person_list_by_group_ordered"),
	
	url(r'^/(?P<username>[\w]+)/$', views.person_detail, name="people_person_detail"),
	
)
