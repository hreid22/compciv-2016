import json
import os

mapzen = os.path.join( 'tempdata', 'mapzen', 'stanford.json')
mapzenplace = open(mapzen, 'r')
mread= mapzenplace.read()
mdict = json.loads(mread)

t = mdict["type"]

newdict = mdict["geocoding"]
ldict= newdict["query"]
a= ldict["text"]
b= ldict["size"]
c=ldict["boundary.country"]

print("type:", t)
print("text:", a)
print("size:", b)
print("boundary.country:", c)