import os
hname = os.path.join('tempdata', 'tragedies', 'hamlet')
hamletfile = open(hname, 'r')
for x in range(5):
	print(hamletfile.readline().strip())
hamletfile.close()
