import json
import os
gmap = os.path.join('tempdata', 'googlemaps', 'stanford.json')
file1 = open(gmap, 'r')
gtxt= file1.read()
file1.close()

gdict = json.loads(gtxt)

print(gdict['status'])