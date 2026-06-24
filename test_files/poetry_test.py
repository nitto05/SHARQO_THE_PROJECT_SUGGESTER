import os
import sys

tools_dir = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "tools"
    )
)

sys.path.insert(0, tools_dir)


from poetrydb_tool import get_poems as gp

query = "Sonnet;Shakespeare"
va = gp
poem_data = va(query, ["title", "author"])

print(poem_data)