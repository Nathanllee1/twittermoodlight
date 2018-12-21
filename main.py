import tweepy
from tweepy import OAuthHandler
'''
api = twitter.Api(consumer_key=['CXMg9Pt0OHWeTIPpD46NCqNaK'],
consumer_secret=['nT0K3Z9oNQjX7Zu64WBiFCjCPs9vTSDPwy8PSBUOOLqzRKTA9r'],
access_token_key=['807388883944017920-7WYXJ0RRp6sqzdeSNktJ3OLmSK8AnLc (Access token)'],
access_token_secret=['rqupZ2ScfrIYJ5SlJuRxOC8IIvHVx6bdqGeuCnlXJ4S10'])
'''
auth = OAuthHandler('CXMg9Pt0OHWeTIPpD46NCqNaK', 'nT0K3Z9oNQjX7Zu64WBiFCjCPs9vTSDPwy8PSBUOOLqzRKTA9r')
auth.set_access_token('807388883944017920-7WYXJ0RRp6sqzdeSNktJ3OLmSK8AnLc', 'rqupZ2ScfrIYJ5SlJuRxOC8IIvHVx6bdqGeuCnlXJ4S10')

happykeywords = ['happiest', 'so happy', 'excited', 'joyful', 'smile']
sadkeywords = ['i\'m so sad', 'i\'m heartbroken', 'i am depressed', 'i am crying']


class Streamer(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print (status_code)

streamer = Streamer()
happystream = tweepy.Stream(auth = auth, listener=Streamer())

happystream.filter(track=happykeywords)
