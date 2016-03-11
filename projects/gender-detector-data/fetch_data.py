import requests
import os
data = requests.get("http://ckan.whythawk.com/km/dataset/4e353550-9380-4be1-adc2-c02a5c1116fb/resource/79b3b3f2-a3a2-48c0-8526-e01405bd2f73/download/olympicathletes0.csv")
os.makedirs("tempdata", exist_ok=True)
dataplace = os.path.join('tempdata', 'olympic_athletes.csv')
athlete_txt= data.text
athlete_open= open(dataplace, 'w')
athlete_open.write(athlete_txt)
athlete_open.close()