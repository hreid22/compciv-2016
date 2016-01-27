import os
import requests
os.makedirs("tempdata", exist_ok = True)
csv=requests.get("http://stash.compciv.org/congress/2016-01/sunlight-legislators.csv")
csv_files=os.path.join('tempdata', 'sunlight-legislators.csv')
csv_files_open=open(csv_files, 'wb')
csvdata= csv.content
csv_files_open.write(csvdata)
csv_files_open.close()
csv_files_open2=open(csv_files, 'r')
line_num=0
for line in csv_files_open2:
	line_num+=1
print("There are", line_num, "in", csv_files)