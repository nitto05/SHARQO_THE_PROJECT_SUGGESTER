import requests

def search_pubmed(query):
    query = "+".join(query.split())

    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        "?db=pubmed"
        "&retmode=json"
        "&retmax=10"
        "&term=" + query
        )
    response = requests.get(url)

    data = response.json()

    return data["esearchresult"]["idlist"]

def get_pubmed_papers(query):
    ids = search_pubmed(query)

    id_string = ",".join(ids)

    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        "?db=pubmed"
        "&retmode=json"
        "&id=" + id_string
        )
    response = requests.get(url)

    data = response.json()
    # print(data["result"][ids[0]])

    paper_data = ""

    for pmid in ids : 

        paper = data["result"][pmid]

        paper_data += f"""
Title : {paper.get('title', 'No Title')}
Published : {paper.get('pubdate', 'unknown')}
PMID : {pmid}
"""
    return paper_data


