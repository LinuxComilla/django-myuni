#fsdg -*- coding: iso-8859-1 -*-
# -*- coding: utf-8 -*-

import datetime

from myuni.courses.models import *
from myuni.modules.models import *
from myuni.people.models import *
from myuni.schools.models import *
from myuni.timeperiods.models import *

import django.contrib.auth.models

def load_data():

	print "deleting auth database (or most of it)..."
	users = django.contrib.auth.models.User.objects.all()
	#Cheers :)
	for user in users:
		user.delete()

	print "Loading basic data into database..."

	# ==========================Titles=================================

	rl = Role(
	name='Head of School',
	weight=900
	)
	rl.save()

	rl = Role(
	name='Deputy Head of School',
	weight=850
	)
	rl.save()

	rl = Role(
	name='Emeritus Professor',
	weight=700
	)
	rl.save()

	rl = Role(
	name='Professor',
	weight=650
	)
	rl.save()

	rl = Role(
	name='Associate Professor',
	weight=600
	)
	rl.save()
	
	rl = Role(
	name='Associate Professor and Reader',
	weight=630
	)
	rl.save()

	rl = Role(
	name='Assistant Professor',
	weight=550
	)
	rl.save()

	rl = Role(
	name='Convener',
	weight=525
	)
	rl.save()

	rl = Role(
	name='Lecturer',
	weight=500
	)
	rl.save()
	
	rl = Role(
	name='PhD Student',
	weight=350
	)
	rl.save()
	
	rl = Role(
	name='Tutor',
	weight=300
	)
	rl.save()

	rl = Role(
	name='Student',
	weight=200
	)
	rl.save()
	
	#===============================Titles===================================
	
	Salutation(abbr='Mr.').save()
	
	Salutation(abbr='Dr.').save()
	
	Salutation(abbr='Prof.').save()
	
	Salutation(abbr='Rev.').save()
	
	#============================GROUPS=======================================
	
	staff = Group(name="Staff")
	staff.save()
	
	students = Group(name="Students")
	students.save()
	
	lecturers = Group(name="Lecturers")
	lecturers.save()
	
	tutors = Group(name="Tutors")
	tutors.save()
	
	# ==========================PEOPLE=================================
	# LECTURERS
	p = Person(
	username='srb',
	title=Salutation.objects.get(abbr='Dr.'),
	first_name='Steven',
	last_name='Bagley',
	initial='R',
	email='srb@cs.nott.ac.uk'
	)
	p.save()
	p.set_password("iamsrb")
	p.save()
	
	p.roles.add(Role.objects.get(name='Lecturer'))
	
	staff.members.add(p)
	
	lecturers.members.add(p)
	
	p = Person(
	username='gmh',
	title=Salutation.objects.get(abbr='Dr.'),
	first_name='Graham',
	last_name='Hutton',
	initial='M',
	email='gmh@cs.nott.ac.uk',
	)
	p.save()
	p.set_password("iamgmh")
	p.save()
	
	p.roles.add(Role.objects.get(name='Associate Professor and Reader'))
	
	staff.members.add(p)
	
	lecturers.members.add(p)

	p = Person(
	username='mjj',
	first_name='Mauro',
	last_name='Jaskelioff',
	initial='J',
	email='mjj@cs.nott.ac.uk',
	)
	p.save()
	p.set_password("iammjj")
	p.save()
	
	p.roles.add(Role.objects.get(name='PhD Student'))
	
	staff.members.add(p)
	
	lecturers.members.add(p)

	p = Person(
	username='dfb',
	title=Salutation.objects.get(abbr='Prof.'),
	first_name='David',
	last_name='Brailsford',
	initial='F',
	email='dfb@cs.nott.ac.uk',
	)
	p.save()
	p.set_password("iamdfb")
	p.save()
	
	p.roles.add(Role.objects.get(name='Professor'))
	
	staff.members.add(p)
	
	lecturers.members.add(p)

	p = Person(
	username='nza',
	title=Salutation.objects.get(abbr='Dr.'),
	first_name='Natasha',
	last_name='Alechina',
	initial='Z',
	email='nza@cs.nott.ac.uk',
	)
	p.save()
	p.set_password("iamnza")
	p.save()
	
	p.roles.add(Role.objects.get(name='Associate Professor'))
	
	staff.members.add(p)
	
	lecturers.members.add(p)

	p = Person(
	username='rcb',
	title=Salutation.objects.get(abbr='Dr.'),
	first_name='Roland',
	last_name='Backhouse',
	initial='C',
	email='rcb@cs.nott.ac.uk',
	)
	p.save()
	p.set_password("iamrcb")
	p.save()
	
	p.roles.add(Role.objects.get(name='Lecturer'))
	
	staff.members.add(p)
	
	lecturers.members.add(p)

	p = Person(
	username='jqg',
	title=Salutation.objects.get(abbr='Dr.'),
	first_name='Julie',
	last_name='Greensmith',
	initial='Q',
	email='jqg@cs.nott.ac.uk',
	)
	p.save()
	p.set_password("iamjqg")
	p.save()
	
	p.roles.add(Role.objects.get(name='Lecturer'))
	
	staff.members.add(p)
	
	lecturers.members.add(p)

	# TUTORS
	Person(
	username='ajr',
	first_name='Alistair',
	last_name='Ross',
	initial='J',
	email='ajr@cs.nott.ac.uk',
	).save()
	
	tutors.members.add(p)

	Person(
	username='sda',
	first_name='Sam',
	last_name='Allen',
	initial='D',
	email='sda@cs.nott.ac.uk',
	).save()
	
	tutors.members.add(p)

	Person(
	username='gzt',
	first_name=u"Germán",  
	last_name='Terrazas Angulo',
	initial='',
	email='gzt@cs.nott.ac.uk',
	).save()
	
	tutors.members.add(p)
	tutors.save()

	Person(
	username='azs',
	first_name='Amr',
	last_name='Soghier',
	initial='',
	email='azs@cs.nott.ac.uk',
	).save()
	
	tutors.members.add(p)

	Person(
	username='mvh',
	first_name='Matthew',
	last_name='Hyde',
	initial='V',
	email='mvh@cs.nott.ac.uk',
	).save()
	
	tutors.members.add(p)

	Person(
	username='bzb',
	first_name='Ben',
	last_name='Bedwell',
	initial='',
	email='bzb@cs.nott.ac.uk',
	).save()
	
	tutors.members.add(p)

	# STUDENTS
	p = Person(
	username='rxm08u',
	first_name='Robert',
	last_name='Miles',
	initial='SK',
	is_staff=1,
	is_superuser=1,
	email='rxm08u@cs.nott.ac.uk',
	sid='4086746'
	)
	p.save()
	p.set_password("iamrxm08u")
	
	students.members.add(p)
	students.save()

	p = Person(
	username='bxj08u',
	first_name='Benedict',
	last_name='Jenkinson',
	is_staff=1,
	is_superuser=1,
	email='bxj08u@cs.nott.ac.uk',
	sid='4082995'
	)
	p.save()
	p.set_password("iambxj08u")
	p.save()
	
	students.members.add(p)

	p = Person(
	username='rjg08u',
	first_name='Robert',
	last_name='Golding',
	initial='J',
	is_staff=1,
	is_superuser=1,
	email='rjg08u@cs.nott.ac.uk',
	sid='4082351'
	)
	p.save()
	p.set_password("iamrjg08u")
	p.save()
	
	students.members.add(p)
	
	p = Person(
	username='mxw18u',
	first_name='Marcus',
	last_name='Whybrow',
	initial='',
	is_staff=1,
	is_superuser=1,
	email='mxw18u@cs.nott.ac.uk',
	sid='4083181'
	)
	p.save()
	p.set_password("iammxw18u")
	
	students.members.add(p)
	students.save()
	
	#============================SCHOOLS=======================================

	School(
	name="School of Computer Science",
	url="cs.nott.ac.uk"
	).save()

	#============================COURSES=======================================

	bsch = CourseType(
	name = "B.Sc. (Hons)",
	details = "Bachelor of Science (Honours)",
	slug = "bsc-hons"
	)
	bsch.save()

	bsc = CourseType(
	name = "B.Sc.",
	details = "Bachelor of Science",
	slug = "bsc"
	)
	bsc.save()
		
	cs = Course(
	code="G400",
	type=bsch,
	name="Computer Science",
	school=School.objects.get(name="School of Computer Science"),
	)
	cs.save()
	#cs.students.add(Person.objects.get(username="rxm08u"))
	#cs.students.add(Person.objects.get(username="rjg08u"))
	#cs.students.add(Person.objects.get(username="bxj08u"))
	#cs.save()

	cs = Course(
	code="G601",
	type=bsch,
	name="Software Systems",
	school=School.objects.get(name="School of Computer Science"),
	)
	cs.save()
	#cs.students.add(Person.objects.get(username="rxm08u"))
	#cs.students.add(Person.objects.get(username="rjg08u"))
	#cs.students.add(Person.objects.get(username="bxj08u"))
	#cs.save()

	#============================YEARS=======================================

	y1 = Year(
	start = datetime.datetime(2007, 9, 5),
#	end = datetime.datetime(2008, 6, 5),
	end = datetime.datetime(2008, 9, 5)
	)
	y1.save()

	y2 = Year(
	start = datetime.datetime(2008, 9, 5),
#	end = datetime.datetime(2009, 6, 5),
	end = datetime.datetime(2009, 9, 5),
	)
	y2.save()

	y3 = Year(
	start = datetime.datetime(2009, 9, 5),
#	end = datetime.datetime(2010, 6, 5),
	end = datetime.datetime(2010, 9, 5),
	)
	y3.save()

	#============================SEMESTERS=======================================

	s1 = Semester(
	year = y1,
	start = datetime.datetime(2007, 9, 5),
	end = datetime.datetime(2008, 1, 10),
	type = 'autumn',
	comment = 'Autumn semester for 2007-2008'
	)
	s1.save()

	s2 = Semester(
	year = y1,
	start = datetime.datetime(2008, 1, 25),
	end = datetime.datetime(2008, 6, 5),
	type = 'spring',
	comment = 'Spring semester for 2007-2008'
	)
	s2.save()

	s3 = Semester(
	year = y2,
	start = datetime.datetime(2008, 9, 5),
	end = datetime.datetime(2009, 1, 10),
	type = 'autumn',
	comment = 'Autumn semester for 2008-2009'
	)
	s3.save()

	s4 = Semester(
	year = y2,
	start = datetime.datetime(2009, 1, 25),
	end = datetime.datetime(2009, 6, 5),
	type = 'spring',
	comment = 'Spring semester for 2008-2009'
	)
	s4.save()

	s5 = Semester(
	year = y3,
	start = datetime.datetime(2009, 9, 5),
	end = datetime.datetime(2010, 1, 10),
	type = 'autumn',
	comment = 'Autumn semester for 2009-2010'
	)
	s5.save()

	s6 = Semester(
	year = y3,
	start = datetime.datetime(2010, 1, 25),
	end = datetime.datetime(2010, 6, 5),
	type = 'spring',
	comment = 'Spring semester for 2009-2010'
	)
	s6.save()

	#============================MODULES=======================================

	def add_module(code, name, credits, level, courses):
		mod = Module(
		code=code,
		name=name,
		credits=credits,
		level=level
		)
		mod.save()
		for course in courses:
			mod.courses.add(Course.objects.get(code=course))
		mod.save()

	add_module('G51PRG', 'Programming', '20', '1', ['G400', 'G601'])
	add_module('G51FUN', 'Functional Programming', '10', '1', ['G400', 'G601'])
	add_module('G51WPS', 'Web Programming and Scripting', '10', '1', ['G400', 'G601'])
	add_module('G51SCI', 'Skills for Communicating Information', '10', '1', ['G400', 'G601'])
	add_module('G51DBS', 'Database Systems', '10', '1', ['G400', 'G601'])
	add_module('G51MCS', 'Mathematics for Computer Scientists', '10', '1', ['G400', 'G601'])
	add_module('G51APS', 'Algorithmic Problem Solving', '10', '1', ['G400', 'G601'])

	#============================MODULE INST.=======================================

	mod_list = [("G51FUN", "gmh"), ("G51WPS", "mjj"), ("G51SCI", "dfb"), ("G51DBS", "nza"), ("G51MCS", "rcb"), ("G51APS", "rcb")]
	y_list = [y1, y2, y3]
	s_list = [s1, s2, s3, s4, s5, s6]

	for (m_code, u_name) in mod_list:

		mod = Module.objects.get(code=m_code)

		for s in s_list:

			mi = ModuleInstance(
			module = mod,
			semester = s,
			convener = Person.objects.get(username=u_name),
			url = 'http://www.cs.nott.ac.uk/'
			)
			mi.save()

			mi.students.add(Person.objects.get(username='rxm08u'))
			mi.students.add(Person.objects.get(username='rjg08u'))
			mi.students.add(Person.objects.get(username='bxj08u'))

			mi.lecturers.add(Person.objects.get(username=u_name))

			mi.tutors.add(Person.objects.get(username='sda'))
			mi.tutors.add(Person.objects.get(username='ajr'))
			mi.tutors.add(Person.objects.get(username='gzt'))
			mi.tutors.add(Person.objects.get(username='azs'))
			mi.tutors.add(Person.objects.get(username='mvh'))
			mi.tutors.add(Person.objects.get(username='bzb'))
			mi.save()

	mod = Module.objects.get(code='G51PRG')

	for y in y_list:

		mi = ModuleInstance(
		module = mod,
		year = y,
		convener = Person.objects.get(username='srb'),
		url = 'http://www.cs.nott.ac.uk/'
		)
		mi.save()

		mi.students.add(Person.objects.get(username='rxm08u'))
		mi.students.add(Person.objects.get(username='rjg08u'))
		mi.students.add(Person.objects.get(username='bxj08u'))

		mi.lecturers.add(Person.objects.get(username='srb'))

		mi.tutors.add(Person.objects.get(username='sda'))
		mi.tutors.add(Person.objects.get(username='ajr'))
		mi.tutors.add(Person.objects.get(username='gzt'))
		mi.tutors.add(Person.objects.get(username='azs'))
		mi.tutors.add(Person.objects.get(username='mvh'))
		mi.tutors.add(Person.objects.get(username='bzb'))
		mi.save()
	#===========================COURSEWORKS=======================================


	#cswk = Coursework(module = mi,
	#	number = "1",
	#	title = "Large Coursework One",
	#	description = "Expand a regex Parser",
	#	time_set = datetime.datetime(2009,2,20),
	#	time_due = datetime.datetime(2009,3,20,17),
	#	url = "http://www.eprg.org/G51PRG/cswk.pdf",
	#	percentage = "8")
	#cswk.save()

	#cswk = Coursework(module = mi,
	#	number = "2",
	#	title = "Large Coursework Two",
	#	description = "Write a report about a Maths Parser",
	#	time_set = datetime.datetime(2009,3,30),
	#	time_due = datetime.datetime(2009,4,30,17),
	#	url = "http://www.eprg.org/G51PRG/cswk2.pdf",
	#	percentage = "8")
	#cswk.save()

if __name__ == "__main__":
    load_data()
