import tweepy
import time
import datetime

# Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_key = "your_access_key"
access_secret = "your_access_secret"

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Create API object
api = tweepy.API(auth)

# Tweet function
def tweet(message):
    api.update_status(message)

# Search for replies with specific word
def search_replies(tweet_id, keyword):
    replies = tweepy.Cursor(api.search, q='to:{}'.format(tweet_id), tweet_mode='extended').items()
    for reply in replies:
        if keyword in reply.full_text.lower():
            print("Reply found: {}".format(reply.full_text))

# Main function
if __name__ == "__main__":
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == "00:00:00":
            tweet = api.update_status("This is a test tweet!")
            search_replies(tweet.id, "test123") 
            time.sleep(86400) # 24 hours in seconds
