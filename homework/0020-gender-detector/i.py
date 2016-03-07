from os.path import join
datadirect= 'tempdata'
csvpath= join(datadirect, 'wrangled2014.csv')
import csv

popular=[]
with open(csvpath) as csvfile:
	readcsv= csv.DictReader(csvfile)
	for row in readcsv:
		if int(row['total']) >= 100:
			popular.append(row)
sixtylist=[]
seventylist=[]
eightylist= []
ninetylist=[]
ninetyninelist=[]
for x in range(len(popular)):
	if int(popular[x]['ratio']) <= 60:
		sixtylist.append(x)
	if int(popular[x]['ratio']) <= 70:
		seventylist.append(x)
	if int(popular[x]['ratio']) <= 80:
		eightylist.append(x)
	if int(popular[x]['ratio']) <= 90:
		ninetylist.append(x)
	if int(popular[x]['ratio']) <= 99:
		ninetyninelist.append(x)

print("Popular names in 2014 with gender ratio less than or equal to:")
print("60%: "+str(len(sixtylist))+"/"+str(len(popular)))
print("70%: "+str(len(seventylist))+"/"+str(len(popular)))
print("80%: "+str(len(eightylist))+"/"+str(len(popular)))
print("90%: "+str(len(ninetylist))+"/"+str(len(popular)))
print("99%: "+str(len(ninetyninelist))+"/"+str(len(popular)))