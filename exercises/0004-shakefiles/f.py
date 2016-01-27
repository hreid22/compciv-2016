import os
fname = os.path.join("tempdata", "tragedies", "romeoandjuliet")
romjul= open(fname, 'r')
line_num=0
#for x in romjul:
	#line_num+=1
for x in range(4766-5):
	line_num+=1
	romjul.readline()
for line in romjul:
	line_num+=1
	realline= str(line_num)+": " +line.strip()
	print(realline)
romjul.close()
