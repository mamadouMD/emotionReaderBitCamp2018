import re
import indicoio
import string

# MAKE GLOBAL Variables
API_KEY = "86835201fbce14ccf4eb3986da330f5a"
indicoio.config.api_key = API_KEY

class Tweet:
	text = ""
	sentiment = 0
	hashtags = []
	mentions = []

	# Constructor
	def __init__(self, text, mentions, hashtags):
		self.text = text
		self.mentions = mentions
		self.hashtags = hashtags
		self.sentiment = 0
		self.sentiment = self.processData()

	# Processes the string given by the constructor and inserts all data into connections
	# Returns the output of Indico's API sentiment reading
	def processData(self):
		textNoSym = str.replace(str.replace(self.text,'#',''),'@','')
		return (int) (indicoio.sentiment_hq(textNoSym) * 100)

