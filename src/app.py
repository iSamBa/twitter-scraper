from twitterscraper import query_tweets
import pandas as pd

import datetime as dt
if __name__ == '__main__':
    # print the retrieved tweets to the screen:
    tweets = query_tweets("Trump", 10, enddate=dt.date.today(), lang="english")
    df = pd.DataFrame(t.__dict__ for t in tweets)
    print(df)
