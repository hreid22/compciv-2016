import requests
import os
os.makedirs("tempdata", exist_ok=True)
os.makedirs("tempdata/googlemaps", exist_ok=True)
os.makedirs("tempdata/mapzen", exist_ok=True)
gurl= "http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json"
gmaps_resp= requests.get(gurl)
gmaps_text= gmaps_resp.text
googlemapz = os.path.join("tempdata", "googlemaps", "stanford.json")
gmap_place=open(googlemapz, 'w')
gmap_place.write(gmaps_text)
glines=len(gmaps_text.splitlines())
gcharacters= len(gmaps_text)



print("---")
print("Dowloading from:", gurl)
print("Writing to:", googlemapz)
print("Wrote", glines, "lines and", gcharacters, "characters")


murl= "http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json"
mapzen_resp= requests.get(murl)
mapzen_text=mapzen_resp.text
mapzen1 = os.path.join("tempdata", "mapzen", "stanford.json")
mapzen_place = open(mapzen1, 'w')
mapzen_place.write(mapzen_text)
mapzen_place.close()
mlines=len(mapzen_text.splitlines())
mcharacters= len(mapzen_text)

print("---")
print("Dowloading from:", murl)
print("Writing to:", mapzen1)
print("Wrote", mlines, "lines and", mcharacters, "characters")