import urllib
import json

#TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=2'
TWITTER_URL = "https://api.twitter.com/1.1/statuses/user_timeline.json"

while True:
    print ''
    acct = raw_input('Enter Twitter Account:')
    if ( len(acct) < 1 ) : break
    url = TWITTER_URL.replace('user_timeline', acct)
    
    print 'Retrieving', url
    document = urllib.urlopen (url).read()
    
    print 'Retrieved', len(document), 'characters.' 
    
    js = json.loads(document)
    count = 0
    for user in js:
        count = count + 1
        if count > 4 : break
        print user[count]

        status =  user.get('status', None)
        if status is not None : 
            txt = status['text']
            print ' ',txt[:50]
