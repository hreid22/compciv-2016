from os.path import join, basename
import csv
datadirect='tempdata'
csvpath= join(datadirect, 'wrangledbabynames.csv')

calldict={}
with open(csvpath, 'r') as csvfile:
	readcsv= csv.DictReader(csvfile)
	for row in readcsv:
		calldict[row['name']]=row

def whatgender(name):
	name=name.capitalize()
	if name in calldict.keys():
		return calldict[name]
	else:
		return {'name': name, 'gender': 'NA', 'ratio': 'None', 'males': 'None', 'females': 'None', 'total': 0}
namelist=['Michael', 'Kelly', 'Kanye', 'THOR', 'casey', 'Arya', 'ZZZblahblah']	
femaletotal=0
maletotal=0
f=0
m=0
n=0
for name in namelist:
	print(name, whatgender(name)['gender'], whatgender(name)['ratio'])
	if whatgender(name)['females'] != "None":
		femaletotal+=int(whatgender(name)['females'])
	if whatgender(name)['males'] != 'None':
		maletotal+=int(whatgender(name)['males'])
	if whatgender(name)['gender'] == 'F':
		f+=1
	if whatgender(name)['gender'] == 'M':
		m+=1
	if whatgender(name)['gender'] == "NA":
		n+=1
print("Total:")
print("F:", f, "M:", m, "NA:", n)
print("females:", femaletotal, "males:", maletotal)

