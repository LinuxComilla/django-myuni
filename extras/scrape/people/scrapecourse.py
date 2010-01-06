from BeautifulSoup import BeautifulSoup
import re, os, sys, glob

import django.contrib.auth.models

#need to do both for getattr later
from myuni.courses.models import Course
from myuni.people.models import Person
#import myuni.people.models

from myuni.extras.utils import *

def scrape(filename):
	try:
		s = BeautifulSoup(open(filename).read())

		print "Parsing file:", filename

		people = s('tr', attrs={'class': re.compile("^un.?$")})
		#print people

		for person in people:
			fields = person('td', attrs={'class': "sm2"})
		#	print fieldges
			name = fields[0].find('a').string.split(",")
			firstname = name[1].split(" ")[1]
			secondname = name[0].strip()
			course = fields[1].string.split("&nbs")[0].strip()
			course = re.findall("[A-Z][0-9]{3}", course)[0]
			#hammers the shit out of the database, can be neatened later
			course = Course.objects.get(code=course)
			username = fields[2].string.strip()
#			print (firstname,secondname,course,username)

			addToDB(Person, "username", username,
			[("first_name",		firstname),
			("last_name",		secondname),
			("username",		username),
			("course_taken",	course)
			] )
	except:
		print "parsing failed, skipping file"
		raise

"""
# objects.get() won't accept strings for attribute names
def getByString(objType, pkname, pkval):
	for inst in objType.objects.all():
		if getattr(inst, pkname) == pkval:
			return inst
	
def addToDB(objType, pkname, pkval, attrs):
	inst = getByString(objType, pkname, pkval)
	if inst == None:
		print "Making new object"
		inst = objType()
	else:
		print "Already in db"
	for name, val in attrs:
		curval = getattr(inst, name)
		if ((curval == None) or (curval == "") or (curval == [])):#all the kinds of nothing
			print "\tsetting", name, "to", val
			setattr(inst, name, val)
		else:
			print "\t", name, "was already", curval, ", leaving alone"
	inst.save()
"""
#Person.objects.get(username="jps08u").delete()

for filename in glob.glob(sys.argv[1]):
	scrape(filename)
