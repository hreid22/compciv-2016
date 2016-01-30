import os
babyplace=os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
babyopen=open(babyplace, 'r')

babydict = { 'M':{}, 'F':{}}


for x in babyopen:
	name, sex, count = x.strip().split(",")
	last_letter= name[-1]
	if sex == "M":
		if babydict['M'].get(last_letter):
			babydict['M'][last_letter]+= int(count)
		else:
			babydict['M'][last_letter]= int(count)
	if sex == "F":
		if babydict['F'].get(last_letter):
			babydict['F'][last_letter]+= int(count)
		else:
			babydict['F'][last_letter]= int(count)

print("letter".ljust(8), "F".rjust(8), "M".rjust(8))
print("------------------------")
import string
for letter in string.ascii_lowercase:
	print(letter.ljust(8), str(babydict['F'][letter]).rjust(8), str(babydict['M'][letter]).rjust(8))
