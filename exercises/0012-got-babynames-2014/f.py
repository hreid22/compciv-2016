import os
babyplace= os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
babyopen= open(babyplace, 'r')

babydict = {}

for x in babyopen:
	name, sex, count = x.strip().split(',')
	last_letter= name[-1]
	
	if babydict.get(last_letter):
		babydict[last_letter]+= int(count)
	else:
		babydict[last_letter] = int(count)
import string

for x in string.ascii_lowercase:
	print(x+":", babydict[x])
