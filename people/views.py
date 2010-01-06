from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import Person, Group

def person_list(request, ordering='by-role', template='people/person.list.html'):
	"""The view for lists of people"""
	if ordering == 'by-role':
		people = Person.objects.by_role()
	elif ordering == 'by-first-name':
		people = Person.objects.order_by('first_name')
	elif ordering == 'by-last-name':
		people = Person.objects.order_by('last_name')
	groups = Group.objects.all()
	data = { 'people' : people, 'groups': groups, 'ordering': ordering }
	return render_to_response(template, data, context_instance=RequestContext(request))

def person_list_by_group(request, group_slug, ordering='by-role', template='people/person.list.html'):
	"""The view for lists of people sorted by group"""
	group = get_object_or_404(Group, slug=group_slug)
	groups = Group.objects.all()
	people = group.members.all()
	if ordering == 'by-role':
		people = people.order_by('-heaviest_role_weight', 'last_name')
	elif ordering == 'by-first-name':
		people = people.order_by('first_name')
	elif ordering == 'by-last-name':
		people = people.order_by('last_name')
	data = { 'people' : people, 'groups': groups, 'group': group, 'ordering': ordering }
	return render_to_response(template, data, context_instance=RequestContext(request))

def person_detail(request, username, template='people/person.html'):
	person = get_object_or_404(Person, username=username)
	data = { 'person' : person }
	return render_to_response(template, data, context_instance=RequestContext(request))
