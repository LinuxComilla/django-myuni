def version(request):
	import os
	from django.conf import settings
	try:
		f = open(os.path.join(settings.PROJECT_DIR, "version"))
		v = f.read()
		f.close()
		v = v.strip()
		return {'version': v}
	except:
		return {'version': 'Unknown'}

def current_year(request):
	from myuni.timeperiods.utils import get_current_year
	return {'current_year': get_current_year()}
