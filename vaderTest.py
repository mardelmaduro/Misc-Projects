#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:05:58 2016

@author: mardelmaduro
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from vaderSentiment import sentiment as vaderSentiment
#import sentiment_mod as s
#from twitterapistuff import *

#consumer key, consumer secret, access token, access secret.
ckey="YiU7huUmalApX6MhuSyAHqXR3"
csecret="vyyjfRsl7wAkrkHWhTYESBbPttlMPiWJSlYTmbkab4ji0vwsXn"
atoken="790250032339398656-E68WqlDK36aa27GSDHRPxKNBvfXWofL"
asecret="sgacxsEXQTeACzTGWIkxtGzTkl8OiCZHsS2IzQ5gIzfN9"





class listener(StreamListener):

    def on_data(self, data):

		all_data = json.loads(data)

		tweet = all_data["text"]
		sentiment_value, confidence = vaderSentiment(tweet)
		print(tweet, sentiment_value, confidence)

		if confidence*100 >= 80:
			output = open("twitter-out.txt","a")
			output.write(sentiment_value)
			output.write('\n')
			output.close()

		return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])