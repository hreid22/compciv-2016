from os.path import join
import json
datadirect='tempdata'
olympicpath=join(datadirect, 'olympic_athletes.json')
openoly=open(olympicpath, 'r')
readoly=openoly.read()
olydata= json.loads(readoly)

#olydata is a list of dictionaries, not yet callable by name

def extract_usable_name(name):
	nname = name.split(' ')[0]
	if "'" in nname:
		newname= nname.replace("'", "")
		return newname.capitalize()
	if "-" in nname:
		nnname= nname.replace("-", "")
		return nnname.capitalize()
	else:
		return nname.capitalize()

def no_weird_characters(weirdname):
	import unicodedata
	newname=unicodedata.normalize('NFKD', weirdname).encode('ASCII', 'ignore').decode()
	return newname

for y in range(len(olydata)):
	name=olydata[y]['Athlete']
	weirdname=extract_usable_name(name)
	finalname=no_weird_characters(weirdname)
	olydata[y]['usable_name']=finalname



namecaller={}
for x in range(len(olydata)):
	call=olydata[x]['usable_name']
	namecaller[call]=olydata[x]
from gender import detect_gender

for athlete in namecaller.keys():
	result=detect_gender(athlete)
	ratio=result['ratio']
	gender=result['gender']
	namecaller[athlete]['ratio']=ratio
	namecaller[athlete]['gender']=gender

olympicpath=join(datadirect, 'olympic_athletes_classified.json')
writejson=open(olympicpath, 'w')
json.dump(namecaller, writejson, indent=2)
print("Writing to olympic_athletes_classified.json file.")

