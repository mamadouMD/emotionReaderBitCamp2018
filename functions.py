import Tweet
# import datetime

# This file holds the various functions after the data has been

# Paramters: Hash table of data (Key = date, Value = tweet(Object))
# Return: New Hashmap (Key = mention Name, Value = Average sentiment rating)
def analyzeMentions(data):
	dataMentions = {}
	for twt in data.keys():
		for mention in data[twt].mentions:
			if dataMentions.has_key(mention):
				dataMentions[mention] = (int) ((dataMentions[mention] + data[twt].sentiment) / 2)
			else:
				dataMentions[mention] = data[twt].sentiment
	return dataMentions


# Paramters: Hash table of data (Key = date, Value = tweet(Object))
# Return: New Hashmap (Key = hashtag, Value = Average sentiment rating)
def analyzeHashtags(data):
	dataHashTags = {}
	for twt in data.keys():
		for hashtag in data[twt].hashtags:
			if dataHashTags.has_key(hashtag):
				dataHashTags[hashtag] = (int) ((dataHashTags[hashtag] + data[twt].sentiment) / 2)
			else:
				dataHashTags[hashtag] = data[twt].sentiment
	return dataHashTags


# Prints out the mentions and hashtags with their average sentiment ratings
def printMentionHashtagSentiment(data):
	dataMentions = analyzeMentions(data)
	dataHashTags = analyzeHashtags(data)

	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "Emotion/Sentiment Readings"
	print "100% = Extrememly Positive"
	print "50% = Neutral"
	print "0% = Extrememly Negative"

	print "~~~~~~~~~~Mentions~~~~~~~~~~"
	if dataMentions is not None:
		for mention in dataMentions.keys():
			print "Mention: {} | Sentiment: {}%".format(mention,dataMentions[mention])

	print "~~~~~~~~~~HashTags~~~~~~~~~~"
	if dataHashTags is not None:
		for hashtag in dataHashTags.keys():
			print "Hashtag: {} | Sentiment: {}%".format(hashtag, dataHashTags[hashtag])


# def printDateSentiment(data):
# 	sortedDate = data.keys().sort()

# 	print "--------------------"
# 	for date in sortedDate:
# 		print "Date: {} | Sentiment: {}%".format(hashtag, data[date].sentiment)
