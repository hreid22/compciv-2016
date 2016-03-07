import json
from os.path import join, basename
import csv
import json
datadirect="tempdata"
csvplace=join(datadirect, "wrangledbabynames.csv")

opencsv=open(csvplace, 'r')
reader = csv.reader(opencsv)
j=0
for row in reader:
	comma= ','.join(row)+'\n'
	j+=len(comma)
opencsv.close()

opencsv2= open(csvplace, 'r')
dictcsv=csv.DictReader(opencsv2)


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

readjson=open(jsonplace, 'r')
txt=readjson.read()

k=len(txt)


print("CSV has", j, "characters")
print("JSON has", k, "characters")
ratio=round(k/j,1)
print("JSON requires", ratio, "times more text characters than CSV")


