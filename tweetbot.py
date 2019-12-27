import tweepy

with open("api_keys.txt") as file:
    key_list = file.readlines()

consumer_key = key_list[0].strip("\n")
consumer_secret = key_list[1].strip('\n')
access_token = key_list[2].strip('\n')
access_token_secret = key_list[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

api.update_status("test tweet")
