# crewai-testinng

This repository demonstrates how to use [CrewAI](https://github.com/crewAIInc/crewAI) to build a simple agent that gathers web search results for a topic. Searches are performed using [SerpAPI](https://serpapi.com/).

The `serpapi_searcher.py` script queries SerpAPI and stores unique result links in a table.

Before running the script, set your SerpAPI key:

- `SERPAPI_API_KEY`

Run the script to collect results:

```bash
python serpapi_searcher.py
```
