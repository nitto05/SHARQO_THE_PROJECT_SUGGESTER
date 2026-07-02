import requests

def get_poems(query, fields = ["lines"], limit = 5):
    # query = ";".join(keyword.strip() for keyword in query.split(","))
    field_string = ",".join(fields)
    url = (
        f"https://poetrydb.org/{field_string}/{query}"
        # + query
    )

    print(url)

    try : 
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    
    
    except Exception as e: 
        print(e)
        return "Unable to fetch poems..."
    
    
    if isinstance(data, dict) and  "status" in data : 
        return "No poems found..."
    
    seen = set()
    poem_data = ""

    for poem in data [:limit]: 
        identifier = (poem["title"], poem["author"])

        if identifier in seen :
            continue

        seen.add(identifier)
        
        poem_data += f""" 
            Title : {poem['title']}
            Author : {poem['author']}
        """

        poem_data += "\n".join(poem["lines"])
        poem_data += "\n\n"
        poem_data += "=" * 30
        poem_data += "\n\n"
    return poem_data