# Data Structures and Examples

Here you can find possible data sources for our project. More data source may be added in time.

### Twitter

#### Tweet - User 

1. id bigint(20) UNSIGNED No None
2. userId bigint(20 UNSIGNED No None
3. createdAt timestamp No 0000-00-00 00:00:00
4. text text utf8_unicode_ci No None
5. longitude float Yes NULL
6. latitude float Yes NULL
7. placeId varchar(25) utf8_general_ci Yes NULL
8. inReplyTo bigint(20) UNSIGNED Yes NULL
9. source int(10) UNSIGNED No None
10. truncated bit(1) No None
11. placeLatitude float Yes NULL
12. placeLongitude float Yes NULL
13. sourceName varchar(255) utf8_general_ci Yes NULL
14. sourceUrl varchar(255) utf8_general_ci Yes NULL
15. userName varchar(200) utf8_general_ci Yes NULL
16. screenName varchar(200) utf8_general_ci Yes NULL
17. followersCount int(10) UNSIGNED Yes NULL
18. friendsCount int(10) UNSIGNED Yes NULL
19. statusesCount int(10) UNSIGNED Yes NULL
20. userLocation varchar(200) utf8_general_ci Yes NULL

[23:10, 10/31/2017] Furkan Özkalay: 776821779457335297	104941024	2016-09-16 16:35:19	#Sortir : Enquête à Dole, Bergers du Jura, Beignets à Fougerolles, et Lucie et les Chevaux à Nans-sous-Saint-Anne https://t.co/LTErsomKBT	\N	\N	3ea75b7392b74cae	\N	18777	 	47.1425	6.19758	Twitter Web Client	http://twitter.com	France3Franche-Comté	F3FrancheComte	9845	381	17440	Besançon

### Instagram

#### Users 

1. uid
2. username
3. profilePicture
4. fullName
5. gender
6. isPublic
7. totalFollowers
8. totalMedia
9. totalFollows

#### Medias 

1. uid
2. ownerUserUid
3. mediaCreatedTime
4. latitude
5. longitude
6. imagePath
7. country
8. level1
9. level2
10. likeCount
11. commentCount
12. tags
13. locationId