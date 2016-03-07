from zoofoo import detect_gender

namelist=['Michael', 'Kelly', 'Kanye', 'THOR', 'casey', 'Arya', 'ZZZblahblah']
f=0
m=0
u=0
females=0
males=0
for name in namelist:
	persondict=detect_gender(name)
	print(name, persondict['gender'], persondict['ratio'])
	if persondict['gender']=='F':
		f+=1
		females+=persondict['females']
		males+=persondict['males']
	elif persondict['gender']== 'M':
		m+=1
		males+=persondict['males']
		females+=persondict['females']
	else:
		u+=1
print("Total:")
print("F:", f, "M:", m, "NA:", u)
print("females:", females, "males:", males)
