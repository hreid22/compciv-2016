
boldx = "\033[1m"
boldy = "\033[0m"
from utils.geocoding import geocode, fetch_mapzen_response, parse_mapzen_response
command_txt= input("What do you want to do? ")

if command_txt == "hello":
	usr_txt = input("What is your name? ")
	print("Hello", boldx + usr_txt + boldy)
elif command_txt == "geocode":
	usr_coordinates = input("What is your location? ")
	print("OK...geocoding", usr_coordinates)
	georesult = geocode(usr_coordinates)
	print(georesult)
elif command_txt == 'help':
	print(geocode.__name__)
	print(geocode.__doc__)
else:
	print("Sorry, I don't know how to respond to", command_txt)