import tweepy
import requests
import simplejson as json
import webbrowser
from textwrap import TextWrapper

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key=""
consumer_secret=""

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

tinykey=""

class StreamListener(tweepy.StreamListener):
    # status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        try:
            tweetText = status.text
            truncatedText = tweetText.rsplit('#pugmusic')[0]
            tinysongurl = 'http://tinysong.com/b/'+truncatedText+'?format=json&key='+tinykey
            print tinysongurl
            tinyresponse = requests.get(tinysongurl).text
            jsonResponse = json.loads(tinyresponse)
            songurl = jsonResponse["Url"]
            print songurl
            webbrowser.open_new_tab(songurl)


        except Exception, e:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass

streamer = tweepy.Stream(auth=auth, listener=StreamListener(), timeout=3000000000 )
setTerms = ['#pugmusic']
streamer.filter(None,setTerms)