from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

tavily_client = TavilyClient(api_key = api_key)

def get_search_results(query: str) -> str:

    """
    Searches the web for the given query and returns a list of result URLs 
    and content snippets.
    """

    try: 
        results = tavily_client.search(
            query=query,
            max_results = 5,
            search_depth = "basic"
        )
    except Exception as e:
        return f"Unable to fetch search results...\n {e}"
    
    if "results" not in results or len(results["results"]) == 0:
        return "No results found..."
    
    search_data = ""

    for item in results ["results"]:
        title = item.get("title", "Unknown")
        url = item.get("url", "Unknown")
        content = item.get("content", "No content available.")

        if len(content) > 500:
            content = content[:500] + "..."
        search_data += f"""
            Title : {title}
            URL : {url}

            Content : {content}
        """

        search_data += "\n"
        search_data += "=" * 50
        search_data += "\n\n"
    return search_data
        