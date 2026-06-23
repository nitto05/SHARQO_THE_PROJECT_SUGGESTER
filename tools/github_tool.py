import requests
import base64

def get_readme(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return "README not found"
    encoded = response.json()["content"]

    decoded = base64.b64decode(encoded)
    return decoded.decode("utf-8")

# search = input("what do you want??? : ")
# query = format(search)
def get_repositories(search):
    query = "+".join(search.split())
    url = "https://api.github.com/search/repositories?q=" + query +"&sort=stars&order=desc"

    response = requests.get(url)
    data = response.json()
    repo_data = ""

    for repo in data["items"][:10]:
        # print(repo["name"])
        readme = get_readme (repo["owner"]["login"], repo["name"])

        repo_data += f"""
        Name: {repo["name"]}
        Owner: {repo["owner"]["login"]}
        Stars: {repo["stargazers_count"]}
        Description: {repo["description"]}
        url : {repo["html_url"]}
        language : {repo ["language"]}
        forks_count : {repo ["forks_count"]}
        html_url : {repo ["html_url"]}
        topics : {repo ["topics"]}
        README : {readme[:300]}
        """

    return repo_data