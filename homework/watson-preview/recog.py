import requests
import os
from glob import glob
import json
api_address = 'https://gateway.watsonplatform.net/visual-recognition-beta/api/v2/classify'
pics_directory = 'pics'
response_dir = 'responses'
os.makedirs(response_dir, exist_ok= True)

params = {
	'version' : '2015-12-02'
}

default_headers = {
	'Accept' : 'application/json'
}

creds = json.load(open('creds_watson_visual.json'))
my_username = creds['credentials']['username']
my_password = creds['credentials']['password']
authorization = (my_username, my_password)

for x in glob(os.path.join(pics_directory, '*.jpg')):
	print("Testing", x)
	with open(x, 'rb') as image_info:
		image_dict = {}
		image_dict['images_file'] = (x, image_info)
		resp = requests.post(api_address, params= params,
			auth= authorization, headers= default_headers, files= image_dict)
		print(resp.status_code)
		if resp.status_code == 200:
			info = os.path.join(response_dir, os.path.basename(x+'.json'))
			print("Writing to:", info)
			with open(info, 'w') as n:
				n.write(resp.text)
		else:
			print("Error code was", resp.status_code, "-- not: 200")

