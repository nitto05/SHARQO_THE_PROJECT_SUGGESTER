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


from pubmed_tool import get_pubmed_papers

ids = get_pubmed_papers("alzheimer disease")

print(ids)