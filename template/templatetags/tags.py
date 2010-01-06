from django import template
from django.conf import settings

register = template.Library()

class MediaURLNode(template.Node):
	def __init__(self, path):
		self.path = path

	def render(self, context):
		import urlparse
		return urlparse.urljoin(settings.MEDIA_URL, self.path);

def media(parser, token):
	"""
		Returns an absolute URL pointing to the given media file.

		The first argument is the path to the file starting from MEDIA_ROOT.
		If the file doesn't exist, empty string '' is returned.

		For example if you have the following in your settings:

		MEDIA_URL = 'http://media.example.com'

		then in your template you can get the URL for css/mystyle.css like this:

		{% media 'css/mystyle.css' %}

		This URL will be returned: http://media.example.com/css/style.css.
	"""
	bits = list(token.split_contents())
	if len(bits) != 2:
		raise TemplateSyntaxError("%r tag takes one argument" % bits[0])

	path = bits[1]
	return MediaURLNode(path)

media = register.tag(media)

class IfInNode(template.Node):
	def __init__(self, needle, haystack, nodelist_true, nodelist_false):
		if (needle[0] == needle[-1] and needle[0] in ('"', "'")):
			self.needle = needle[1:-1]
		else:
			self.needle = template.Variable(needle)
			#raise template.TemplateSyntaxError, "%r tag's first argument (needle) should be in quotes" % tag_name
		self.haystack = template.Variable(haystack)
		self.nodelist_true = nodelist_true
		self.nodelist_false = nodelist_false
	
	def render(self, context):
		try:
			if type(self.needle) == template.Variable:
				needle = self.needle.resolve(context)
			else:
				needle = self.needle
		except template.VariableDoesNotExist:
			needle = None
		
		try:
			haystack = self.haystack.resolve(context)
		except template.VariableDoesNotExist:
			haystack = None
		if needle in haystack:
			return self.nodelist_true.render(context)
		else:
			return self.nodelist_false.render(context)

def do_ifin(parser, token):
	try:
		# split_contents() knows not to split quoted strings.
		tag_name, needle, haystack = token.split_contents()
	except ValueError:
		raise template.TemplateSyntaxError, "%r tag requires 2 arguments" % token.contents.split()[0]
	
	nodelist_true = parser.parse(('else', 'endifin'))
	token = parser.next_token()
	if token.contents == 'else':
		nodelist_false = parser.parse(('endifin',))
		parser.delete_first_token()
	else:
		nodelist_false = NodeList()
	return IfInNode(needle, haystack, nodelist_true, nodelist_false)


register.tag('ifin', do_ifin)
