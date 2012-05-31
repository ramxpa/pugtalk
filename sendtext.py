import tweepy
from twilio.rest import TwilioRestClient


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

#Twilio creds
account = "abc"
token = "xx"
client = TwilioRestClient(account, token)


class StreamListener(tweepy.StreamListener):
    # status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        try:
            """
            Sends a message and makes a call if a @reply is received.
            The 'To' number needs to be verfied with Twilio and the
            'from' number can be changed only in paid accounts.
            Fyi, Messages and calls are charged at a fixed rate
            by Twilio.

            The call resource needs a url which outputs valid TwiML.
            Refer to Twilio documentation for more info on TwiML.
            Currently it just makes a call.
            """
            message = client.sms.messages.create(to="XXX-XXX-XXXX", from_="+14155992671",
                                     body=status.text)

            call = client.calls.create(to="XXX-XXX-XXXX", from_="+14155992671",
                                url="http://foo.com/call.xml")

        except Exception, e:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass

streamer = tweepy.Stream(auth=auth, listener=StreamListener(), timeout=3000000000 )
setTerms = ['@ramanujam']
streamer.filter(None,setTerms)