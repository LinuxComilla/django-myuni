from django.conf.urls.defaults import *

import views

urlpatterns = patterns("",

	url(r'^/$', views.courses_list, name="courses_course_list"),
	url(r'^/type/(?P<type_slug>[a-zA-Z0-9\-]+)/$', views.courses_list),
	url(r'^/(?P<course_code>[\w]+)/$', views.course_detail, name="courses_course_detail"),
	
)
