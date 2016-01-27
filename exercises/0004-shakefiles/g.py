import os
import glob
tragic_path = os.path.join('tempdata', 'tragedies', '*')
tragic_filenames = glob.glob(tragic_path)
for x in tragic_filenames:
	txtfile = open(x, 'r')
	line_num=0
	for line in txtfile:
		line_num+=1
	txtfile.close()
	print(x,"has", line_num, "lines")
	starting_line_num= line_num-5
	txtfile= open(x, 'r')
	for line_num in range(line_num):
		line=txtfile.readline()
		if line_num>= starting_line_num:
			the_line= str(line_num+1)+": "+line.strip()
			print(the_line)
	txtfile.close

