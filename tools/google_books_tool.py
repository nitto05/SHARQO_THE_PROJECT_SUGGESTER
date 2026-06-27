import requests
# import os
# import sys

# utils_dir = os.path.abspath(
#     os.path.join(
#         os.path.dirname(__file__),
#         "..",
#         "utils"
#     )
# )

# sys.path.insert(0, utils_dir)
# from api_keys import get_api_key

from dotenv import load_dotenv
import os

load_dotenv()   # Loads variables from .env

# youtube_key = os.getenv("YOUTUBE_API_KEY")
api_key = os.getenv("GOOGLE_BOOKS")

# base_url = "https://www.googleapis.com/books/v1/volumes" 

# api_key = get_api_key("GOOGLE_BOOKS")

base_url = "https://www.googleapis.com/books/v1/volumes"

def get_google_books(query, max_results = 10):
    
    # query = "+".join(keyword.strip() for keyword in query.split())

    # url =
    params = {
        "q" : query,
        "maxResults" : 10,
        "key" : api_key
    }

    print(base_url)
    print(params)

    try: 

        response = requests.get(base_url, params = params)

        response.raise_for_status ()

        data = response.json()
    except Exception as e:
        return f"Unable to fetch books...\n {e}"
    if "items" not in data :
        return "No books found..."
    seen = set()

    book_data = ""

    for book in data ["items"]:
        info = book.get("volumeInfo", {})

        book_id = book.get("id")
        if book_id in seen :
            continue
        seen.add(book_id)

        title = info.get("title", "Unknown")
        authors = ", ".join(info.get("authors", ["Unknown"])[:3])

        publisher = info.get("publisher", "unknwon")

        published = info.get("publishedDate", "Unknown")

        pages = info.get("pageCount", "Unknown")

        language = info.get("language", "Unknown")

        categories = ", " .join (info.get("categories", ["Unknown"]))

        isbn = "Unknown"

        if "industryIdentifiers" in info:
            isbn = info["industryIdentifiers"][0].get("identifier", "Unknown")
        
        rating = info.get("averageRating", "Not Rated")

        ratings = info.get("ratingCount", 0)

        preview = info.get("previewLink", "N/A")

        info_link = info.get("infoLink", "N/A")

        description = info.get("description", "No description available")

        if len(description) > 300:
            description = description[:300] + "..."
        book_data += f""" 
Title : {title}
Author(s) : {authors}
Publisher : {publisher}
Published on : {published}
Pages : {pages}
ISBN : {isbn}
Languages : {language}
Categories = {categories}
Average Rating : {rating}
Ratings Count : {ratings}

Description : 
{description}

preview : 
{preview}

More Information : 
{info_link}

"""
        
        book_data += "\n"
        book_data += "=" * 50
        book_data += "\n\n"

    return book_data