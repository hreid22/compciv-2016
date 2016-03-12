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


for x in range(len(olydata)):
	if olydata[x]['Age'] !='' and olydata[x]['Age'] <= 20:
		if olydata[x]['gender']== 'M':
			young_men+=1
		if olydata[x]['gender']== 'F':
			young_women+=1
		if olydata[x]['gender'] == 'NA':
			young+=1
	elif olydata[x]['Age'] !='' and olydata[x]['Age'] <= 30:
		if olydata[x]['gender']== 'M':
			med_men+=1
		if olydata[x]['gender']== 'F':
			med_women+=1
	elif olydata[x]['Age'] !='' and olydata[x]['Age'] <= 40:
		if olydata[x]['gender']== 'M':
			old_men+=1
		if olydata[x]['gender']== 'F':
			old_women+=1
	elif olydata[x]['Age'] !='' and olydata[x]['Age'] > 40:
		if olydata[x]['gender']== 'M':
			ancient_men+=1
		if olydata[x]['gender']== 'F':
			ancient_women+=1
print("In these Olympics (2000-2012) athletes ages 15-61 were medal winners.") 
print('The ratio of women and men in these various age categories differed.')
print("Of athletes 20 or younger there were:")
print(young_men, 'men and', young_women, 'women thus '+str(round(young_men/(young_women+young_men)*100, 1))+'% of the medal winners were men.')
print("Of athletes 20-30 years old there were:")
print(med_men, 'men and', med_women, 'women thus '+str(round(med_men/(med_women+med_men)*100, 1))+'% of the medal winners were men.')
print("Of athletes 30-40 years old there were:")
print(old_men, 'men and', old_women, 'women thus '+str(round(old_men/(old_men+old_women)*100, 1))+'% of the medal winners were men.')
print("Of over 40 years old there were:")
print(ancient_men, 'men and', ancient_women, 'women thus '+str(round(ancient_men/(ancient_women+ancient_men)*100, 1))+'% of the medal winners were men.')

#so now that we know the age break down what are people winning at different ages? When do people peak?
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
tym=0
tyw=0
tmm=0
tmw=0
tom=0
tow=0
tam=0
taw=0
for z in range(len(olydata)):
	a=olydata[z]
	if a['Age'] !='' and a['Age'] <= 20:
		if a['gender']== 'M':
			gym+=a['Gold Medals']
			sym+=a['Silver Medals']
			bym+=a['Bronze Medals']
			tym+=a['Total Medals']
		if a['gender']== 'F':
			gyw+=a['Gold Medals']
			syw+=a['Silver Medals']
			byw+=a['Bronze Medals']
			tyw+=a['Total Medals']
	elif a['Age'] !='' and a['Age'] <= 30:
		if a['gender']== 'M':
			gmm+=a['Gold Medals']
			smm+=a['Silver Medals']
			bmm+=a['Bronze Medals']
			tmm+=a['Total Medals']
		if a['gender']== 'F':
			gmw+=a['Gold Medals']
			smw+=a['Silver Medals']
			bmw+=a['Bronze Medals']
			tmw+=a['Total Medals']
	elif a['Age'] !='' and a['Age'] <= 40:
		if a['gender']== 'M':
			gom+=a['Gold Medals']
			som+=a['Silver Medals']
			bom+=a['Bronze Medals']
			tom+=a['Total Medals']
		if a['gender']== 'F':
			gow+=a['Gold Medals']
			sow+=a['Silver Medals']
			bow+=a['Bronze Medals']
			tow+=a['Total Medals']
	elif a['Age'] !='' and a['Age'] > 40:
		if a['gender']== 'M':
			gam+=a['Gold Medals']
			sam+=a['Silver Medals']
			bam+=a['Bronze Medals']
			tam+=a['Total Medals']
		if a['gender']== 'F':
			gaw+=a['Gold Medals']
			saw+=a['Silver Medals']
			baw+=a['Bronze Medals']
			taw+=a['Total Medals']
print("Percentage breakdown of medals by age:")
print("Age <= 20")
print("Gold".ljust(6), "Sliver".rjust(6), "Bronze".rjust(8))
print("M:".ljust(10))
print(str(round(gym/tym,2)).ljust(6), str(round(sym/tym,2)).rjust(6), str(round(bym/tym,2)).rjust(8))
print("F:".ljust(10))
print(str(round(gyw/tyw,2)).ljust(6), str(round(syw/tyw,2)).rjust(6), str(round(byw/tyw,2)).rjust(8))
print("20 < Age <= 30")
print("Gold".ljust(6), "Sliver".rjust(6), "Bronze".rjust(8))
print("M:".ljust(10))
print(str(round(gmm/tmm,2)).ljust(6), str(round(smm/tmm,2)).rjust(6), str(round(bmm/tmm,2)).rjust(8))
print("F:".ljust(10))
print(str(round(gmw/tmw,2)).ljust(6), str(round(smw/tmw,2)).rjust(6), str(round(bmw/tmw,2)).rjust(8))
print("30 < Age <= 40")
print("Gold".ljust(6), "Sliver".rjust(6), "Bronze".rjust(8))
print("M:".ljust(10))
print(str(round(gom/tom,2)).ljust(6), str(round(som/tom,2)).rjust(6), str(round(bom/tom,2)).rjust(8))
print("F:".ljust(10))
print(str(round(gow/tow,2)).ljust(6), str(round(sow/tow,2)).rjust(6), str(round(bow/tow,2)).rjust(8))
print("Age > 40")
print("Gold".ljust(6), "Sliver".rjust(6), "Bronze".rjust(8))
print("M:".ljust(10))
print(str(round(gam/tam,2)).ljust(6), str(round(sam/tam,2)).rjust(6), str(round(bam/tam,2)).rjust(8))
print("F:".ljust(10))
print(str(round(gaw/taw,2)).ljust(6), str(round(saw/taw,2)).rjust(6), str(round(baw/taw,2)).rjust(8))

#Who is sending the youngest athletes? Are the same countries sending men and women?

newdict={}
for h in range(len(olydata)):
	if olydata[h]['Age'] !='' and olydata[h]['Age'] <= 20 and olydata[h]['gender']=='F':
		if newdict.get(olydata[h]['Country']):
			newdict[olydata[h]['Country']] += 1
		else:
			newdict[olydata[h]['Country']]=1 
tdict={}
for i in range(len(olydata)):
	if olydata[i]['Country'] in newdict.keys() and olydata[i]['gender']=='F':
		if tdict.get(olydata[i]['Country']):
			tdict[olydata[i]['Country']]+=1
		else:
			tdict[olydata[i]['Country']]=1
for key in newdict.keys():
	newdict[key]=round(newdict[key]/tdict[key]*100,2)

import operator 
tallyF_sorted = sorted(newdict.items(), key=operator.itemgetter(1), reverse=True)

newMdict={}
for j in range(len(olydata)):
	if olydata[j]['Age'] !='' and olydata[j]['Age'] <= 20 and olydata[j]['gender']=='M':
		if newMdict.get(olydata[j]['Country']):
			newMdict[olydata[j]['Country']] += 1
		else:
			newMdict[olydata[j]['Country']]=1 
tMdict={}
for l in range(len(olydata)):
	if olydata[l]['Country'] in newMdict.keys() and olydata[l]['gender']=='M':
		if tMdict.get(olydata[l]['Country']):
			tMdict[olydata[l]['Country']]+=1
		else:
			tMdict[olydata[l]['Country']]=1
for key in newMdict.keys():
	newMdict[key]=round(newMdict[key]/tMdict[key]*100,2)

import operator 
tallyF_sorted = sorted(newdict.items(), key=operator.itemgetter(1), reverse=True)
tallyM_sorted= sorted(newMdict.items(), key=operator.itemgetter(1), reverse=True)
print("The top 5 countries with the most young female medalists proportional to total female medalists of that nationality in this selection of Olympic games were:")
for x in range(0,5):
	print(tallyF_sorted[x][0], "where", str(tallyF_sorted[x][1])+'%', " of female medalists were <=20 years old.")
print("The top 5 countries with the most young male medalists proportional to total male medalists of that nationality in this selection of Olympic games were:")
for x in range(0,5):
	print(tallyM_sorted[x][0], "where", str(tallyM_sorted[x][1])+'%', " of male medalists were <=20 years old.")

#What countries have names that the US SS data does not recognize in terms of gender? At what freq?
nadict={}
for k in range(len(olydata)):
	if olydata[k]['gender'] == 'NA':
		if nadict.get(olydata[k]['Country']):
			nadict[olydata[k]['Country']]+=1
		else:
			nadict[olydata[k]['Country']]=1
na_order=sorted(nadict.items(), key=operator.itemgetter(1), reverse=True)
print("The top 10 countries with the most names not recognized by the US SS Data trained gender detector were:")
for x in range(0,10):
	print(na_order[x][0], "with", na_order[x][1], "athletes with names not recognized by US SS data.")

#For the US athletes what were the names that were not in the US SS database from 1950-2014
print("The names of the American athletes not recognized by the US SS Data trained gender detector were:")
for m in range(len(olydata)):
	if olydata[m]['gender'] == 'NA' and olydata[m]['Country']== "United States":
		print(olydata[m]['usable_name'])

#Do different sexes win different total numbers of medals?
medalM=[]
medalF=[]
for n in range(len(olydata)):
	if olydata[n]['gender'] == 'M':
		medalM.append(olydata[n]['Total Medals'])
	if olydata[n]['gender'] == 'F':
		medalF.append(olydata[n]['Total Medals'])
sortM=sorted(medalM, reverse=True)
sortF=sorted(medalF, reverse=True)

print("The most medals won by one male athlete in any Olympics from 2000-2012 was", sortM[0])
print("The most medals won by one female athlete in any Olympics from 2000-2012 was", sortF[0])

