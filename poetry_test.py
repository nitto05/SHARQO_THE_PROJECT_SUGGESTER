from tools.poetrydb_tool import get_poems as gp

query = "Sonnet;Shakespeare"
va = gp
poem_data = va(query, ["title", "author"])

print(poem_data)