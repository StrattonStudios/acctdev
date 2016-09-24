import os, sys
import shutils
#import pdf reader, pyxlb, and others

#Global Vars
path = os.getcwd
filenames = ps.listdir(path)


#Boolean Variables
filetorename = None
src = None;
dest = None;

# duh moves file
def filemove(src, dest):
	shutils.move(src, dest)

# duh renames file
def filerename(self):
	print "the director is: %s"%os.listdir(os.getcwd())
	#os.listdir(os.getcwd()) ---- i dont think i need this
	os.rename(filetorename, newfilename)
	print "Sucessfully renamed"
	print "the director is: %s"%os.listdir(os.getcwd())


#updates the text of a document with a replacement string that is prompted for
def fileyears():
	filetoprocess = raw_input("Enter the file to be processed:")
	oldyear = raw_input("Enter the outdated year: ")
	newyear = raw_input("Enter the replacing year: ")
	newfilename = raw_input("Save file as: ")

	with open(filetoprocess, 'r') as file :
    	filedata = file.read()
    	print filedata

	# Replace the target string
	filedata = filedata.replace(oldyear,newyear)
	print filedata

	# Write the file out again
	with open(newfilename, 'w') as file:
    	file.write(filedata)


#Removes all spaces in files and replaces them with underscores
def underscorefile():
	path = os.getcwd
	filenames = ps.listdir(path)

	for filename in filenames:
		os.rename(filename, filename.replace("","_").lower())

def walktree():

def parsepdf():
	
	#Find header info
	#Seperate each item under withdraws
	#break it in to useful chuncks i.e.
	def vendor():
	def amount():
	def date():
		return data

