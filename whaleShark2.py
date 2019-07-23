import tweepy as tw
from tweepy import OAuthHandler
import pandas as pd
import pymongo
import json
import datetime
# import collections

import twitterCred

auth = OAuthHandler(twitterCred.CONSUMER_KEY, twitterCred.CONSUMER_SECRET)
auth.set_access_token(twitterCred.ACCESS_TOKEN, twitterCred.ACCESS_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "whale shark"
date_since = "2018-11-16"

tweets = tw.Cursor(api.search, q=search_words, lang="en", since=date_since).items(1000)

tweetCreatedAt = []
tweetUrl = []
tweetImgUrl = []

# def hashtagList(hashtags):
# 	hashtagsNew = []
# 	for new in hashtags:
# 		tempDic = {}
# 		tempDic['tag'] = new
# 	return hashtagsNew

#when multiple pics
# def multiPic(tweet):
# 	#get url for each pic
# 	for eachImg in tweet.extended_entities:
# 		return tweet.extended_entities["media"][eachImg]["url"]



def checkMedia(tweets):
	# for tweet in tweets:
		if "media" in tweets.entities:
			return tweets.entities["media"][0]["media_url"]
		else:
			return False


def checkExtendedEntities(tweets):
	if(hasattr(tweets, 'extended_entities')):
		for img in range(0, len(tweet.extended_entities["media"])):
			print(tweet.extended_entities["media"][img]["media_url"])
		return True
	else:
 		return False



for tweet in tweets:

	tweetList = []
	tweetDic = {}

	if checkMedia(tweet) != False:
		createdAt = str(tweet.created_at)
		url = checkMedia(tweet)
		checkExtendedEntities(tweet)

		user_name = tweet.user.name
		location = tweet.user.location
		user_id = tweet.user.id_str
		hashtags = tweet.entities["hashtags"]


		# tweetCreatedAt.append(str(createdAt))
		tweetDic["created_at"] = createdAt
		tweetDic["location"] = location
		tweetDic[""]
		tweetDic["img_url"] = str(url)
		tweetDic["user_name"] = user_name
		tweetDic["hashtags"] = hashtags

		#put this into an array of dictionaries
		tweetList.append(tweetDic)

		print (url)


		#add collection into mongodb
		
		myclient = pymongo.MongoClient("mongodb://localhost:27017/")
		mydb = myclient["species"]
		mycol = mydb["whale shark"]
		x = mycol.insert_many(tweetList)
		
	





