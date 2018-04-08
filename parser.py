# -*- coding: UTF-8 -*-
import Tweet
import re
import csv
import tweepy
from tweepy import OAuthHandler
from tweepy import API

# This file is the parser. It parses the data and returns it inside
# of a dictionary.


# keys and tokens from the Twitter Dev Console 			(Before committing remember to hide)
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


def getTweets(username):
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	auth_api = API(auth)
	api = tweepy.API(auth)

	# Gets the past 20 previous tweets
	new_tweets = api.user_timeline(id=username)

	tweets = []
	tweetsCSV = [tweet.text for tweet in new_tweets]
	for x in tweetsCSV:
		try:
			tweets.append(emojiPattern.remove_emoji(x))
		except:
			continue	# This is a random statement to get rid of an error

	dateCSV = [tweet.created_at for tweet in new_tweets] 

	allData = {} # Key =  Date, Value = tweet (Object from Tweet.py)
	for i in range(0, (len(tweetsCSV))):
		try:
			text = (str)(tweetsCSV[i])
			print "Text: {} | Mentions: {} | Hashtags: {}".format(text, getMentions(text), getHashTags(text))
			allData[dateCSV[i]] = Tweet.Tweet(text, getMentions(text), getHashTags(text))
		except:
			continue		
	return allData


def getMentions(text):
	try:
		return map(str, re.findall('(@[^~`!@#$%^&*\(\)+-=\{\}\|\][:\';\?\/.,\"<>\s]+)',text))
	except:
		return


def getHashTags(text):
	try:
		return map(str, re.findall('(#[^~`!@#$%^&*\(\)+-=\{\}\|\][:\';\?\/.,\"<>\s]+)',text))
	except:
		return