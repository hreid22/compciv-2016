import glob
import os
all_line_count=0
all_nonblank_line_count=0
all_paths= os.path.join('tempdata','**', '*')
all_files=glob.glob(all_paths)
for story in all_files:
	line_num=0
	notblank_line_num=0
	txtfile=open(story, 'r')
	for line in txtfile:
		line_num+=1
		if line.strip() != "":
			notblank_line_num+=1
	print(story, "has", notblank_line_num, "non-blank lines out of", line_num, "total lines")
	all_nonblank_line_count+=notblank_line_num
	all_line_count+=line_num
	txtfile.close
print("All together, Shakespeare's", len(all_files), "text files have:", all_nonblank_line_count, "non-blank lines out of", all_line_count, "total lines")
