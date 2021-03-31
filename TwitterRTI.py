#!/usr/bin/python3
import tweepy
import argparse

# usage: TwitterRTI.py [-h] --terms TERMS
#
# optional arguments:
#   -h, --help     show this help message and exit
#   --terms TERMS  Search terms to get tweets of interest

class StreamDataListener(tweepy.StreamListener):
    def on_data(self, raw_data):
        # Display raw_data in the standard output.
        print(raw_data.rstrip())
        return super().on_data(raw_data)

def main(terms):
    # 1. Setup Tweepy to use our Twitter App settings.
    consumer_key = "__KEY__"
    consumer_secret = "__KEY__"
    access_token = "__KEY__"
    access_token_secret = "__KEY__"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    
    # 2. Setup Tweety to ingest tweets in real-time (stream data)
    streamDataListener = StreamDataListener()
    streamData = tweepy.Stream(auth = api.auth, listener=streamDataListener)
    
    # 3. Start streaming data from Twitter
    streamData.filter(track=terms.split(","))

if __name__ == "__main__":
    # 1. Setup arguments parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--terms", help="Search terms to get tweets of interest", required=True)
    args = parser.parse_args()
    # 2. Call the main function with the search terms.
    main(args.terms)
