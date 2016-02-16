import os
babyplace= os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
babyopen= open(babyplace, 'r')

babydict= {}

for baby in babyopen:
	name, sex, number= baby.strip().split(',')
	if babydict.get(name):
		babydict[name] += int(number)
	else:
		babydict[name] = int(number)

newbabylist= []
for key in babydict.keys():
	sublist= [key, babydict[key]]
	newbabylist.append(sublist)

def large(x):
	return x[1]

orderbaby=sorted(newbabylist, reverse=True, key=large)

total1=0
total2=0
total3=0
total4=0
total5=0

for x in range(0,10):
	total1+=int(orderbaby[x][1])
for y in range(10,100):
	total2+=int(orderbaby[y][1])
for z in range(100,1000):
	total3+=int(orderbaby[z][1])
for q in range(1000,10000):
	total4+=int(orderbaby[q][1])
for w in range(10000,30579):
	total5+=int(orderbaby[w][1])
fulltotal=0
for x in range(len(orderbaby)):
	fulltotal+=int(orderbaby[x][1])

mylist=[total1, total2, total3, total4, total5]

newlist=[]
for f in range(len(mylist)):
	newlist.append(mylist[f]/fulltotal)

finalist=[]
for g in range(len(newlist)):
	finalist.append(round((newlist[g]*100), 1))

print("Names 1 to 10:", finalist[0])
print("Names 11 to 100:", finalist[1])
print("Names 101 to 1000:", finalist[2])
print("Names 1001 to 10000:", finalist[3])
print("Names 10001 to 30579:", finalist[4])