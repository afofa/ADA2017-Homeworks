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

## Milestones 

| Week          | Targets     |
| ------------- |-------------|
| Week 1 **01.11 - 07.11**      | Search and decide datasets to use for enriching <br/> Load and preprocess data. <br/> Exploratory data analysis, data cleaning and wrangling |
| Week 2 **07.11 - 14.11**      | Start answering research questions. <br/> Merge datasets for enriching when necessary.      |
| Week 3 **14.11 - 21.11** | Main part of scripts and notebook is done. <br/> Search for and decide how to visualize data effectively.    |
| Week 4 **21.11 - 28.11** | Get temporary results and analyze. <br/> Collect codes, results and analyses up to now, display them for milestone 2.    |

# Milestone 1

After reviews from TAs and initial exploration of data, some of the elements in our project has changed. Our project topic was found interesting but it had very large scope. Thus, we wanted to limit number of external datasets to be used and decrease number of research questions we ask. As a result, we decided to not use any of the external datasets which we named in proposal except we can possibly use dataset containing location based demographic statistics about Switzerland, for example population and languages spoken in different parts of Switzerland in order to able to compare tweeting trends better across locations.

We explored Swiss dataset and learned that contrary to its [description](https://docs.google.com/spreadsheets/d/1cB3UBUDF0rXvIpPQz8ly1T_7ERutw8ObGheFI6e3Y4E/), Swiss dataset does not contain sentiment of tweets which are necessary for our task. Instead, another dataset containing tweets geolocated in Switzerland is provided after some discussion on mattermost. Although not for each tweet, this dataset contains location in which tweet has sent, language of tweet, sentiment of tweet; which means everything we want to have. Thus, we decided to use this dataset.

Up to know, we explored the data (note that, this data is provided just 1 week ago) and tried to understand its structure and how it can be used for our purposes. We extracted useful features from subsample of the data using pandas with some processing of json files. However, as the dataset is huge it does not seem likely that our classical tools that we used in assignments would suffice. Thus, using AWS we created a working environment for ourselves and uploaded significant proportion of whole dataset to see that indeed we can deal with such high volume of data. We provided our pipeline and examples from our working environment to show the work we did up to know. We are confident that we can the data in its size with our working environment. In fact, we used it to understand what is in the data. We examined features which are important for us; their formats, how they are distributed, whether there are significant number of missing values. We filtered and transformed data up to know, and for answering research questions we will further filter and transform the data.

From now on, as we extracted useful fatures for answering our questions, we will work on our research questions one by one to filter and transform the data further for our needs. Each time, we will use visualization to understand the result better. If it is possible to enrich the data in a way which is helpful for answering our question, we will find and use suitable external data (for example, location based demographic statistics of Switzerland to compare tweeting patterns across different locations). 
