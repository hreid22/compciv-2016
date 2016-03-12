# Gender Detector Final Project: Olympic Athletes
## Introduction
* About the Dataset
	* This data set contains information on every medal winner in a summer or winter olympic games from 2000-2012. Data is formatted such that if an athlete attended multple olympic games they have an entry for each Olympic games during which they won at least a bronze medal. For instance, Michael Phelps is listed three times for the Summer Games in 2012, 2008, and 2004.
* Hypotheses
	* I will test how gender and age interact for Olympic athletes. Do men and women truly peak at different times?
	I propose to test this by looking at the ages of male versus female athletes (as gender-detected by my function)when they compete.
	* I also want to test what medals males versus females of different ages are winning. This should get more at the success of the two sexes of athletes at different ages.
	* As the list of Olympic athletes contains a diverse name set (athletes are from all around the world) I am also interested in which countries have the most names that the gender detector does not recognize (returns 'gender'="NA" e.g.)
*Brief Analysis
	* Men and women peak at different times. The share of woman athletes falls with age (while the male share rises).
	* Men remain more constant in their performance as measured by the number of gold medals earned per male athlete of their age bracket medaling. By this I mean that up until the highest age bracket men consistently earn ~.3 medals per male athlete medaling in that category. WOmen on the other hand have a definitive peak in the 30-40 years old category.
	* Different coutries have the youngest successful (at least one medal) athletes for men and women. 
	* The Netherlands sends the most athletes who win medals with names that are not in the US SS data base.
	* Interestingly, there are 26 US athletes who have names were not recorded in the US social security data indicating that this data is incomplete. (Although some of these not found names appear to be nicknames or abbreviations)
	* Finally, men and women win a simlar number of medals per athlete per Olympic game.

## Methodology
* Dataset 
	* The data's landing page: [CSV Olympic Athletes](http://ckan.whythawk.com/km/dataset/odata-test/resource/79b3b3f2-a3a2-48c0-8526-e01405bd2f73)
	* The data is in a csv format (8619 rows) and contains categories: athlete, age, country, year, closing ceremony date, sport, gold medals, silver medals, bronze medals, and total medals.
* Name Extraction
	* The dataset came with a field "Athletes" that included a string of the athlete's entire name. Thus I first had to split the name to call only the first name (which is what my gender detector recognizes). To accomplish this I split the string at the first space. 
		* nname = name.split(' ')[0]
	* I then also wanted to get rid of any extraneous characters in the name such as hyphens or apostrophes that prevented names form being recognized by the SS trained gender detector (for instance Am'are in the Olympic data would not be recognized as the same as Amare in the SS data). 
		* if "-" in nname:
		nnname= nname.replace("-", "")  E.G.
	* I also wanted to return a name that had one capital letter (the leading letter) and no other capitals. This was important for names like JJ which in the SS data is written as Jj.
		* nname.capitalize() #where nname is my formatted name string
	* For the last step in formatting the name I defined a new function to replace accents and other unicode characters that the US Social Security data does not include. The string fed into this function is the already split and modified name string from the steps above "Hélène eg." This function returns "Helene" from an input of Hélène.
		* def no_weird_characters(weirdname):
			import unicodedata
			newname=unicodedata.normalize('NFKD', weirdname).encode('ASCII', 'ignore').decode()
			return newname
* Gender Classification
	* Athletes were classified by gender by using a gender detector generated from historical United States SS data. When an athlete's name is fed into the function it looks for that name in the database and compares the ratio of males to females born with that name. It then guesses the gender of the name based on whether historically males or females in the SS database had that name.
	* Unlike the previous assignment I included all years between 1950-2014 to create formatted SS file off of which the gender detector is built.
* Limitations
	* One limitation that I did not deal with in my analysis (as I do not think it really affected the fields I was analyzing) is the fact that the same athlete may appear in this dataset multiple times if they attended multiple Olympics. In order to rectify this I could have tried to merge all records under the same name. Instead, however, I decided to treat each entry as "new athlete" in a different game. This also allowed me to consider their performance at different ages.
	* I am also limited by the preponderence of names in this dataset that are not recognized by my gender detector. The fact that the Olympics inherently have a diverse set of naems (as a diverse set of athletes fo all different nationalities compete) means that a significant portion of my names were classified as gender 'NA' byt the gender detector. This was especially prominent for the Netherlands, Japan and Cuba.
	* Some athletes were also included in the data set by either only a first intial or a nickname (ie Cat or A.). Unfortunately I could not generate their true first names based on this information thus they were also classified as gender "NA" using the gender detector.
##Past Research


