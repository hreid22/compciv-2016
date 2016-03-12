# Gender Detector Final Project: Olympic Athletes
## Introduction
* About the Dataset
	* This data set contains information on every medal winner in a summer or winter olympic games from 2000-2012. Data is formatted such that if an athlete attended multple olympic games they have an entry for each Olympic games during which they won at least a bronze medal. For instance, Michael Phelps is listed three times for the Summer Games in 2012, 2008, and 2004.
* Hypotheses
	* I will test how gender and age interact for Olympic athletes. Do men and women truly peak at different times?
	I propose to test this by looking at the ages of male versus female medalists (as gender-detected by my function) when they competed.
	* I also want to test what medals (gold, silver eg) males versus females of different ages are winning. This should get more at the success of the two sexes of athletes at different ages.
	* As the list of Olympic medalists contains a diverse name set (athletes are from all around the world) I am also interested in which countries have the most names that the gender detector does not recognize (returns 'gender'="NA" e.g.)
* Brief Analysis
	* Men and women peak at different times. The share of woman medalists falls with age (while the male share rises).
	* Females appear to win fewer gold medals as a percentage of total medals as they age.
	* Different coutries have the youngest medalists for men and women. 
	* China sends the most medalists who win medals with names that are not in the US SS data base.
	* Interestingly, there are 37 US medalists who have names were not recorded in the US social security data, which could indicate that these athletes are immigrants competing on behalf of the US (as well as any American athletes with nicknames or abbreviations not covered in the US SSA.)
	* The most decorated athlete at these Olympics is a man.

## Methodology
* Dataset 
	* The data's landing page: [CSV Olympic Athletes](http://ckan.whythawk.com/km/dataset/odata-test/resource/79b3b3f2-a3a2-48c0-8526-e01405bd2f73)
	* The data is in a csv format (8619 rows) and contains categories: athlete, age, country, year, closing ceremony date, sport, gold medals, silver medals, bronze medals, and total medals.
* Name Extraction
	* The dataset came with a field "Athletes" that included a string of the athlete's entire name. Thus, I first had to split the name to call only the first name (which is what my gender detector recognizes). To accomplish this I split the string at the first space. 
		* nname = name.split(' ')[0]
	* I then also wanted to get rid of any extraneous characters in the name such as hyphens or apostrophes that prevented names from being recognized by the SS trained gender detector (for instance Am'are in the Olympic data would not be recognized as the same as Amare in the SS data). 
		* if "-" in nname:
		-nnname= nname.replace("-", "")  E.G.
	* I also wanted to return a name that had one capital letter (the leading letter) and no other capitals. This was important for names like JJ which in the SS data is written as Jj.
		* nname.capitalize() #where nname is my formatted name string
	* For the last step in formatting the name I defined a new function to replace accents and other unicode characters that the US Social Security data does not include. The string fed into this function is the already split and modified name string from the steps above "Hélène eg." This function returns "Helene" from an input of Hélène.
		* def no_weird_characters(weirdname):
			- import unicodedata
			- newname=unicodedata.normalize('NFKD', weirdname).encode('ASCII', 'ignore').decode()
			- return newname
* Gender Classification
	* Athletes were classified by gender by using a gender detector generated from historical United States SS data. When an athlete's name is fed into the function it looks for that name in the database and compares the ratio of males to females born with that name. It then guesses the gender of the name based on whether historically males or females in the SS database had that name.
	* Unlike the previous assignment I included all years between 1950-2014 to create formatted json SS file off of which the gender detector is built.
* Limitations
	* One limitation that I did not deal with in my analysis (as I do not think it really affected the fields I was analyzing) is the fact that the same athlete may appear in this dataset multiple times if they attended multiple Olympics. In order to rectify this I could have tried to merge all records under the same name. Instead, however, I decided to treat each entry as "new athlete" in a different game. This also allowed me to consider their performance at different ages.
	* I am also limited by the preponderence of names in this dataset that are not recognized by my gender detector. The fact that the Olympics inherently have a diverse set of names (as a diverse set of athletes of all different nationalities compete) means that a significant portion of my names were classified as gender 'NA' by the gender detector. This was especially prominent for the China and the Netherlands.
	* Some athletes were also included in the dataset by either only a first intial or a nickname (ie Cat or A.). Unfortunately I could not generate their true first names based on this information thus they were also classified as gender "NA" using the gender detector.
	* Finally this data set includes only medal winners. In future analyses it would be useful to work with a larger dataset of all Olympic athletes to get a more rigorous comparison of differences between the sexes, not just the medal winners of each sex.

## Past Research
* The Atlantic [We Thought Female Athletes Were Catching Up to Men, but They're Not](http://www.theatlantic.com/technology/archive/2012/08/we-thought-female-athletes-were-catching-up-to-men-but-theyre-not/260927/)
	* Women and men clearly have different levels that they are physically able to attain in sports (the Atlantic article points to blood oxygen and hemoglobin levels as main determinants). However, for me this still left the question of at what ages men and women are reaching their different peaks.
* The Economist [Women against men](http://www.economist.com/blogs/graphicdetail/2012/08/daily-chart-olympics)
	* Contrary to the argument in The Atlantic, this Economist post proposes that the performance gap between women and men might be narrowing in some sports if not in others. My research relates to this article in a similar way as it does to The Atlantic article.
* The NYT [Gender Testing for Athletes Remains a Tough Call](http://www.nytimes.com/2012/06/18/sports/olympics/the-line-between-male-and-female-athletes-how-to-decide.html?_r=0)
	* Caster Semenya created a huge controversy after her record setting 800m run which led to questions about whether she should be allowed to compete against females due to her "masculine physique." This article proposes testosterone levels as a possible measure for differentiating between male and female athletes. This article underscores the idea that men's versus women's ability to perform in different athletic contests is of interest to a wide audience. The tests I run on the data look at women versus men's ability to perform at different ages as a proxy for when they are biologically peaking, a related aspect of male/female differences in sports.
* The Washington Post [How much do sex differences matter in sports?](https://www.washingtonpost.com/opinions/how-much-do-sex-differences-matter-in-sports/2014/02/07/563b86a4-8ed9-11e3-b227-12a45d109e03_story.html)
	* Another article exploring the idea of male/female sports performance. It concludes that for the majority of events male biology is simply too advantageous to overcome, which should not be viewed as a slight to women, nor a reason to keep them from competing in certain events. Simply men and women have different levels of attainable excellence in most sports. These differences are small prior to puberty, but the youngest athletes allowed to compete at the Olympics are 15 years old. I look at comparatively how age affects success of male and female atheltes in their respective genders, however due to the age restrictions of the Olympics all of my comparison occurs after puberty.
* Feminist Majority Foundation [Equality for Women in the Olympics](http://www.feminist.org/sports/olympics.asp)
	* While women have achieved greater equality in representation in sports (44% of the athletes at the London Summer 2012 games were women) they still face challenges in terms of outdated attitudes. The push for women to wear skirts while boxing to distinguish them from the male athletes being one such example. My analysis looks at the success of women as athletes over time and from which countries in order to probe at when and where female athletics have been most successful.
* A series of articles have been published in the past in Nature [Will women soon outrun men](http://www.nature.com/nature/journal/v355/n6355/abs/355025a0.html), and [Athletics:  Momentous sprint at the 2156 Olympics?](http://www.nature.com/nature/journal/v431/n7008/full/431525a.html) as well as the BMJ [Women will do it in the long run](http://bjsm.bmj.com/content/39/7/410.full).
	* These articles mainly argue about the likelihood of women attaining mens' records in various sports/distances of running. However many of the assertions made in the articles have been disproved by the plateau-ing of women's performance over time.
* It is clear that the participation of women in athletics has historically been a contentious issue. For the 32 years when women's long and middle distance running events were eliminated from the Olympics (fully reinstated in 2008) the justification was that the distance was simply too grueling for women's bodies. More recently we have seen a dispute arise over what defines a woman as a woman such that they can compete in female athletic events. While my analysis of this Olympic data using my US SS-trained gender detector is unable to comment on either women's biology at a scientific level, or give the definitive sex of athletes like Caster Semenya, it provides intersting analysis to complement this interesting and often debated subject. I focus on determinants like age and country of origin which I will further discuss in my analysis section.

## How to Use It
* Clone the repo from my github account
* Run the scripts in this order:
1. fetch_gender_data.py -- Running this script will fetch the SSA files on babies named since 1880, unzip them and store them under a the directory tempdata/
2. wrangle_gender_data.py -- Running this script will create a new json file (wrangledbabynames.json) under your tempdata directory which contains a list of dictionaries. Each dictionary represents one name that has appeared in the US SSA from 1950-2014. Each dictionary contains the fields {"females": # of females born with that name from 1950-2014, "males": # of males born with that name from 1950-2014, "gender": the gender the gender detector guesses for individuals with that name based on the ratio, "total": total # of babies born with that name between 1950-2014, "name": the name itself, and "ratio": if gender =='M' ratio= women/men or vice versa if gender =='F' (a ratio of 100 indicates that nearly all babies with the name were of one gender)}
3. fetch_data.py -- This script will download the Olympic data in csv format under the tempdata/ directory
4. wrangle_data.py -- This script will convert the Olympic csv file into a json format and also store it under the tempdata/ directory. Also converts all numeric values stored as strings in the csv to integers in the json file.
5. gender.py -- This script contains the gender detector built off of the US SSA data. For any name fed into detect_gender(name) it returns either the US SSA dictionary of that name (ie "Michael") with the fields as defined by the wrangle_gender_data.py script or if the name is not found in the US SSA it returns {'name': the name, 'gender': 'NA', 'ratio': 'None', 'males': 'None', 'females': 'None', 'total': 0}
6. classify.py -- This script creates a new json file of Olympic athletes with gender assigned by the detect_gender() function. It formats the names of the athletes in the Olympic csv to be recognized by the gender detector. The new json file is a list of dictionaries with each dictionary containing the same keys as the original Olympic csv with the addition of a "usable_name" key, a "ratio" key, and a "gender" key.
7. analyze.py -- This script runs a series of analyses on the classified json of Olympic athletes. See below for more detail on the output of the three analyses.

##Analysis
* My first analysis looks at what proportion of medal winners are male and female in 4 age brackets. The output looks like:
	- In these Olympics (2000-2012) athletes ages 15-61 were medal winners.
	- The ratio of women and men in these various age categories differed.
	- Of athletes 20 or younger there were:
	- 272 men and 411 women thus 39.8% of the medal winners were men.
	- Of athletes 20-30 years old there were:
	- 2828 men and 2369 women thus 54.4% of the medal winners were men.
	- Of athletes 30-40 years old there were:
	- 755 men and 515 women thus 59.4% of the medal winners were men.
	- Of over 40 years old there were:
	- 68 men and 39 women thus 63.6% of the medal winners were men.
* The proportion of female to male medalists decliens with age, perhaps indicaitng an earlier atheltic peak for women.
* My second analysis expands on the first by asking what medals are male and female athletes winning at different ages (gold, silver, bronze e.g.). I do this by normalizing the total number of medals won in each category by the number of male or female athletes competing in that category. For instance the first segment of output looks like:
	- Percentage breakdown of medals by age:
	- Age <= 20
	- Gold   Sliver   Bronze
	- M:        
	- 0.37      0.3     0.32
* This indicates that for male medal winners less than 20 years old 37% of the medals were gold medals, 30% were silver and 32% were bronze. The full output:
	- Percentage breakdown of medals by age:
	- Age <= 20
	- Gold   Sliver   Bronze
	- M:        
	- 0.37      0.3     0.32
	- F:        
	- 0.36     0.32     0.31
	- 20 < Age <= 30
	- Gold   Sliver   Bronze
	- M:        
	- 0.34     0.32     0.34
	- F:        
	- 0.31     0.33     0.35
	- 30 < Age <= 40
	- Gold   Sliver   Bronze
	- M:        
	- 0.31     0.36     0.33
	- F:        
	- 0.36     0.31     0.33
	- Age > 40
	- Gold   Sliver   Bronze
	- M:        
	- 0.35     0.32     0.33
	- F:        
	- 0.24     0.36      0.4
* Based on this data women seem to have a steeper decline in performance than men, although this is most pronounced only in the last age bracket.
* I then look at which countries are sending the youngest medal winners (proportional to total medal winners) and if these countries are the same between men and women. I find the following:
	- The top 5 countries with the most young female medalists proportional to total female medalists of that nationality in this selection of Olympic games were:
	- Moldova where 100.0%  of female medalists were <=20 years old.
	- Georgia where 100.0%  of female medalists were <=20 years old.
	- Zimbabwe where 50.0%  of female medalists were <=20 years old.
	- Turkey where 50.0%  of female medalists were <=20 years old.
	- North Korea where 40.0%  of female medalists were <=20 years old.
	- The top 5 countries with the most young male medalists proportional to total male medalists of that nationality in this selection of Olympic games were:
	- Botswana where 100.0%  of male medalists were <=20 years old.
	- Cameroon where 50.0%  of male medalists were <=20 years old.
	- Indonesia where 40.0%  of male medalists were <=20 years old.
	- Nigeria where 35.29%  of male medalists were <=20 years old.
	- Armenia where 28.57%  of male medalists were <=20 years old.
* As a check on the limitations of my data I also looked at which countries had the highest number of medalists' names not recognized by the gender detector. I find that China leads followed by the Netherlands. The full list of the top 10 is below:
	- The top 10 countries with the most names not recognized by the US SS Data trained gender detector were:
	- China with 171 athletes with names not recognized by US SS data.
	- Netherlands with 109 athletes with names not recognized by US SS data.
	- South Korea with 75 athletes with names not recognized by US SS data.
	- Russia with 71 athletes with names not recognized by US SS data.
	- Cuba with 60 athletes with names not recognized by US SS data.
	- Brazil with 57 athletes with names not recognized by US SS data.
	- Japan with 56 athletes with names not recognized by US SS data.
	- Finland with 50 athletes with names not recognized by US SS data.
	- Norway with 46 athletes with names not recognized by US SS data.
	- United States with 37 athletes with names not recognized by US SS data.
* Interestingly, as the United States was one of the countries with the largest absolute number of unrecognized names (yet the detector is built on data derived from the US SSA database) I wanted to know what these names were.
	- The names of the American athletes not recognized by the US SS Data trained gender detector were:
	- Klete
	- Klete
	- J.
	- Beezie
	- J.
	- Tayyiba
	- Lloy
	- Tayyiba
	- Ogonna
	- Breeja
	- Klete
	- Ritz
	- Rhi
	- B.
	- Staciana
	- J.
	- Tairia
	- Cat
	- Tairia
	- Cat
	- Pease
	- A.
	- Guard
	- Cat
	- Keeth
	- Beezie
	- Seimone
	- Swin
	- Seimone
	- Swin
	- Manteo
	- Hyleas
	- Bershawn
	- Meb
	- Moushaumi
	- Chryste
	- Nanceen
* As one can see from the above list some of these names were excluded as they are abbreviations or intials not recognized by the US SSA data. Others may be of athletes who were immigrants to the United States or who go by a nickname. This list also brings back one of the limitations of the data set in that the same medalist is included multiple times if they won medals at multiple Olympics. For instance Klete in the list above.
* As a last test I look at the most medals won by an individual female versus an individual male athlete in any single Olympics. 
	- The most medals won by one male athlete in any Olympics from 2000-2012 was 8
	- The most medals won by one female athlete in any Olympics from 2000-2012 was 6
* Thus the most decorated female athlete is less decorated than the most decorated male athlete in these Olympics.




