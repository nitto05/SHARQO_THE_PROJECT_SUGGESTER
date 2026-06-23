import requests
import xml.etree.ElementTree as ET

def get_papers(query):
    query = "+".join(query.split())

    url = "http://export.arxiv.org/api/query?search_query=all:" + query + "&start=0&max_results=20"
    response = requests.get(url)
    # return response.text

    root = ET.fromstring(response.text)

    paper_data = ""

    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        title = entry.find("{http://www.w3.org/2005/Atom}title")
        summary = entry.find("{http://www.w3.org/2005/Atom}summary")
        published = entry.find("{http://www.w3.org/2005/Atom}published")
        # print(title.text)

        pdf_link = ""

        for link in entry.findall("{http://www.w3.org/2005/Atom}link"):
            if link.get("title") == "pdf":
                pdf_link = link.get("href")
        

        paper_data += f"""
            Title: {title.text.strip()}
            published : {published.text.strip()}
            Abstract : {summary.text[:300]}
            pdf : {pdf_link}
        """
    return paper_data

