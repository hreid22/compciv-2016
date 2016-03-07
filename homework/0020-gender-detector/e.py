from os.path import join, basename
from glob import glob
datadirect= 'tempdata'
filepath= join(datadirect, 'yob2014.txt')
openbaby= open(filepath, 'r')

namedict={'F': set(), 'M': set(), 'B': set()}
numberdict={'F':0, 'M':0}
for line in openbaby:
	name, gender, number = line.split(',')
	namedict['B'].add(name)
	if gender == "M":
		namedict['M'].add(name)
		numberdict['M']+= int(number)
	if gender == 'F':
		namedict['F'].add(name)
		numberdict['F']+= int(number)
total= len(namedict['B'])
total2 = int(numberdict['M'])+numberdict['F']
print("Total:", total, "unique names for", total2, "babies")
print("    M:", len(namedict['M']), "unique names for", numberdict['M'], "babies")
print("    F:", len(namedict['F']), "unique names for", numberdict['F'], "babies")




