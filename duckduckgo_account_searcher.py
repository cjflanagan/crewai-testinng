import os
import pandas as pd
from typing import List, Dict
from duckduckgo_search import DDGS
import tweepy

TWITTER_CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')

class TwitterProfileTool:
    def __init__(self):
        auth = tweepy.OAuth1UserHandler(
            TWITTER_CONSUMER_KEY,
            TWITTER_CONSUMER_SECRET,
            TWITTER_ACCESS_TOKEN,
            TWITTER_ACCESS_SECRET,
        )
        self.api = tweepy.API(auth)

    def get_profile(self, username: str) -> Dict | None:
        try:
            user = self.api.get_user(screen_name=username)
            return {
                'username': user.screen_name,
                'name': user.name,
                'description': user.description,
                'followers': user.followers_count,
                'profile_url': f'https://twitter.com/{user.screen_name}',
            }
        except tweepy.TweepyException:
            return None

class DuckDuckGoSearchTool:
    def search_accounts(self, query: str, count: int = 20) -> List[str]:
        with DDGS() as ddgs:
            results = ddgs.text(f"site:twitter.com {query}", max_results=count)
            handles = []
            for r in results:
                url = r.get('href') or r.get('url')
                if not url or 'twitter.com/' not in url:
                    continue
                username = url.split('twitter.com/')[-1].split('/')[0]
                username = username.lstrip('@').split('?')[0]
                if username and username not in handles:
                    handles.append(username)
        return handles

def gather_accounts(topic: str, batch_size: int = 20, target: int = 1000) -> pd.DataFrame:
    searcher = DuckDuckGoSearchTool()
    verifier = TwitterProfileTool()
    unique: Dict[str, Dict] = {}
    page = 1
    while len(unique) < target:
        print(f"Searching batch {page}... collected {len(unique)} so far")
        handles = searcher.search_accounts(topic, count=batch_size)
        for handle in handles:
            if handle in unique:
                continue
            profile = verifier.get_profile(handle)
            if profile and profile['followers'] > 0:
                unique[handle] = profile
        print(f"Total unique verified accounts: {len(unique)}")
        page += 1
    return pd.DataFrame(list(unique.values()))

if __name__ == "__main__":
    topic = "AI research"
    df = gather_accounts(topic)
    print(df.head())
