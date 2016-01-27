import os
babyplace = os.path.join("tempdata", os.path.basename("http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt"))
baby_open=open(babyplace, 'r')
count=0
for x in baby_open:
	mylist=x.split(',')
	num=mylist[2].strip()
	nummy=int(num)
	count+=nummy

print("There are", count, "babies whose names were recorded in 2014")
