import os
babyplace= os.path.join("tempdata", os.path.basename("http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt"))
baby_open= open(babyplace, 'r')
baby_list=[]
for line in baby_open:
	name, sex, number = line.strip().split(',')
	sublist = [name, sex, int(number)]
	baby_list.append(sublist)

def sort_baby(x):
	return x[-1]

newlist= sorted(baby_list, reverse= True, key=sort_baby)

num=0
for x in range(0, 10):
	num+=1
	print(str(num)+'.', newlist[x][0]+','+newlist[x][1]+','+str(newlist[x][2]))
