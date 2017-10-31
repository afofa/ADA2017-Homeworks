# Swiss Twitter Journey

## Abstract

Social media has penetrated to our daily lives and occupy undeniably significant amount of time for majority of people. One service which strikes among social media is Twitter, where people can share their opinion about any matter with relatively short posts called tweets. Together with their twitter usage habits, these tweets reflect a great deal about people and the society they live in. By finding and analyzing the patterns in their Twitter usage, one can gain insights about people which are hard or even impossible to get in any other way. In the light of this discussion, our aim is to investigate Swiss Twitter usage patterns and its daily change depending on location, occurrence of important local or international events as well as analyzing diversification of usage in different parts of Switzerland.

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
	* Depending on location, how ratios of languages of tweets change?
	* How do these change in different regions of Switzerland depending on official language (German, French, Italian, Romansh) of the region? (*Use dataset about demographics of Switzerland*)
	* Are there a significant number of tweets sent in languages which are not official languages in Switzerland? If there are, which languages are well represented and in which locations these tweets are sent? Can any information be inferred about immigration by examining language of tweets? (*Using dataset about demographics of Switzerland*)
* Are there any peak in usage, very low or very high sentiment score compared to any others?
	* When do these trends occur?
	* Is there an important local or global event before or during these trends? (*Using dataset containing important local or global events*)
	* How is an important local or global event received by Swiss Twitter users? Is there a difference between their response and response of global Twitter users? (*Using Global Twitter dataset*)

## Dataset

We will mainly use Swiss Tweets dataset. It consists of 22,222,184 tweets geolocated in Switzerland and collected between 2010 and 2016. Most importantly text of tweet, date, username, longitude, and latitude (geolocation), and sentiment score are given in the dataset. The following information is also given in the dataset. *DataStructure.md is for additional information about the structure of data.*


### We might enrich our data with following datasets as well.


**Global Twitter dataset:** We can get tweets following an event (tweets sent in the small period given the date) and find sentiment scores using various methods. Compare overall response of all Twitter users to overall response of Swiss twitter users, using the sentiment scores. In Twitter dataset only following information is available: username, language, tweet and date.


**Instagram:** We can collect Instagram data geolocated in Switzerland. Analyze instagram usage of Swiss people, compare the results with results from analyze of Twitter usage. We can compare the results from Instagram and twitter dataset.


**Dataset containing important local or global events:** (local: festival in Lausanne, elections in Switzerland; global: terrorist attack in Paris, US elections etc.) where date is given, analyze how twitter usage is different during or following these events. GDELT or UCDP datasets might be useful. For enriching only following information are necessary: event, location, date.


**Dataset containing demographic information of Switzerland across locations:**. Statistics of languages spoken in different regions of Switzerland. Swiss open data might have useful datasets.

## A list of internal milestones up until project milestone 2

Week 1
01.11.2017 - 07.11.2017
Search and decide datasets to use for enriching.
Load and preprocess data.
Exploratory data analysis, data cleaning and wrangling.

Week 2
07.11.2017 - 14.11.2017
Start answering research questions.
Merge datasets for enriching when necessary.

Week 3
14.11.2017 - 21.11.2017
Main part of scripts and notebook is done.
Search for and decide how to visualize data effectively.

Week 4
21.11.2017 - 28.11.2017
Get temporary results and analyze.
Collect codes, results and analyses up to now, display them for milestone 2.


## Questions for TAs

Q1: It is hard to manage all of your codebase in a jupyter notebook, can we have separate scripts other than the jupyter notebook that will be graded? 

Q2: Can we use external datasets, or even data that we will collect using various APIs or libraries (for example, data from instagram)?

Q3: How long our analyses and results should be? Considering high number of questions we have, is it more than what is asked?
