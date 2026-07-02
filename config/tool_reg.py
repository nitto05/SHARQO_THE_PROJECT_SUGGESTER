TOOL_REGISTRY = {
    "GITHUB": {
    "valid" : True,

    "id_rules": {
        "projects",
        "repositories",
        "source code",
        "implementation examples",
        "learning by building",
        "open-source tools"
    },

    "search_rules": (
        "Convert the following request into a GitHub repository search query.\n"
        "Focus on repositories, frameworks, implementations and open-source projects.\n"
        "Return only the search query."
    ),

    "file_name": "github_tool",

    "function_name": "get_repositories"
},
"ARXIV": {
    "valid" : True,

    "id_rules": {
        "research papers",
        "academic publications",
        "surveys",
        "thesis topics",
        "scientific literature",
        "state-of-the-art research"
    },

    "search_rules": (
        "Convert the user's request into a good arXiv search query.\n"
        "Focus on research topics, surveys and academic terminology.\n"
        "Return only the search query."
    ),

    "file_name": "arxiv_tool",

    "function_name": "get_papers"
},
"CROSSREF": {
    "valid" : True,

    "id_rules": {
        "journal articles",
        "journal papers",
        "conference papers",
        "citations",
        "DOI information",
        "scholarly publications"
    },

    "search_rules": (
        "Convert the user's request into a good Crossref search query.\n"
        "Focus on journal papers, conference papers and scholarly terminology.\n"
        "Return only the search query."
    ),

    "file_name": "crossref_tool",

    "function_name": "get_crossref_papers"
},
"PUBMED": {
    "valid" : True,

    "id_rules": {
        "medicine",
        "healthcare",
        "biology",
        "biomedical research",
        "clinical studies",
        "diseases",
        "drugs",
        "genetics",
        "public health"
    },

    "search_rules": (
        "Convert the user's request into a good PubMed search query.\n"
        "Focus on medicine, healthcare, biology and biomedical terminology.\n"
        "Return only the search query."
    ),

    "file_name": "pubmed_tool",

    "function_name": "get_pubmed_papers"
},
"POETRYDB": {
    "valid" : True,

    "id_rules": {
        "poetry",
        "poems",
        "poets",
        "literature",
        "verses",
        "rhymes",
        "poetry collections",
        "famous poems",
        "literary works"
    },

    "search_rules": (
    "Return a JSON object with the following format:\n"
    '{'
    '"query": "<search text>",'
    '"fields": ["lines"]'
    '}\n'
    "Do not return anything else."
    ),

    "file_name": "poetrydb_tool",

    "function_name": "get_poems"
},
"OPEN_LIBRARY": {
    "valid" : True,

    "id_rules": {
        "books",
        "novels",
        "authors",
        "literature",
        "reading",
        "book recommendations",
        "ISBN",
        "classic books",
        "publications"
    },

    "search_rules": (
        "Convert the following request into an Open Library search query.\n\n"
        "Focus on books, novels, textbooks, authors, literature,\n"
        "reading materials, educational resources, ISBNs and subjects.\n\n"
        "Include important keywords.\n"
        "Remove unnecessary words.\n"
        "Keep the query concise.\n"
        "Return ONLY the query."
    ),

    "file_name": "open_library_tool",

    "function_name": "get_books"
},
"GOOGLE_BOOKS": {
    "valid" : True,

    "id_rules": {
        "books",
        "ebooks",
        "authors",
        "educational books",
        "textbooks",
        "reading",
        "book recommendations",
        "publications"
    },

    "search_rules": (
        "Convert the following request into a Google Books search query.\n"
        "Focus on books, textbooks, authors and educational materials.\n"
        "Return only the search query."
    ),

    "file_name": "google_books_tool",

    "function_name": "get_google_books"
},
"YOUTUBE": {
    "valid" : True,

    "id_rules": {
        "video tutorials",
        "courses",
        "lectures",
        "educational videos",
        "content creation",
        "entertainment",
        "channels",
        "playlists",
        "learning resources"
    },

    "search_rules": (
        "Convert the following request into a YouTube search query.\n"
        "Focus on tutorials, lectures, educational videos and useful channels.\n"
        "Return only the search query."
    ),

    "file_name": "youtube_tool",

    "function_name": "get_youtube_videos"
},
"ALPHA_VANTAGE": {
    "valid" : False,

    "id_rules": {
        "stocks",
        "finance",
        "investing",
        "market analysis",
        "company fundamentals",
        "technical indicators",
        "forex",
        "cryptocurrencies",
        "financial data"
    },

    "search_rules": (
        "Convert the following request into an Alpha Vantage search query.\n"
        "Focus on stocks, companies, market data and financial analysis.\n"
        "Return only the search query."
    ),

    "file_name": "alpha_vantage_tool",

    "function_name": "get_market_data"
},
"NEWS_API": {
    "valid" : False,

    "id_rules": {
        "news",
        "current events",
        "headlines",
        "world affairs",
        "technology news",
        "business news",
        "politics",
        "sports news",
        "trending topics"
    },

    "search_rules": (
        "Convert the following request into a News API search query.\n"
        "Focus on recent news, current events and trending topics.\n"
        "Return only the search query."
    ),

    "file_name": "news_tool",

    "function_name": "get_news"
},
"RAWG": {
    "valid" : False,

    "id_rules": {
        "games",
        "gaming",
        "video games",
        "game recommendations",
        "game databases",
        "multiplayer games",
        "RPG",
        "FPS",
        "gaming platforms",
        "game reviews"
    },

    "search_rules": (
        "Convert the following request into a RAWG API search query.\n"
        "Focus on video games, game databases, recommendations and gaming platforms.\n"
        "Return only the search query."
    ),

    "file_name": "rawg_tool",

    "function_name": "get_games"
},
"API_FOOTBALL": {
    "valid" : False,

    "id_rules": {
        "football",
        "soccer",
        "matches",
        "leagues",
        "teams",
        "players",
        "standings",
        "fixtures",
        "scores",
        "sports statistics"
    },

    "search_rules": (
        "Convert the following request into an API-Football search query.\n"
        "Focus on football teams, leagues, fixtures, scores and player statistics.\n"
        "Return only the search query."
    ),

    "file_name": "football_tool",

    "function_name": "get_football_data"
},
"WGER": {
    "valid" : False,

    "id_rules": {
        "fitness",
        "gym",
        "workouts",
        "exercises",
        "bodybuilding",
        "strength training",
        "weight loss",
        "muscle building",
        "health",
        "fitness routines"
    },

    "search_rules": (
        "Convert the following request into a Wger Workout API search query.\n"
        "Focus on exercises, workouts, muscle groups, fitness routines "
        "and strength training.\n"
        "Return only the search query."
    ),

    "file_name": "wger_tool",

    "function_name": "get_workouts"
}
}