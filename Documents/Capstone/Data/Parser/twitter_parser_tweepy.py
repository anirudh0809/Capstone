
# import modules
import pandas as pd
import tweepy
  
  

def get_tweets(tweetnumber,tweet):
    print()
    print('/n')
    print(f"Tweet {tweetnumber}")
    print(f"Username:{tweet[0]}")
    print(f"Following Count:{tweet[1]}")
    print(f"Follower Count:{tweet[2]}")
    print(f"Total Tweets:{tweet[3]}")
    print(f"Retweet Count:{tweet[4]}")
    print(f"Tweet Text:{tweet[5]}")
    print(f"Hashtags Used:{tweet[6]}")

def scrape(words, date_since, numtweet):
      
    db = pd.DataFrame(columns=['username', 'following',
                               'followers', 'totaltweets', 'retweetcount', 'text', 'hashtags'])
      
    tweets = tweepy.Cursor(api.search_tweets, q=words, lang="en",
                           since=date_since, tweet_mode='extended').items(numtweet)
     
    list_tweets = [tweet for tweet in tweets]
      
    # Counter to maintain Tweet Count
    i = 1  
      
    # we will iterate over each tweet in the list for extracting information about each tweet
    for tweet in list_tweets:
        username = tweet.user.screen_name
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])
          
        # Here we are appending all the extracted information in the DataFrame
        ith_tweet = [username, following,
                     followers, totaltweets, retweetcount, text, hashtext]
        db.loc[len(db)] = ith_tweet
          
        # Function call to print tweet data on screen
        get_tweets(i, ith_tweet)
        i = i+1
    filename = 'scraped_tweets.csv'
      
    # we will save our database as a CSV file.
    db.to_csv(filename)
  
  
if __name__ == '__main__':
      
    # Enter your own credentials obtained 
    # from your developer account
    consumer_key = ""
    consumer_secret = ""
    access_key = ""
    access_secret = ""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    print("Welcome to tweet parser!!!")
    print("__________________________")
    print("__________________________")
    print("__________________________")
    print("__________________________")
    print("__________________________")

    # Enter Hashtag and initial date
    print("Enter Twitter HashTag to search for")
    words = input()
    print("Enter Date since The Tweets are required in yyyy-mm--dd")
    date_since = input()
    print('Specify the number of tweets you need to scrape')
    numtweet = int(input() )
    scrape(words, date_since, numtweet)
    print('Scraping has completed!')
    print('End')

