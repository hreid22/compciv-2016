import json
import os

gmaps = os.path.join('tempdata', 'googlemaps', 'stanford.json')
gmapsplace= open(gmaps, 'r')
gread= gmapsplace.read()
gdict=json.loads(gread)

for k in gdict.keys():
	if k == "results":
		mylist = gdict[k]
		for x in range(len(mylist)):
			mydict=mylist[x]
			fa = mydict['formatted_address']
			for a in mydict:
				if a == "geometry":
					newdict= mydict[a]
					for c in newdict:
						if c == "location":
							lastdict= newdict[c]
							for d in lastdict:
								if d == "lng":
									longitude=lastdict[d]
								if d == "lat":
									latitude = lastdict[d]
print( fa+";"+str(longitude)+';'+str(latitude))

