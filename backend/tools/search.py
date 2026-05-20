from tavily import TavilyClient
from config.settings import settings


class SearchManager:

    def __init__(self):

        self.client = TavilyClient(
            api_key=settings.TAVILY_API_KEY
        )

    async def search(
        self,
        query: str,
        max_results: int = 5
    ):

        response = self.client.search(
            query=query,
            max_results=max_results
        )

        cleaned_results = []

        for result in response["results"]:

            cleaned_results.append({

                "title": result.get("title", ""),

                "content": result.get("content", ""),

                "url": result.get("url", "")
            })

        return cleaned_results


search_manager = SearchManager()