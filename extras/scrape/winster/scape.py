from BeautifulSoup import BeautifulSoup
import re, os, sys, glob

#need to do both for getattr later
from myuni.models import *
import myuni.models

from myuni.util.util import *

def scrape(filename):
	try:
		s = BeautifulSoup(open(filename).read())

		print "\nPARSING FILE:", filename

		code = s.body.h2.contents[0].split(" ")[0].strip()
		print "module code =", code

		name = s.body.h2.contents[0].partition(" ")[2].strip()
		print "module name =", name

		year = s.body.h3.string.split(";")[1].strip()
		print "year =", year

		semester = s.find('b', text=re.compile("^.*Taught Semesters.*$")).parent.parent.find('td').string.partition("&")[0].strip()
		print "semester =", semester

		convenors = []
		for bit in s.find('b', text=re.compile("^Convenor.*:.*$")).parent.parent.contents[1:]:
			string = bit.string
			if (string != None) and (len(string.strip()) > 0):
				convenors.append(string.strip())
		print "convenors =", convenors

		credits = int(s.find('b', text=re.compile("^Total Credits.*$")).parent.parent.contents[1].strip())
		print "credits =", credits

		level = s.find('b', text=re.compile("^Level.*$")).parent.parent.contents[1].split(" ")[1:][0].strip()
		print "level =", level

		addToDB(Module, "code", code,
			[("code",		code),
			("name",		name),
			("credits",		credits),
			("level",		level)
			] )

	except:
		print "parsing failed"
		raise
	

for inp in sys.argv[1:]:
	for filename in glob.glob(inp):
		scrape(filename)
