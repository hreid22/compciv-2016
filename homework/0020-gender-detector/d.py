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
x=1949
for file in namefiles:
	openfile= open(file, 'r')
	x+=1
	print(x)
	namedict= {'M': set(), 'F': set()}
	for line in openfile:
		name, gender, number = line.split(',')
		if gender == 'M':
			namedict['M'].add(name)
		elif gender == 'F':
			namedict['F'].add(name)
	females= len(namedict['F'])
	males = len(namedict['M'])
	print("F:", str(females).rjust(6),"M:", str(males).rjust(6))
	ratio = round(females/males*100)
	print("F/M name ratio:", ratio)
	
