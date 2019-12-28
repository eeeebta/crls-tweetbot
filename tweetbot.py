import tweepy
from random import randint

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
#for tweet in public_tweets:
#    print(tweet.text)


def get_rand_tweet():
    with open("markov/generated_quotes.txt", "r") as f:
        quotes = f.readlines()
    rgen_tweet_ind = randint(0, len(quotes))
    gen_rand_tweet = quotes[rgen_tweet_ind]
    with open("markov/generated_quotes.txt", "w") as f:
        for line in quotes:
            if line != quotes[rgen_tweet_ind]:
                f.write(line)
    return gen_rand_tweet


rand_tweet = get_rand_tweet()

print(rand_tweet)

api.update_status(rand_tweet)

