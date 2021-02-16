from twitterscraper import query_tweets

if __name__ == '__main__':
    list_of_tweets = query_tweets("Freelance", 40)

    for tweet in list_of_tweets:
        print(tweet)