from os.path import join
import json
import csv
datadirect= "tempdata"
csvplace= join(datadirect, 'olympic_athletes.csv')
open_csv= open(csvplace, 'r')
dict_csv= csv.DictReader(open_csv)

intlist=[]
for row in dict_csv:
	intlist.append(row)

#Athlete,Age,Country,Year,Closing Ceremony Date,Sport,
#Gold Medals,Silver Medals,Bronze Medals,Total Medals

for x in range(len(intlist)):
	if intlist[x]['Age'] != '':
		intlist[x]['Age']=int(intlist[x]['Age'])
	intlist[x]['Gold Medals']=int(intlist[x]['Gold Medals'])
	intlist[x]['Silver Medals']=int(intlist[x]['Silver Medals'])
	intlist[x]['Bronze Medals']=int(intlist[x]['Bronze Medals'])
	intlist[x]['Total Medals']= int(intlist[x]['Total Medals'])

jsonplace = join(datadirect, 'olympic_athletes.json')
writejson=open(jsonplace, 'w')
json.dump(intlist, writejson, indent=2)
print("Writing to olympic_athletes.json file.")

