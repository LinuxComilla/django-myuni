def get_root_object():
	from django.conf import settings
	from django.db.models import get_model
	if not hasattr(settings, "ROOT_OBJECT") or not settings.ROOT_OBJECT:
		raise AttributeError, "ROOT_OBJECT is not defined in settings.py"
	else:
		return get_model(*settings.ROOT_OBJECT.split("."))

def chain(*args, **kwargs):
	unique = kwargs['unique'] if 'unique' in kwargs else True
	r = None
	for q in args:
		r = r | q if r else q
	if r is None: return r
	return r.distinct() if unique else r

def slugify(s):
	"""
	Takes a String and turns it into a slug by replacing spaces with dashes
	and making it lower case.
	"""
	return s.replace(' ', '-').lower()

# objects.get() won't accept strings for attribute names. used by addToDB
def getByString(objType, pkname, pkval):
	for inst in objType.objects.all():
		if getattr(inst, pkname) == pkval:
			return inst

class DataConflictException(Exception):
	"""
	An exception raised when scrape data is different from db data
	"""
	def __init__(self, orig='', new=''):
		self.orig = orig
		self.new = new
	def __str__(self):
		return "existing value \'"+orig+"\' doesn't match new value \'"+new

def addToDB(objType, pkname, pkval, attrs, makeNew=True):
	"""
	Add a new object to the database using a list of attributes (for scraping)
	e.g addToDB(myuni.models.Person, "username", "srb", [("username,"srb"),("name","steven bagley")])
	"""
	print "attempting to add", pkval, "to db..."
	inst = getByString(objType, pkname, pkval)
	if inst == None:
		if makeNew:
			print "Making new object"
			inst = objType()
		else:
			print pkval, "not in DB, _not_ trying to add it"
			return
	else:
		print "Already in db"
	for name, val in attrs:
		curval = getattr(inst, name)
		if ((curval == None) or (curval == "") or (curval == [])):#all the kinds of nothing
			print "\tsetting", name, "to", val
			setattr(inst, name, val)
		else:
			if curval != val:
				DataConflictException(curval, val)
			print "\t", name, "was already", curval, ", leaving alone"
	inst.save()
	print "added", pkval, "to db successfully", "\n"
	
