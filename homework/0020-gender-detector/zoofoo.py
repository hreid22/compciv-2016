def detect_gender(name):
	import json
	from os.path import join
	datadirect= 'tempdata'
	jsonplace=join(datadirect, 'wrangledbabynames.json')
	openjson=open(jsonplace, 'r')
	readjson=openjson.read()
	jsondata= json.loads(readjson)
#jsondata is a list of dictionaries containing name info
#we need to make each list item callable by name
#ie convert it into a dictionary
	calldict={}
	for h in range(len(jsondata)):
		key=jsondata[h]['name']
		calldict[key]=jsondata[h]
	name=name.capitalize()
	if name in calldict.keys():
		return calldict[name]
	else:
		return{'name': name, 'gender': 'NA', 'ratio': 'None', 'males': 'None', 'females': 'None', 'total': 0}
	
