import re
import indicoio
import string

# This file holds the object Tweet
# This is where all data about each specific tweet is stored
# This is also where the Indico API is used

# If you want to download Indico API: https://indico.io/docs#install
# For using Indico 								HIDE BEFORE PUSHING
API_KEY = "Insert Yours Here"	
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
		textNoSym = str.replace(str.replace((str)(self.text),'#',''),'@','')
		textNoSym = re.sub('https:://[^\^\'$&:<>\[\{\}\]"+#%@\/;=?^|,`]+ ','',textNoSym) # This regexp checks gets a URL
		return (int) (indicoio.sentiment_hq(textNoSym) * 100)

