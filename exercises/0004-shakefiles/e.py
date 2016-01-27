import os
filename = os.path.join('tempdata', 'tragedies', 'hamlet')
hamletfile=open(filename, 'r')
line_num=0
for x in hamletfile:
	line_num+=1
hamletfile.close()
print(filename, "has", line_num, "lines")
