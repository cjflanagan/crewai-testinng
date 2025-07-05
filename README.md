# crewai-testinng

This repository demonstrates how to use [CrewAI](https://github.com/crewAIInc/crewAI) to build a hierarchical agent system that searches for Twitter accounts related to a topic. Originally the example was provided as a Jupyter notebook, but a Python script is now included.

The new `duckduckgo_account_searcher.py` script searches **DuckDuckGo** for Twitter profiles matching a topic. It then verifies each profile via the Twitter API to ensure the account is real and active.

Before running the script, set the following environment variables with your API credentials:

- `TWITTER_CONSUMER_KEY`
- `TWITTER_CONSUMER_SECRET`
- `TWITTER_ACCESS_TOKEN`
- `TWITTER_ACCESS_SECRET`
- `OPENAI_API_KEY`
- `SERPER_API_KEY`

Run the script to collect 1000 unique verified Twitter accounts:

```bash
python duckduckgo_account_searcher.py
```
