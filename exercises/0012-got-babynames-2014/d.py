import os
babyplace= os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
babyfiles=open(babyplace, 'r')
linenum=0
women=0
for x in babyfiles:
	mylist=x.split(',')
	linenum+=1
	if linenum==1:
		print("Top baby girl names")
	if linenum<=5:
		print(str(linenum)+".", mylist[0], mylist[2].strip())
	if mylist[1]=='F':
		women+=1

print("")

babyfiles.close()
babyfiles=open(babyplace, 'r')
linecount=0
for b in babyfiles:
	mylist=b.split(',')
	linecount+=1
	if linecount == women:
		print("Top baby boy names")
	if linecount>19067 and linecount <= 19072:
		print(str(linecount-women)+".", mylist[0], mylist[2].strip())
