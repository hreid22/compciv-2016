import requests
import json
def geocode(location):

	"""
	This function will aim to geocode a location string from a data file using Mapzen Search APO

	What it expects:
	----------------
	It expects that location is a string entered by the user for instance "New York CIty, NY"

	It also expects that `CREDS_FILE` points to an existing file that contains my valid Mapzen API search key

	What it does:
	-------------
	This funciton opens and reads the file at CREDS_FILE to find the Mapzen API key
	This function calls the Mapzen Search API via a HTTP request, using the API key from the CREDS_FILE, and the
	`location` that the user provides as the text parameter in the query.
	This function deserializes the MApzen search repsonse into a dictionary (object type), using the JSON library
	Finally it creates a dictionary.

	What it returns:
	-----------------
	Object type: dictionary
	Containing:
	- query_text: sting, the `location` text entered by the user
	-label: string, label that Mapzen provides to describe the location it identifies
	-confidence: float, value representing the poercent confidence Mapzen has in its result
	-latitude: float, value representing the latitude coordinate
	-longitude: float, value representing the longitude coordinate
	-status: string, "OK" if result was found, "None" if no result was found
	"""

	begin = fetch_mapzen_response(location)

	mapdict= parse_mapzen_response(begin)

	mapdict['query_string']= location
	return mapdict

def fetch_mapzen_response(location):

	"""
	`location` is a string entered by the user that will be passed to the Mapzen API for geocoding

	What it returns:
	-----------------
	A text stirng of the raw JSON data form Mapzen
	"""
	url= "https://search.mapzen.com/v1/search?"
	credkey = read_mapzen_credentials()
	my_params = { 'text': location, 'api_key': credkey}
	data = requests.get(url, params= my_params)
	data.txt= data.text
	return data.txt

def parse_mapzen_response(txt):
	"""
	This function will transform a JSON string into a well-formatted dictionary of key values

	What it Expects:
	----------------
	`txt` is a user entered string containing a JSON-formatted Mapzepn API (comes from fetch_mapzen_response)

	What it Returns:
	----------------
	-a dictionary of the relevant repsonses from the Mapzen API for gecoding
	"""
	firstdict={}
	mapresults = json.loads(txt)
	if mapresults['features']:
		firstdict['status'] = "OK"
		umbrella = mapresults['features'][0]
		properties = umbrella['properties']
		firstdict['confidence'] = properties['confidence']
		firstdict['label'] = properties['label']

		coordinates = umbrella['geometry']['coordinates']
		firstdict['latitude'] = coordinates[0]
		firstdict['longitude'] = coordinates[1]
	else:
		firstdict['status'] = "None"

	return firstdict

def read_mapzen_credentials():
	"""
	Reads my Mapzen API credentials from a seperate file and stores them as a string
	"""
	cred_place = "creds_mapzen.txt"
	credkey = open(cred_place).read().strip()
	return credkey


