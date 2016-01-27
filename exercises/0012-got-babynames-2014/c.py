import os
babyplace=os.path.join('tempdata','ssa-babynames-nationwide-2014.txt')
babyfiles=open(babyplace)
countD=0
countK=0
for x in babyfiles:
	mylist=x.split(',')
	if mylist[0]=='Daenerys':
		countD+=int(mylist[2].strip())
	if "Khalees" in mylist[0]:
		countK+=int(mylist[2].strip())
	if "Khaless" in mylist[0]:
		countK+=int(mylist[2].strip())
print("Daenerys:", countD)
print("Khaleesi:", countK)
