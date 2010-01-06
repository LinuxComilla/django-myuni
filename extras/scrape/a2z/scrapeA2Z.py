from BeautifulSoup import BeautifulSoup
import re, os, sys, glob

import django.contrib.auth.models

#need to do both for getattr later
from myuni.models import *
import myuni.models

from myuni.util.util import *

def scrape(filename):
	try:
		s = BeautifulSoup(open(filename).read())
		print "\nPARSING FILE:", filename

		people = s.findAll("tr", attrs={'class': "table-content"})
		#people = people[:5]
		
		for person in people:
			print "==============NEW PERSON======================"
			fullname = person.a.contents[0].strip()
			
			last_name = fullname.partition(",")[0].strip()
			first_name = fullname.partition(",")[2].strip()
			
			parts = person.findAll("td")
			
			phone =  parts[1].contents[0]
			job_desc = parts[2].contents[0]
			email =  parts[3].a.get("href").partition(":")[2]
			
			print first_name
			print last_name
			print phone
			print job_desc
			print email
		
		
#		print s.prettify()
		
		
	
	except:
		print "parsing failed"
		raise



for inp in sys.argv[1:]:
	for filename in glob.glob(inp):
		scrape(filename)
