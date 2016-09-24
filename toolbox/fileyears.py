# Read in the file
import easygui

filedata = None

print "Hello welcome to the proforma Beta"

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

