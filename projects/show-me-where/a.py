import requests
import os
data = requests.get("https://ndownloader.figshare.com/files/3230399")
dataplace = os.path.join('tempdata', 'ebola')
ebola_txt= data.text
ebola_open= open(dataplace, 'w')
ebola_open.write(ebola_txt)
ebola_open.close()

#item #2 is Name of the location, #3 is country, #6 is point or polygon, #7 is lat, #8 is long
#9 is location notes #16 is start day

#location=input("Where are you?")

batcage= open(dataplace, 'r')

import csv

pointdict= {}
polygondict = {}
ebolalist= list(csv.reader(ebola_txt.splitlines()))
for x in range(len(ebolalist)):
	if ebolalist[x][5] == "point":
		if pointdict.get(ebolalist[x][0]):
			pointdict[ebolalist[x][3]] += {'lat' : float(ebolalist[x][6]), 'longi': float(ebolalist[x][7])}
		else:
			pointdict[ebolalist[x][2]] = {'lat' : float(ebolalist[x][6]), 'longi': float(ebolalist[x][7])}
		#print("This case occurred at latitude", lat, "and longitude", longi, "in year", ebolalist[x][27])
	elif ebolalist[x][5] == "polygon":
		if polygondict.get(ebolalist[x][0]):
			polygondict[ebolalist[x][2]] += {'lat' : float(ebolalist[x][6]), 'longi': float(ebolalist[x][7])}
		else:
			polygondict[ebolalist[x][2]] = {'lat' : float(ebolalist[x][6]), 'longi': float(ebolalist[x][7])}
print(pointdict)

from urllib.request import urlretrieve
from urllib.parse import urlencode




#haversine