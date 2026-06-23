import requests

def get_books(query):

    query = "+". join(keyword.strip() 
                       for keyword in query.split()
                       )

    url = f"https://openlibrary.org/search.json?q={query}"

    try:
        response = requests.get(url)

        response.raise_for_status()
        data = response.json ()
    except Exception as e:
        return f"Unable to fetch books... \n {e}"
    if data["numFound"] == 0:
        return "No books found..."
    
    seen = set() #this stores the list of found books

    book_data = ""

    for books in data ["docs"][:10]:
        title = books.get("title", "unknown")

        authors = ", ".join(books.get("author_name", ["Unknown"])[:3])

        identifier = (title, authors)

        if identifier in seen :
            continue
        seen.add(identifier)
        year = books.get("first_publish_year", "Unknown")

        edition_count = books.get("edition_count", "Unknown")

        language = ", ".join(books.get("language", [])[:3])

        isbn = "Unknown"

        if "isbn" in books:
            isbn = books["isbn"][0]
        
        

        book_data += f"""
Title : {title}
Author(s) : {authors}
First Published : {year}
Edition Count : {edition_count}
ISBN : {isbn}
Languages : {language}
    """
        book_data += "\n"
        book_data += "=" * 50
        book_data += "\n\n"
    return book_data