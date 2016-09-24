import os, sys

print "the director is: %s"%os.listdir(os.getcwd())

os.rename(filetorename, newfilename)

print "Sucessfully renamed"

print "the director is: %s"%os.listdir(os.getcwd())
