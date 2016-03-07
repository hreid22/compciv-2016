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
	x+=1
	openfile=open(file, 'r')
	namedict= {'M': set(), 'F': set(), 'B': set()}
	numberdict={'F':0, 'M':0, 'B':0}
	for line in openfile:
		name, gender, number = line.split(',')
		if gender == 'M':
			namedict['M'].add(name)
			namedict['B'].add(name)
			numberdict['M']+= int(number)
			numberdict['B'] += int(number)
		elif gender == 'F':
			namedict['F'].add(name)
			namedict['B'].add(name)
			numberdict['F']+= int(number)
			numberdict['B'] += int(number)
	if x % 5 == 0:
		print(x)
		print("Total:", round(numberdict['B']/len(namedict['B'])), "babies per name")
		print("    M:", round(numberdict['M']/len(namedict['M'])), "baibes per name")
		print("    F:", round(numberdict['F']/len(namedict['F'])), "babies per name")
