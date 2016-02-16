import os
babyplace= os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
babyopen = open(babyplace, 'r')

babydict= {}

for baby in babyopen:
	name, sex, number= baby.strip().split(',')
	if babydict.get(name):
		babydict[name] += int(number)
	else:
		babydict[name] = int(number)


newbabylist= []
for key in babydict.keys():
	if int(babydict[key]) >= 2000:
		sublist= [key, babydict[key]]
		newbabylist.append(sublist)
	else:
		pass 		

def lengthsort(x):
	leng= x[0]
	return (len(leng), x[1])

orderedbaby=sorted(newbabylist, reverse=True, key=lengthsort)



for x in range(0,10):
	print(orderedbaby[x][0].ljust(18), str(orderedbaby[x][1]).rjust(5))

#for key in newbabydict.keys():
#	def lengthsort(x):
#		leng = x[key]
#		return len(leng)

#sorted(newbabydict, reverse=True, key=lengthsort)
		
#newbabydict.update({key : babydict[key]})

