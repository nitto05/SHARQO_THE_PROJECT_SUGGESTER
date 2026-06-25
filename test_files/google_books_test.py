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

from google_books_tool import get_google_books

results = get_google_books("machine learning")

print (results)