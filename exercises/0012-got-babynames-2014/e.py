import os
babyplace= os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
baby_open=open(babyplace, 'r')


countF=0
countM=0
for x in baby_open:
	mylist = x.split(',')
	if mylist[1] == "F":
		countF+=int(mylist[2])
	elif mylist[1] == "M":
		countM+=int(mylist[2])

print("F:", countF)
print("M:", countM)
