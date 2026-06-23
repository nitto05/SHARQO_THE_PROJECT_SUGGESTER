import requests

def get_crossref_papers(query):
    query = "+".join(query.split())

    url = (
        "https://api.crossref.org/works?"
        + "query="
        + query
        + "&rows=10"
    )

    response = requests.get(url)

    data = response.json()

    paper_data = ""

    for item in data["message"]["items"][:10]:

        title = item.get("title", ["No Title"])

        year = "unknown"

        if "published-print" in item:
            year = item["published-print"]["date-parts"][0][0]
        elif "published-online" in item:
            year = item["published-online"]["date-parts"][0][0]
        doi = item.get("DOI", "N/A")

        paper_data += f"""
                    Title : {title[0]}
                    Year : {year}
                    DOI : {doi}

                        """
    return paper_data