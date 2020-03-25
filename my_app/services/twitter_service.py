# web_app/services/twitter_service.py

import os
from dotenv import load_dotenv
import tweepy
from pprint import pprint

# load environment variables
load_dotenv()
consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

def twitter_api_client():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    #print("AUTH", type(auth))

    api = tweepy.API(auth)
    #print("API", type(api)) #> <class 'tweepy.api.API'>
    return api

if __name__ == "__main__":
    # testing the api
    api = twitter_api_client()

    screen_name = "elonmusk"

    print("--------------")
    print("USER...")
    user = api.get_user(screen_name)
    print(type(user)) #> <class 'tweepy.models.User'>
    print(user.screen_name)
    print(user.followers_count)
    #pprint(user._json)

    print("--------------")
    print("STATUSES...")
    # get that user's tweets:
    # see: http://docs.tweepy.org/en/latest/api.html#API.user_timeline
    statuses = api.user_timeline(screen_name, tweet_mode="extended", count=150, 
                                 exclude_replies=False, include_rts=False)

    for status in statuses:
        print(type(status)) #> <class 'tweepy.models.Status'>
        #pprint(status._json)
        print(status.full_text)