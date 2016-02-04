import requests
import os
data = requests.get("https://ndownloader.figshare.com/files/3230399")
dataplace = os.path.join('tempdata', 'ebola')
ebola_txt= data.text
ebola_open= open(dataplace, 'w')
ebola_open.write(ebola_txt)

#item #2 is Name of the location, #3 is country, #6 is point or polygon, #7 is lat, #8 is long
#9 is location notes
