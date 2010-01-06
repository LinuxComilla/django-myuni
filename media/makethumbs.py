from PIL import Image
import sys, os
import re

args = sys.argv

sizes = []
username = 0
infile = 0
force = False

for arg in args:
	if (re.match(r"^.*[jpg|png|gif]$",arg) != None):
		infile = arg
		print 'Using input file',arg
	if (re.match(r"^[0-9]+$",arg) != None):
		sizes.append(int(arg))
	if (re.match(r"^username=[0-9|a-z]+$",arg) != None):
		username = arg.split('=')[1]
		print "Using specified username:", username
	if (arg=='-f'):
		force = True

if (infile==0):
	print "I can't find a source image in the arguments. gif/jpg/png"
	sys.exit()

if (username==0):
	username = os.path.split(infile)[1].split('.')[0]
	print 'No username specified, using filename:', username

newdir = os.path.join('./people/',username)

print "Will make directory:", newdir
print "Containing", len(sizes), "thumbnails:",
for s in [(str(x)+"px.png") for x in sizes]: print s,
print

if not force:
	print "Proceed making directory and thumbnails? [y/n]",
	if (raw_input() != 'y'):
		sys.exit()

mainim = Image.open(infile)
try:
	os.mkdir(newdir)
except:
	pass


for size in sizes:
	print "doing size", size
	im = mainim.resize((size,size), Image.ANTIALIAS)
	newfilepath = os.path.join(newdir,str(size)+'px.png')
	im.save(newfilepath,'PNG')






