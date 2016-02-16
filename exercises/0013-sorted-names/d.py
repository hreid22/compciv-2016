import os
babyplace = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
babyopen= open(babyplace, 'r')

xbabylist= []

for x in babyopen:
	name, sex, number = x.strip().split(',')
	if 'x' in name.lower():
		sublist= [name, sex, number]
		xbabylist.append(sublist)

malexlist= []
femxlist= []

for a in range(len(xbabylist)):
	if xbabylist[a][1] == 'M':
		listo= [xbabylist[a][0], xbabylist[a][2]]
		malexlist.append(listo)
	elif xbabylist[a][1] == 'F':
		lista= [xbabylist[a][0], xbabylist[a][2]]
		femxlist.append(lista)


def makenumber(x):
	kiki= x[1]
	return int(kiki)

ordermale= sorted(malexlist, reverse=True, key= makenumber)
orderfemale = sorted(femxlist, reverse=True, key=makenumber)


numf=0
numm=0
print("Female")
for b in range(0,5):
	numf+=1
	print(str(numf)+".", orderfemale[b][0].ljust(18), orderfemale[b][1].rjust(4))
print("Male")
for c in range(0,5):
	numm+=1
	print(str(numm)+".", ordermale[c][0].ljust(17), ordermale[c][1].rjust(5))