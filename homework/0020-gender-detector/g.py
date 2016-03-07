from os.path import join, basename
import csv
datadirect= 'tempdata'
filepath = join(datadirect, "yob2014.txt")

csv_headers=['year', 'name', 'gender', 'ratio', 'females','males', 'total']
csvpath= join(datadirect, 'wrangled2014.csv')

namesdict = {}
openfile= open(filepath, 'r')
for line in openfile:
	name, gender, number = line.split(',')
	if not namesdict.get(name):
		namesdict[name]= {'M':0, 'F':0}
	namesdict[name][gender] += int(number)


csvlist = []
for name, number in namesdict.items():
	newdict={}
	newdict['year']= 2014
	newdict['name']= name
	newdict['males']= namesdict[name]['M']
	newdict['females']= number['F']
	newdict['total']=newdict['males']+newdict['females']
	if newdict['females']>= newdict['males']:
		newdict['gender']= 'F'
		newdict['ratio']= round(newdict['females']/newdict['total']*100)
	else:
		newdict['gender']= 'M'
		newdict['ratio']= round(newdict['males']/newdict['total'] * 100)
	csvlist.append(newdict)

def ascending(newdict):
	return (-newdict['total'], newdict['name'])

final= sorted(csvlist, key=ascending)

wfile=open(csvpath, 'w')
writecsv= csv.DictWriter(wfile, fieldnames=csv_headers)
writecsv.writeheader()
for row in final:
	writecsv.writerow(row)
wfile.close()

openeye= open(csvpath, 'r')
textlines= openeye.readlines()[0:5]
for line in textlines:
	print(line.strip())


