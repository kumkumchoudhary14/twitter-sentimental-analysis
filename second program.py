import tweepy 
from textblob import TextBlob
import  matplotlib.pyplot as plt
def percentage (part,whole):
    return 100* float(part)/float(whole)

consumerKey = 'lUmOTITqvWzidNLTRCKsfqpbl'
consumerSecret = 'D540vU03qg7ElodEqnkOb1kpBEkD4N8eJHVcW9LWYUjgZIzIwg'
accessToken = '1264810992061624320-AgdUsSx4KDqSYA5t7W80xd4EG0Uj1n'
accessTokenSecret = 'K0b3nUgpa9BpQ6jihUK5k5XGeUmDfQWDQGaSBVQnd3bNc'
auth = tweepy.OAuthHandler(consumerKey , consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)
searchTerm = input("Enter Keyword/Tag to search about: ")
NoOfTerms = int(input("Enter how many tweets to search: "))
tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(NoOfTerms)

polarity = 0
positive = 0
negative = 0
neutral = 0

for tweet in tweets:
      print(tweet.text)
      analysis = TextBlob(tweet.text)
      
      polarity += analysis.sentiment.polarity
      
      if(analysis.sentiment.polarity == 0):
          neutral += 1
      elif(analysis.sentiment.polarity > 0 ):
          positive += 1
      elif(analysis.sentiment.polarity < 0):
          negative += 1
positive = percentage(positive, NoOfTerms)
negative = percentage(negative, NoOfTerms)
neutral = percentage(neutral, NoOfTerms)

positve = format(positive,'2f')
negative = format(negative,'2f')
neutral = format(neutral,'2f')

 
if (polarity == 0):
    print("Neutral")
elif (polarity > 0 ):
    print(" Positive")
elif (polarity < 0):
    print("Negative")


     
labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]','Negative [' + str(negative) + '%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(NoOfTerms) + ' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()



              
     
        

      
