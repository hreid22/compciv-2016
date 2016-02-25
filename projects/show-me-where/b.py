import requests
import os
dataplace = os.path.join('tempdata', 'ebola')
batcage= open(dataplace, 'r')

import csv

pointdict= {}
polygondict = {}
ebolalist= list(csv.reader(batcage.splitlines()))
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