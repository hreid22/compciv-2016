from os.path import basename, join
import csv
import json
datadirect= 'tempdata'
wrangledbaby= join(datadirect, 'wrangledbabynames.csv')
headers= ['name', 'gender', 'ratio', 'females','males', 'total' ]

start=1950
stop= 2015
years=list(range(start, stop))

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

csvplace=join(datadirect, "wrangledbabynames.csv")

opencsv=open(csvplace, 'r')
dictcsv=csv.DictReader(opencsv)


newlist=[]
for row in dictcsv:
	newlist.append(row)
for x in range(len(newlist)):
	newlist[x]['ratio']=int(newlist[x]['ratio'])
	newlist[x]['females']=int(newlist[x]['females'])
	newlist[x]['males']=int(newlist[x]['males'])
	newlist[x]['total']=int(newlist[x]['total'])

jsonplace=join(datadirect, 'wrangledbabynames.json')
writejson=open(jsonplace, 'w')
json.dump(newlist, writejson, indent=2)
writejson.close()