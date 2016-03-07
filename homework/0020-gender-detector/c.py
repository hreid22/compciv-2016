from os.path import join, basename
from glob import glob
datadirect= 'tempdata'
allfiles_path= join(datadirect, '*.txt')
allfiles_names = glob(allfiles_path)

namefiles= []
for filename in allfiles_names:
	bname = basename(filename)
	year = bname[3:7]
	if int(year) >= 1950:
		namefiles.append(filename)
namedict= {'M': set(), 'F': set()}
for file in namefiles:
	openfile=open(file, 'r')
	for line in openfile:
		name, gender, number = line.split(',')
		if gender == 'M':
			namedict['M'].add(name)
		elif gender == 'F':
			namedict['F'].add(name)

print("F:", str(len(namedict['F'])).rjust(6), 
	"M:", str(len(namedict['M'])).rjust(6))
ratio= round(len(namedict['F'])/len(namedict['M'])*100)
print("F/M name ratio:", ratio)

