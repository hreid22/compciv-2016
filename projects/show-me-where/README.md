# About the dataset
Data that contains exact geolocations for cases in the most recent Ebola outbreak is either very hard to find or nonexistent. However, this data set provides geolocations including latitude and longitude for Ebola cases in historical Ebola outbreaks in sub-Saharan Africa. The data comes from a paper published in the Nature affiliate journal Scientific Data in October of 2014. I am interested in visualizing the location of these cases to make a more visual representation of what the communities look like that often bear the burden of Ebola outbreaks: rural and poor.
## Basic facts about the dataset
- Source of the data: [A comprehensive database of the geographic spread of past human Ebola outbreaks](http://www.nature.com/articles/sdata201442#data-citations)
- The data's landing page: [Figshare File](https://figshare.com/articles/Ebola_past_outbreak_geographic_spread_data/1192660)
- Direct link to the data: [https://ndownloader.figshare.com/files/3230399](https://ndownloader.figshare.com/files/3230399)
- The data format: CSV
- Number of rows: 118

## Description of data fields
#### UNIQ_ID
Contains an *integer* that is an identification number starting at 101 and ranging up to 217.
#### NAME
Contains a *text string* that is the name of the site where the case was documented. Varies in specificity from the town name to the exact hospital.
#### Country
Contains a *text string* of the country where the case occurred.
#### Virus
Contains a *text string* which describes the sub-type of the Ebola virus in the case.
#### CASE_TYPE
Contains a *text string* that indicates whether the case was an index, secondary or imported case
#### DATA_TYPE
Contains a *text string* which indicates whether this location is a point location or whether there is some degree of uncertainty in which case it is a "polygon" with a radius demarcated under *LOC_NTS*.
#### LAT
Contains a *float* of the latitude coordinate of where the case occurred.
#### LONG
Contains a *float* of the longitude coordinate of where the case occurred.
#### LOC_NTS
Contains a *text string* that gives notes on the way the location of an incident case was derived and the uncertainty in the location, if applicable.
#### SPR_ORDER
Contains mostly *integers* or a *text string* (NA if not applicable to a certain data point). The purpose of this column is unclear to me.
#### SOURCE_1
Contains mostly *integers* or a *text string* if the category is not applicable (NA) to the case being described, then NA is displayed. The integers are number codes of sources from which the case information was derived.
#### SOURCE_2
Contains mostly *integers* or a *text string* if the category is not applicable (NA) to the case being described, then NA is displayed. The integers are number codes of sources from which the case information was derived.
#### SOURCE_3
Contains mostly *integers* or a *text string* if the category is not applicable (NA) to the case being described, then NA is displayed. The integers are number codes of sources from which the case information was derived.
#### STR_DAY
Contains an *integer* describing the starting day of the case from 1-31.
#### STR_MONTH
Contains an *integer* describing the starting month of the case from 1-12.
#### STR_YEAR
Contains an *integer* describing the starting year of the case from 1976-2012.
#### END_DAY
Contains an *integer* or *text string* in the case of NA that seems to describe the ending day of the case. However so few of these values were actually available that this column is not useful.
#### END_MNTH
Contains an *integer* or *text string* in the case of NA that seems to describe the ending month of the case. However so few of these values were actually available that this column is not useful.
#### END_YEAR
Contains an *integer* or *text string* in the case of NA that seems to describe the ending year of the case. However so few of these values were actually available that this column is not useful.
#### REP_CASE
Contains an *integer* or *text string* if NA. Most *integer* values are missing. Content of the column is unclear.
#### REP_DEATH
Contains an *integer* or *text string* if NA. Most *integer* values are missing. Content of the column is unclear.
#### OB_ID
Contains an *integer* denoting the identity of the outbreak to which the case in that line belongs.
#### OB_STR_DAY	
Contains an *integer* denoting the start day of the outbreak to which the case in that line belongs.
#### OB_STR_MNTH
Contains an *integer* denoting the start month of the outbreak to which the case in that line belongs.
#### OB_STR_YEAR
Contains an *integer* denoting the start year of the outbreak to which the case in that line belongs.
#### OB_END_DAY
Contains an *integer* denoting the end day of the outbreak to which the case in that line belongs.
#### OB_END_MNTH
Contains an *integer* denoting the end month of the outbreak to which the case in that line belongs.
#### OB_END_YEAR
Contains an *integer* denoting the end year of the outbreak to which the case in that line belongs.
#### OB_CASE	
Contains an *integer* describing the number of total reported cases in the outbreak to which the case in that line belongs
#### OB_DEATH
Contains an *integer* describing the number of total reported deaths in the outbreak to which the case in that line belongs
## Anticipated data wrangling
Since there are not a huge number of entries in this data set I will include all cases (my requirement being that they all have at least latitude and longitude coordinates and a start year which all do). I am not sure yet how I will incorporate the data in the location notes section that indicates uncertainty in the location. My plan right now is to filter cases denoted polygon and then search for the radius of uncertainty in the case location from the data in the LOC_NTS column. I will then indicate this radius on the map API I display.