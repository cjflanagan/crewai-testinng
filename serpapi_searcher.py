import os
from typing import List, Dict
import pandas as pd
import serpapi

SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

class SerpAPISearchTool:
    def search(self, query: str, start: int = 0, num_results: int = 10) -> List[Dict]:
        params = {
            "q": query,
            "api_key": SERPAPI_API_KEY,
            "start": start,
            "num": num_results,
        }
        results = serpapi.search(params)
        data = []
        for item in results.get('organic_results', []):
            title = item.get('title')
            link = item.get('link')
            if title and link:
                data.append({"title": title, "link": link})
        return data

def gather_results(topic: str, batch_size: int = 10, target: int = 50) -> pd.DataFrame:
    searcher = SerpAPISearchTool()
    collected: List[Dict] = []
    start = 0
    while len(collected) < target:
        print(f"Fetching results starting at {start} ... collected {len(collected)} so far")
        results = searcher.search(topic, start=start, num_results=batch_size)
        if not results:
            break
        for r in results:
            if r not in collected:
                collected.append(r)
        start += batch_size
    return pd.DataFrame(collected)

if __name__ == "__main__":
    topic = "AI research"
    df = gather_results(topic)
    print(df.head())
