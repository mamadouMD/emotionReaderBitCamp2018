# -*- coding: utf-8 -*-
import tweepy
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys

# Authentification need from twitter develloper account

# Consumer Key (API Key)	f81rnWk1xGOy61lqDAQ6VQ7Ms
# Consumer Secret (API Secret)	aLtuyVIPugaluuPAohqngAezTOP7z7BDR4ljIR9oWcAllOD9Nl
# Access Level	Read and write (modify app permissions)
# Owner	mouctarjalloh
# Owner ID	179606045
# Access Token	179606045-AzWfFpunUf73A354XenHJbzbi4HBI6IVwWI2AVxc
# Access Token Secret	mw3czr0T295Z8CAR9GMZQipZxQfjB7uUvC6FGmpgkcNvb

consumer_key="f81rnWk1xGOy61lqDAQ6VQ7Ms"
consumer_secret="aLtuyVIPugaluuPAohqngAezTOP7z7BDR4ljIR9oWcAllOD9Nl"
access_token="179606045-AzWfFpunUf73A354XenHJbzbi4HBI6IVwWI2AVxc"
access_token_secret="mw3czr0T295Z8CAR9GMZQipZxQfjB7uUvC6FGmpgkcNvb"
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)


# Names of accounts to be queried will be passed in as command-line arguments. 
# I’m going to exit the script if no args are passed, since there would be no reason to continue.

account_list = []
if (len(sys.argv) > 1):
  account_list = sys.argv[1:]
else:
  print("Please provide a list of usernames at the command line.")
  sys.exit(0)

# through the account names passed and use tweepy’s API.get_user() to obtain a few details about the queried account.

if len(account_list) > 0:
  for target in account_list:
    print("Getting data for " + target)
    item = auth_api.get_user(target)
    print("name: " + item.name)
    print("screen_name: " + item.screen_name)
    print("description: " + item.description)
    print("statuses_count: " + str(item.statuses_count))
    print("friends_count: " + str(item.friends_count))
    print("followers_count: " + str(item.followers_count))


tweets = item.statuses_count
account_created_date = item.created_at
delta = datetime.utcnow() - account_created_date
account_age_days = delta.days
print("Account age (in days): " + str(account_age_days))
if account_age_days > 0:
  print("Average tweets per day: " + "%.2f"%(float(tweets)/float(account_age_days)))


hashtags = []
mentions = []
tweet_count = 0
end_date = datetime.utcnow() - timedelta(days=30)
for status in Cursor(auth_api.user_timeline, id=target).items():
  tweet_count += 1
  if hasattr(status, "entities"):
    entities = status.entities
    if "hashtags" in entities:
      for ent in entities["hashtags"]:
        if ent is not None:
          if "text" in ent:
            hashtag = ent["text"]
            if hashtag is not None:
              hashtags.append(hashtag)
    if "user_mentions" in entities:
      for ent in entities["user_mentions"]:
        if ent is not None:
          if "screen_name" in ent:
            name = ent["screen_name"]
            if name is not None:
              mentions.append(name)
  if status.created_at < end_date:
    break
# Finally, we’ll use Counter.most_common() to print out the ten most used hashtags and mentions.

print
print("Most mentioned Twitter users:")
for item, count in Counter(mentions).most_common(10):
  print(item + "\t" + str(count))

print
print("Most used hashtags:")
for item, count in Counter(hashtags).most_common(10):
  print(item + "\t" + str(count))

print
print "All done. Processed " + str(tweet_count) + " tweets."
print