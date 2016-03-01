import os
from glob import glob
import json
picture_directory = 'pics'
response_directory = 'responses'

html_name = 'printout.html'
html_file = open(html_name, 'w')
html_file.write("<html><title>Hello</title><body>")
html_file.write("<h1>This is Hadley's IBM Watson Analysis Project</h1>")

for response in glob(os.path.join(response_directory, '*.json')):
	print("Extracting", response)
	hoo = json.load(open(response))
	image = hoo['images'][0]
	imgname = image['image']
	html_file.write("<h2>%s</2h>" % imgname)
	imagefilename = os.path.join('*', picture_directory, imgname)
	html_file.write('<li>'+'<img src="%s">' % imagefilename + '</li>')
	for x in range(len(image['scores'])):
		mylist=[]
		mylist.append('<li>' + image['scores'][x]['name']+ "---" + str(image['scores'][x]['score'])+"</li>")
		for y in range(len(mylist)):
			html_file.write(mylist[y])

html_file.close()

#formatting???