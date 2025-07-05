# crewai-testinng

This repository demonstrates how to use [CrewAI](https://github.com/crewAIInc/crewAI) to build agents that gather web search results using [SerpAPI](https://serpapi.com/).

The `serpapi_searcher.py` script queries SerpAPI and stores unique result links in a table.

Before running the script, set your SerpAPI key:

- `SERPAPI_API_KEY`

Run the script to collect results:

```bash
python serpapi_searcher.py
```

## Hierarchical search notebook

A Jupyter notebook `hierarchical_twitter_search.ipynb` shows how to build a hierarchical crew that keeps searching Twitter via SerpAPI until it finds 1000 unique accounts about a topic.

Set both `SERPAPI_API_KEY` and `OPENAI_API_KEY` environment variables before running the notebook.
