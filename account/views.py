from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from myuni.people.models import Person, Group
from myuni.people.forms import ProfileForm

from forms import RegistrationForm

@login_required
def account_detail(request, template='account.html'):
	data = {}
	return render_to_response(template, data, context_instance=RequestContext(request))

def register(request, template='account.register.form.html'):
	if request.method == 'POST':
		f = RegistrationForm(request.POST)
		if f.is_valid():
			person = f.save()
			return HttpResponseRedirect(person.get_absolute_url())
	else:
		f = RegistrationForm()
	data = { 'form': f }	
	return render_to_response(template, data, context_instance=RequestContext(request))

@login_required
def profile(request, template='account/profile.edit.html'):
	if request.method == 'POST':
		f = ProfileForm(request.POST, instance=request.user.get_profile())
		if f.is_valid():
			f.save()
			return HttpResponseRedirect("/account/")
	else:
		f = ProfileForm(instance=request.user.get_profile())
	data = {'form': f}
	return render_to_response(template, data, context_instance=RequestContext(request))

def change_password(request):
	f = PasswordChangeForm()
	return render_to_response('testing/password.html', {'form': f}, context_instance=RequestContext(request))

def login(request, template='account.login.html'):
	if (request.user.is_authenticated()):
		return HttpResponseRedirect("/account/")
	if request.method == 'POST':
		f = AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect("/account/")
			else:
				error = 'account_disabled'
				return render_to_response(template, {'form': f, 'error': error, 'form_error': 'Account disabled'}, context_instance=RequestContext(request))
		else:
			error = 'bad_password'
			return render_to_response(template, {'form': f, 'error': error, 'form_error': 'Invalid username/password'}, context_instance=RequestContext(request))
	else:
		f = AuthenticationForm()
		return render_to_response(template, {'form': f, 'user':request.user}, context_instance=RequestContext(request))



def logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/")


