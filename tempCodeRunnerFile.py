from tools.poetrydb_tool import get_poems

query = "nature"

poem_data = get_poems(query)

print(poem_data)