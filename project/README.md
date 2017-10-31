# Swiss Twitter Journey

Our aim is to investigate Swiss Twitter usage patterns and its daily change depending on location, occurrence of local or international events as well as analyzing diversification of usage in different parts of Switzerland.

In order to achieve our aim, we will use Swiss Tweet dataset together with other several different data collections. 

## Research questions

Are there striking patterns for Swiss Twitter users?

* How frequency of tweets change across time? 
	* Is there a pattern depending on time of day? 
	* Is there a seasonal pattern (more frequent twitter usage during winter nights)? 
	* How does usage change during the time period dataset spans?

* Is there different pattern in time in terms of usage depending on location? 
	* Is there a pattern depending on location? 
	* How different are tweets sent in Zurich than tweets sent in Lausanne?

* How languages are represented in tweets?
	* Depending on location, how ratios of languages of tweets change? H
	* How do these change in different regions of Switzerland depending on official language (German, French, Italian, Romansh) of the region? (Use dataset about demographics of Switzerland)
	* Are there a significant number of tweets sent in languages which are not official languages in Switzerland? If there are, which languages are well represented and in which locations these tweets are sent? Can any information be inferred about immigration by examining language of tweets? *Using dataset about demographics of Switzerland*
* Are there any peak in usage, very low or very high sentiment score compared to any others?
	* When do these trends occur?
	* Is there an important local or global event before or during these trends? *Using dataset containing important local or global events*
	* How is an important local or global event received by Swiss Twitter users? Is there a difference between their response and response of global Twitter users? *Using Global Twitter dataset*

## Dataset

We will mainly use Swiss Tweets dataset. It consists of 22,222,184 tweets geolocated in Switzerland and collected between 2010 and 2016. Most importantly text of tweet, date, username, longitude, and latitude (geolocation), and sentiment score are given in the dataset. The following information is also given in the dataset. *DataStructure.md is for additional information about the structure of data.*


### We might enrich our data with following datasets as well.


**Global Twitter dataset:** We can get tweets following an event (tweets sent in the small period given the date) and find sentiment scores using various methods. Compare overall response of all Twitter users to overall response of Swiss twitter users, using the sentiment scores. In Twitter dataset only following information is available: username, language, tweet and date.


**Instagram:** We can collect Instagram data geolocated in Switzerland. Analyze instagram usage of Swiss people, compare the results with results from analyze of Twitter usage. We can compare the results from Instagram and twitter dataset.


**Dataset containing important local or global events:** (local: festival in Lausanne, elections in Switzerland; global: terrorist attack in Paris, US elections etc.) where date is given, analyze how twitter usage is different during or following these events. GDELT or UCDP datasets might be useful. For enriching only following information are necessary: event, location, date.


**Dataset containing demographic information of Switzerland across locations:**. Statistics of languages spoken in different regions of Switzerland. Swiss open data might have useful datasets.
