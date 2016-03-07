#Gender Detector: About the Dataset
This data set contains information on every medal winner in a summer or winter olympic games from 2000-2012. Data is characterized such that if an athlete attended multple olympic games they have an entry for each Olympic games during which they won at least a bronze medal. For instance, Michael Phelps is listed three times for the Summer Games in 2012, 2008, and 2004.
##Basic facts about the dataset
- Source of the data: [CWhythawk](http://ckan.whythawk.com/km/)
- The data's landing page: [CSV Olympic Athletes](http://ckan.whythawk.com/km/dataset/odata-test/resource/79b3b3f2-a3a2-48c0-8526-e01405bd2f73)
- Direct link to the data: [http://ckan.whythawk.com/km/dataset/4e353550-9380-4be1-adc2-c02a5c1116fb/resource/79b3b3f2-a3a2-48c0-8526-e01405bd2f73/download/olympicathletes0.csv](http://ckan.whythawk.com/km/dataset/4e353550-9380-4be1-adc2-c02a5c1116fb/resource/79b3b3f2-a3a2-48c0-8526-e01405bd2f73/download/olympicathletes0.csv)
- The data format: CSV
- Number of rows: 8619
## Description of data fields
#### Athlete
*String* variable containing first and last name of athlete
#### Age
*String* variable indicating age of athlete at time of medal victory. Can be easily converted into *integer*.
#### Country
Country which the athlete was representing when medal was won. *String* variable.
#### Year
*String* variable (easily convertable to *integer*) of the year of the olympic games in which the medal was won.
#### Closing Ceremony Date
*String* variable in format MM/DD/YYYY.
#### Sport
*String* variable indicating the year of the Olympic Games in which the medal was won
#### Gold Medals
*String* (easily convertable to int) variable indicating the number of gold medals won by the athlete in this specific Olympic games. 0 indicates the athlete won no gold medals.
#### Silver Medals
*String* (easily convertable to int) variable indicating the number of silver medals won by the athlete in this specific Olympic games. 0 indicates the athlete won no silver medals.
#### Bronze Medals
*String* (easily convertable to int) variable indicating the number of bronze medals won by the athlete in this specific Olympic games. 0 indicates the athlete won no bronze medals.
#### Total Medals
*String* (easily convertable to int) variable indicating the total number of medals won by the athlete in this specific Olympic games. This field is never equal to 0.

### Previous Classification Attempts
My digging did not turn up other attempts to run this data through a gender classifer based on name. HOwever, gender classification has been a contentious issue at past major sporting events and the Olympics after female athletes have been accused of "masculine physique" and "high levels of testosterone." See past controversies [NYT: You Say You're a Woman? That Should Be Enough](http://www.nytimes.com/2012/06/18/sports/olympics/olympic-sex-verification-you-say-youre-a-woman-that-should-be-enough.html?_r=0)
