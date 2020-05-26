import tweepy 
from textblob import TextBlob
key = 'lUmOTITqvWzidNLTRCKsfqpbl'
secret = 'D540vU03qg7ElodEqnkOb1kpBEkD4N8eJHVcW9LWYUjgZIzIwg'
token_key = '1264810992061624320-AgdUsSx4KDqSYA5t7W80xd4EG0Uj1n'
token_secret = 'K0b3nUgpa9BpQ6jihUK5k5XGeUmDfQWDQGaSBVQnd3bNc'
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(token_key,token_secret)
api=tweepy.API(auth)
public_tweets = api.search("AKSHAY KUMAR")
for tweet in public_tweets:
      print(tweet.text)
      analysis = TextBlob(tweet.text)
      print(analysis.sentiment)
