# test_open_library.py

from tools.open_library_tool import get_books

query = "machine learning"

book_data = get_books(query)

print(book_data)