from os.path import join
import json
datadirect= 'tempdata'
olympicplace= join(datadirect, 'olympic_athletes_classified.json')
openoly=open(olympicplace, 'r')
readoly=openoly.read()
olydata= json.loads(readoly)

#3 different ways to analyze.
#Age differentials between athletes of different genders

young_women=0
young_men=0
young=0
med_women=0
med_men=0
old_women=0
old_men=0
ancient_women=0
ancient_men=0


for key in olydata.keys():
	if olydata[key]['Age'] !='' and olydata[key]['Age'] <= 20:
		if olydata[key]['gender']== 'M':
			young_men+=1
		if olydata[key]['gender']== 'F':
			young_women+=1
		if olydata[key]['gender'] == 'NA':
			young+=1
	elif olydata[key]['Age'] !='' and olydata[key]['Age'] <= 30:
		if olydata[key]['gender']== 'M':
			med_men+=1
		if olydata[key]['gender']== 'F':
			med_women+=1
	elif olydata[key]['Age'] !='' and olydata[key]['Age'] <= 40:
		if olydata[key]['gender']== 'M':
			old_men+=1
		if olydata[key]['gender']== 'F':
			old_women+=1
	elif olydata[key]['Age'] !='' and olydata[key]['Age'] > 40:
		if olydata[key]['gender']== 'M':
			ancient_men+=1
		if olydata[key]['gender']== 'F':
			ancient_women+=1
print("In these Olympics (2000-2012) athletes ages 15-61 competed.") 
print('The ratio of women and men in these various age categories differed.')
print("Of athletes 20 or younger there were:")
print(young_men, 'men and', young_women, 'women thus '+str(round(young_men/(young_women+young_men)*100, 1))+'% of the athletes were men.')
print("Of athletes 20-30 years old there were:")
print(med_men, 'men and', med_women, 'women thus '+str(round(med_men/(med_women+med_men)*100, 1))+'% of the athletes were men.')
print("Of athletes 30-40 years old there were:")
print(old_men, 'men and', old_women, 'women thus '+str(round(old_men/(old_men+old_women)*100, 1))+'% of the athletes were men.')
print("Of over 40 years old there were:")
print(ancient_men, 'men and', ancient_women, 'women thus '+str(round(ancient_men/(ancient_women+ancient_men)*100, 1))+'% of the athletes were men.')

#so now that we know the age break down what are people
#winning at different ages? When do people peak?
gym=0
sym=0
bym=0
gyw=0
syw=0
byw=0
gmm=0
smm=0
bmm=0
gmw=0
smw=0
bmw=0
gom=0
som=0
bom=0
gow=0
sow=0
bow=0
gam=0
sam=0
bam=0
gaw=0
saw=0
baw=0
for key in olydata.keys():
	a=olydata[key]
	if olydata[key]['Age'] !='' and olydata[key]['Age'] <= 20:
		if olydata[key]['gender']== 'M':
			gym+=a['Gold Medals']
			sym+=a['Silver Medals']
			bym+=a['Bronze Medals']
		if olydata[key]['gender']== 'F':
			gyw+=a['Gold Medals']
			syw+=a['Silver Medals']
			byw+=a['Bronze Medals']
	elif olydata[key]['Age'] !='' and olydata[key]['Age'] <= 30:
		if olydata[key]['gender']== 'M':
			gmm+=a['Gold Medals']
			smm+=a['Silver Medals']
			bmm+=a['Bronze Medals']
		if olydata[key]['gender']== 'F':
			gmw+=a['Gold Medals']
			smw+=a['Silver Medals']
			bmw+=a['Bronze Medals']
	elif olydata[key]['Age'] !='' and olydata[key]['Age'] <= 40:
		if olydata[key]['gender']== 'M':
			gom+=a['Gold Medals']
			som+=a['Silver Medals']
			bom+=a['Bronze Medals']
		if olydata[key]['gender']== 'F':
			gow+=a['Gold Medals']
			sow+=a['Silver Medals']
			bow+=a['Bronze Medals']
	elif olydata[key]['Age'] !='' and olydata[key]['Age'] > 40:
		if olydata[key]['gender']== 'M':
			gam+=a['Gold Medals']
			sam+=a['Silver Medals']
			bam+=a['Bronze Medals']
		if olydata[key]['gender']== 'F':
			gaw+=a['Gold Medals']
			saw+=a['Silver Medals']
			baw+=a['Bronze Medals']
print("How many medals are athletes of different sexes winning by age (per athlete competing?")
print("Age <= 20")
print("Gold".ljust(6), "Sliver".rjust(6), "Bronze".rjust(8))
print("M:".ljust(10))
print(str(round(gym/young_men,2)).ljust(6), str(round(sym/young_men,2)).rjust(6), str(round(bym/young_men,2)).rjust(8))
print("F:".ljust(10))
print(str(round(gyw/young_women,2)).ljust(6), str(round(syw/young_women,2)).rjust(6), str(round(byw/young_women,2)).rjust(8))
print("20 < Age <= 30")
print("Gold".ljust(6), "Sliver".rjust(6), "Bronze".rjust(8))
print("M:".ljust(10))
print(str(round(gmm/med_men,2)).ljust(6), str(round(smm/med_men,2)).rjust(6), str(round(bmm/med_men,2)).rjust(8))
print("F:".ljust(10))
print(str(round(gmw/med_women,2)).ljust(6), str(round(smw/med_women,2)).rjust(6), str(round(bmw/med_women,2)).rjust(8))
print("30 < Age <= 40")
print("Gold".ljust(6), "Sliver".rjust(6), "Bronze".rjust(8))
print("M:".ljust(10))
print(str(round(gom/old_men,2)).ljust(6), str(round(som/old_men,2)).rjust(6), str(round(bom/old_men,2)).rjust(8))
print("F:".ljust(10))
print(str(round(gow/old_women,2)).ljust(6), str(round(sow/old_women,2)).rjust(6), str(round(bow/old_women,2)).rjust(8))
print("Age > 40")
print("Gold".ljust(6), "Sliver".rjust(6), "Bronze".rjust(8))
print("M:".ljust(10))
print(str(round(gam/ancient_men,2)).ljust(6), str(round(sam/ancient_men,2)).rjust(6), str(round(bam/ancient_men,2)).rjust(8))
print("F:".ljust(10))
print(str(round(gaw/ancient_women,2)).ljust(6), str(round(saw/ancient_women,2)).rjust(6), str(round(baw/ancient_women,2)).rjust(8))

#Who is sending the youngest athletes? Are the same countries sending men and women?

newdict={}
for key in olydata.keys():
	if olydata[key]['Age'] !='' and olydata[key]['Age'] <= 20 and olydata[key]['gender']=='F':
		if newdict.get(olydata[key]['Country']):
			newdict[olydata[key]['Country']] += 1
		else:
			newdict[olydata[key]['Country']]=1 
tdict={}
for key in olydata.keys():
	if olydata[key]['Country'] in newdict.keys() and olydata[key]['gender']=='F':
		if tdict.get(olydata[key]['Country']):
			tdict[olydata[key]['Country']]+=1
		else:
			tdict[olydata[key]['Country']]=1
for key in newdict.keys():
	newdict[key]=round(newdict[key]/tdict[key]*100,2)

import operator 
tallyF_sorted = sorted(newdict.items(), key=operator.itemgetter(1), reverse=True)

newMdict={}
for key in olydata.keys():
	if olydata[key]['Age'] !='' and olydata[key]['Age'] <= 20 and olydata[key]['gender']=='M':
		if newMdict.get(olydata[key]['Country']):
			newMdict[olydata[key]['Country']] += 1
		else:
			newMdict[olydata[key]['Country']]=1 
tMdict={}
for key in olydata.keys():
	if olydata[key]['Country'] in newMdict.keys() and olydata[key]['gender']=='M':
		if tMdict.get(olydata[key]['Country']):
			tMdict[olydata[key]['Country']]+=1
		else:
			tMdict[olydata[key]['Country']]=1
for key in newMdict.keys():
	newMdict[key]=round(newMdict[key]/tMdict[key]*100,2)

import operator 
tallyF_sorted = sorted(newdict.items(), key=operator.itemgetter(1), reverse=True)
tallyM_sorted= sorted(newMdict.items(), key=operator.itemgetter(1), reverse=True)
print("The countries with the most young female athletes proportional to total athletes of that nationality in these Olympics were:")
for x in range(0,5):
	print(tallyF_sorted[x][0], "where", str(tallyF_sorted[x][1])+'%', " of female athletes competing were <=20 years old.")
print("The countries with the most young male athletes proportional to total athletes of that nationality in these Olympics were:")
for x in range(0,5):
	print(tallyM_sorted[x][0], "where", str(tallyM_sorted[x][1])+'%', " of male athletes competing were <=20 years old.")

#What countries have names that the US SS data does not recognize in terms of gender? At what freq?
nadict={}
for key in olydata.keys():
	if olydata[key]['gender'] == 'NA':
		if nadict.get(olydata[key]['Country']):
			nadict[olydata[key]['Country']]+=1
		else:
			nadict[olydata[key]['Country']]=1
na_order=sorted(nadict.items(), key=operator.itemgetter(1), reverse=True)
print("The top 10 countries with the most names not recognized by the US SS Data trained gender detector were:")
for x in range(0,10):
	print(na_order[x][0], "with", na_order[x][1], "athletes with names not recognized by US SS data.")

#For the US athletes what were the names that were not in the US SS database from 1950-2014
print("The names of the American athletes not recognized by the US SS Data trained gender detector were:")
for key in olydata.keys():
	if olydata[key]['gender'] == 'NA' and olydata[key]['Country']== "United States":
		print(olydata[key]['usable_name'])

#Do different sexes win different total numbers of medals?
medalM=[]
medalF=[]
for key in olydata.keys():
	if olydata[key]['gender'] == 'M':
		medalM.append(olydata[key]['Total Medals'])
	if olydata[key]['gender'] == 'F':
		medalF.append(olydata[key]['Total Medals'])
avgM=sum(medalM)/len(medalM)
avgF=sum(medalF)/len(medalF)
print("The average man wins", avgM, "medals per Olympic game.")
print("The average woman wins", avgF "medals per Olympic game.")

