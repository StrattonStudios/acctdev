import os

path = os.getcwd
filenames = ps.listdir(path)

for filename in filenames:
	os.rename(filename, filename.replace("","_").lower())

