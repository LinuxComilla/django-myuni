from django.conf.urls.defaults import *
from django.contrib.auth.views import password_change, password_reset
import views

urlpatterns = patterns("",
	
	url(r'^/$', views.account_detail, name="account_detail"),
	
	url(r'^/login/$', views.login, name="account_login"),
	url(r'^/logout/$', views.logout, name="account_logout"),
	
	url(r'^/create/$', views.register, name="account_register"),
	
	url(r'^/profile/$', views.profile, name="account_profile"),
	
	url(r'^/password/$', password_change, {'template_name': 'account/password.edit.html', 'post_change_redirect': '/account/'}),
	
)
