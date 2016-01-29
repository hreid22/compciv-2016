import json
import os

mapzen = os.path.join('tempdata', 'mapzen', 'stanford.json')
mapzenplace= open(mapzen, 'r')
mread=mapzenplace.read()
mdict= json.loads(mread)



alist=mdict["features"]
for a in range(len(alist)):
	places=alist[a]["properties"]["label"]
	conf= alist[a]["properties"]["confidence"]
	longi= alist[a]["geometry"]["coordinates"][0]
	lati=alist[a]["geometry"]["coordinates"][1]
	print(places+";"+str(conf)+";"+str(longi)+";"+str(lati))


	
	