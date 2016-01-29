import json
import os
gmap= os.path.join('tempdata', 'googlemaps', 'stanford.json')
gmapplace= open(gmap, 'r')
gread= gmapplace.read()

gdict = json.loads(gread)
c=0
for k in gdict.keys():
	results=gdict[k] #fine for my purposes but how do you get a loop to iterate through and store all the different keys
	for x in range(len(results)):
		label = results[x]
		fun=type(label)
		if fun != str:
			for k in label.keys():
				if k == "address_components":
					mylist=label[k]
					for a in range(len(mylist)):
						newdict= mylist[a]
						for b in newdict:
							c+=1
							if c==1:
								component=newdict["long_name"]
							if c ==4 :
								component2 = newdict["long_name"]
							if c ==8 :
								component3 = newdict["long_name"]
							if c ==12 :
								component4 = newdict["long_name"]
							
print(component+";", component2+";", component3+";", component4)




