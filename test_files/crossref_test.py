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

from crossref_tool import get_crossref_papers

papers = get_crossref_papers ("ai agents")

print(papers)

