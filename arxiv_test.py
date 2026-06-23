from tools.arxiv_tool import get_papers

papers = get_papers("physics")

print(papers[:2000])
