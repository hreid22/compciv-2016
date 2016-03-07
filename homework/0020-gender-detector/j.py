from os.path import basename, join
import csv
datadirect= 'tempdata'
wrangledbaby= join(datadirect, 'wrangledbabynames.csv')
headers= ['name', 'gender', 'ratio', 'females','males', 'total' ]

start=1950
stop= 2014
years=list(range(start, stop, 10))
years.append(2014)

namedict= {}
for year in years:
	filepath= join(datadirect, "yob"+str(year)+'.txt')
	print("Parsing", filepath)
	with open(filepath, 'r') as openbaby:
		for line in openbaby:
			name, gender, number= line.split(',')
			if not namedict.get(name):
				namedict[name]={'M':0, 'F':0}
			namedict[name][gender] += int(number)
namelist=[]
for name, number in namedict.items():
	newdict={'name':name, 'females': number['F'], 'males': number['M']}
	newdict['total']= newdict['females']+newdict['males']
	if newdict['females'] >= newdict['males']:
		newdict['gender']='F'
		newdict['ratio']= round(newdict['females']/newdict['total']*100)
	if newdict['males'] >= newdict['females']:
		newdict['gender']= 'M'
		newdict['ratio']= round(newdict['males']/newdict['total']*100)
	namelist.append(newdict)

def ascending(newdict):
	return (-newdict['total'], newdict['name'])

sortedlist= sorted(namelist, key=ascending)

writefile= open(wrangledbaby, 'w')
writecsv= csv.DictWriter(writefile, fieldnames=headers)
writecsv.writeheader()
for row in sortedlist:
	writecsv.writerow(row)
writefile.close()

openeye= open(wrangledbaby, 'r')
textlines= openeye.readlines()[0:5]
for line in textlines:
	print(line.strip())


