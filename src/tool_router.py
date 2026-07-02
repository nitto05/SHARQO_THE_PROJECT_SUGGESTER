import time
import json
import importlib
# import os
from google import genai
# from tools.github_tool import get_repositories
# from tools.arxiv_tool import get_papers
# from tools.crossref_tool import get_crossref_papers
# from tools.pubmed_tool import get_pubmed_papers
from tool_manager import get_rules, get_search_rules, get_file, get_func
from dotenv import load_dotenv
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

load_dotenv()   # Loads variables from .env

# youtube_key = os.getenv("YOUTUBE_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")

# print(youtube_key)
# print(gemini_key)



client = genai.Client (api_key = gemini_key)


# goal = input("what do you need??? : ")
start = time.time()
    


prompt = f"""
User request:

{goal}

Rules:

{get_rules()}

Query Generation Rules:

{get_search_rules()}


Rules:

- Return ALL relevant categories.
- Categories must be comma-separated.
- If only one category is relevant, return only that category.
- If multiple categories are relevant, return all of them.
- Do not explain.
- Do not add extra text.

Output a dictionary where the keys are the selected tools and the value for each key is query for that specific tool:

Return ONLY a valid JSON object.

Do NOT include any explanation.

Do NOT use Markdown.

Do NOT wrap the JSON inside ```json or ```.

Your response must start with {{ and end with }}.


"""

# prompt = f"""
# User request:

# {goal}

# Determine:

# 1. Which tools should be used
# 2. A search query suitable for all selected tools

# Available tools:

# GITHUB
# ARXIV
# CROSSREF
# PUBMED

# Output EXACTLY in this format:

# TOOLS: tool1,tool2,...

# QUERY: search query

# Example:

# TOOLS: GITHUB,ARXIV

# QUERY: ai agents

# Do not explain.
# Do not add extra text.
# """

response = client.models.generate_content(
    # model="gemini-2.5-flash",
    # model = "gemini-2.0-flash",
    model="gemini-2.5-flash", # gemini-2.5-flash-lite or gemini-2.5-flash
    
    contents= prompt
    
)


# choice = response.text.strip().upper()

print("Raw Gemini Output:")
print(response.text)

# lines = response.text.strip().split("\n")

# tools_line = ""
# # query_line = ""
# queries = {}

# for line in lines:
#     line = line.strip()

#     if line.startswith("TOOLS:"):
#         tools_line = line
#     elif "_QUERY:" in line:
#         # query_line = line
#         key, value = line.split(":", 1)

#         queries[key.strip()] = value.strip() 

# tools_text = tools_line.split(":", 1)[1]
# choices = [
#     tool.strip().upper()
#     # for choice in response.text.split(",")

#     for tool in tools_text.split(",")

# ] # gathers all the choices made by the agent

# # search_query = query_line.replace("QUERY:", "").strip()

########## this dictionary should be stored in database...

tool_quer = json.loads(response.text)

choices = tool_quer.keys()
queries = list()

for tool, query in tool_quer.items():
    print(tool, query)



all_data = {}


###########
# for tool in tool_quer:
    
#     module_name = "tools." + get_file(tool)
#     module = importlib.import_module(module_name)
#     function = getattr(module, get_func(tool))
#     all_data [tool] = function(tool_quer[tool]) + "\n\n"

for tool, query in tool_quer.items():

    print(f"\nRunning {tool}...")
    print(f"Query: {query}")

    module_name = "tools." + get_file(tool)
    module = importlib.import_module(module_name)
    function = getattr(module, get_func(tool))

    # result = function(query)
    params = tool_quer[tool]
    if isinstance(params, dict):
        result = function(**params)
    else : 
        result = function(params)

    print(f"{tool} finished.")
    print(f"Result length: {len(result)}")

    all_data[tool] = result








# if "GITHUB" in choices and "GITHUB_QUERY" in queries:

    

#     print("Searching GitHub...")
#     repo_data = get_repositories(queries["GITHUB_QUERY"])

#     # print(repo_data)
#     # all_data += "\n\n === GITHUB === \n\n"
#     # all_data += repo_data
#     all_data["GITHUB"] = repo_data

# if "ARXIV" in choices and "ARXIV_QUERY" in queries:

    
    
#     print("Searching Arxiv...")
#     arxiv_data = get_papers(queries["ARXIV_QUERY"])

#     # print(paper_data)
#     # all_data += "\n\n === ARXIV === \n\n"
#     # all_data += paper_data
#     all_data["ARXIV"] = arxiv_data

    
# if "CROSSREF" in choices and "CROSSREF_QUERY" in queries:

    

#     print("Searching Crossref...")
#     crossref_data = get_crossref_papers(queries["CROSSREF_QUERY"])

#     # print(crossref_data)
#     # all_data += "\n\n === CROSSREF === \n\n"
#     # all_data += crossref_data
#     all_data["CROSSREF"] = crossref_data

# if "PUBMED" in choices and "PUBMED_QUERY" in queries:

    

#     print("Searching PubMed...")
#     pubmed_data = get_pubmed_papers(queries["PUBMED_QUERY"])

#     # print(pubmed_data)
#     # "\n\n === PUBMED === \n\n"
#     # all_data += pubmed_data
#     all_data["PUBMED"] = pubmed_data

# # print(all_data)
for source, results in all_data.items():
    # formatted_data += f"\n\n ==== {source} ==== \n\n"
    # formatted_data += results
    print(f"\n\n ==== {source} ====\n\n")
    print(results)




print("\nGenerating analysis...\n")

formatted_data = ""

for source, results in all_data.items():
    formatted_data += f"\n\n ==== {source} ==== \n\n"
    formatted_data += results

analysis_prompt = f"""
USER GOAL:

{goal}

Retrieved Resources:

{formatted_data}

Act as an expert mentor.

Analyze the resources and provide:

1. Top 5 resources overall
2. Top 3 beginner resources
3. Top 3 advanced resources
4. Best projects to build
5. Best research papers to read
6. Recommended reading order
7. 30-day learning roadmap
8. Skills that will be learned
9. Resources that can be skipped initially

Explain your reasoning briefly.
"""

analysis_response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=analysis_prompt
)
final_analysis = analysis_response.text
print("\n ==== FINAL ANALYSIS ==== \n")
print(final_analysis)

end = time.time()

print(f"completed in {end-start} seconds")

