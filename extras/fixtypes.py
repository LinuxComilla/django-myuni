from myuni.object.models import Object

def fix_types():

	objects = Object.objects.all()

	print "Fixing the type of all objects. This could take a while..."

	for object in objects:
		try:
			t = object.get_object_type()
			object.object_type = t
			print "%s is a %s" % (object.id, t)
			object.save()
		except:
			print "Lost child on object %s" % object.id

	print "Done"

if __name__ == "__main__":
    fix_types()
