import tweepy
from tweepy import OAuthHandler
import datetime

auth = OAuthHandler('CXMg9Pt0OHWeTIPpD46NCqNaK', 'nT0K3Z9oNQjX7Zu64WBiFCjCPs9vTSDPwy8PSBUOOLqzRKTA9r')
auth.set_access_token('807388883944017920-7WYXJ0RRp6sqzdeSNktJ3OLmSK8AnLc', 'rqupZ2ScfrIYJ5SlJuRxOC8IIvHVx6bdqGeuCnlXJ4S10')

keyworddict = {
'happy' : ['happiest', 'so happy', 'excited', 'joyful', 'smile'],
'sad' : ['i\'m so sad', 'i\'m heartbroken', 'i am depressed', 'i am hurting']
}


class Streamer(tweepy.StreamListener):

    def on_status(self, status):
        data = []
        counter = 0
        print(status.text)
        data.append(status.text)
        counter += 1

    def on_error(self, status_code):
        print (status_code)

def collectdata(keywords, counter):
    streamer = Streamer()
    stream = tweepy.Stream(auth = auth, listener=Streamer())
    datacollected = {}

    for keywordset in keyworddict:

        stream.filter(track=keywordset)
        datacollected.append({keywordset.keys() : counter})
