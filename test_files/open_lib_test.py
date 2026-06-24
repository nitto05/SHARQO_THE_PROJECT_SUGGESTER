# test_open_library.py

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

from open_library_tool import get_books

query = "machine learning"

book_data = get_books(query)

print(book_data)