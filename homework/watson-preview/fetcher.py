import requests
import os

pics_dir = 'pics'
os.makedirs(pics_dir, exist_ok=True)

urls_list = ['https://upload.wikimedia.org/wikipedia/commons/3/31/SlothDWA.jpg', 'https://upload.wikimedia.org/wikipedia/commons/c/cc/Strawberries_at_St._Joseph_Market_in_Barcelona.JPG',
'https://static.pexels.com/photos/8374/food-ice-cream.jpg', 'https://upload.wikimedia.org/wikipedia/commons/d/d7/Thai_Breakdancers.jpg',
'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/The_Beatles_and_Muhammad_Ali.jpg/1280px-The_Beatles_and_Muhammad_Ali.jpg',
'https://upload.wikimedia.org/wikipedia/commons/7/7f/Fireworks_DetroitWindsorIntlFreedomFest.jpg']

for x in urls_list:
	print('Downloading', x)
	image = requests.get(x)
	file_name = os.path.join('pics', os.path.basename(x))
	print("Saving to", file_name)
	with open(file_name, 'wb') as w:
		w.write(image.content)
