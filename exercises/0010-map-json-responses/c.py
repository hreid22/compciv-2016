import os
import json
gmap = os.path.join('tempdata', 'googlemaps', 'stanford.json')
file1 = open(gmap, 'r')
gtxt= file1.read()
file1.close()

gdict = json.loads(gtxt)

a=gdict['results']
for x in range(1): 
	b= a[x]
	print(b['formatted_address'])

	