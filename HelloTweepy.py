#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:25:33 2016

@author: mardelmaduro
"""

import tweepy

from tweepy import Stream
from tweepy.streaming import StreamListener

auth = tweepy.OAuthHandler('YiU7huUmalApX6MhuSyAHqXR3','vyyjfRsl7wAkrkHWhTYESBbPttlMPiWJSlYTmbkab4ji0vwsXn')
auth.set_access_token(	'790250032339398656-E68WqlDK36aa27GSDHRPxKNBvfXWofL','sgacxsEXQTeACzTGWIkxtGzTkl8OiCZHsS2IzQ5gIzfN9')

api = tweepy.API(auth)
user = api.me()

def printInfoOnMe():
    

    print("name: " + user.name)
    print("location: " + user.location)
    print("friends: " + str(user.friends_count))
    return None

def tweetOut(stringToTweet):
    api.update_status(stringToTweet)
    return None
    
def pullAllTweets():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print tweet.text
    return None 
    
def checkFriends():
    
    myFriends = api._lookup_friendships
    
    if user.friends_count == 0:
        print("No friends")
    else:
        print(myFriends)
    
    return None
    
    
class MyListener(StreamListener):
    
    def on_data(self, data):
        try:
            with open('python.json','a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print(";Error on_data:"+str(e))
        return True
        
    def on_error(self, status):
        print(status)
        return True
        
twitter_stream = Stream(auth, MyListener())


twitter_stream.filter(track=["#NationalPumpkinDay"])
    
    
    
    
    
#printInfoOnMe()
#checkFriends()
#tweetOut('This is but a test')
#pullAllTweets()
