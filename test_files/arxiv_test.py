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

from arxiv_tool import get_papers

papers = get_papers("physics")

print(papers[:2000])
