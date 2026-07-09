from google import genai
from tools.github_tool import get_repositories, get_readme

from dotenv import load_dotenv
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = gemini_key)

goal = input("waht do you want to learn? : ")
repo_data = get_repositories (goal)
response = client.models.generate_content(
    # model="gemini-2.5-flash",
    # model = "gemini-2.0-flash",
    model="gemini-2.5-flash-lite",
    
    contents= f""" 
    a student wants to learn about {goal} and give him details about {repo_data}
    for each repo :
    1. explain waht it teaches
    2. difficulty level
    3. who should use it
    4. learning value
    5. resume value
    
    rank them from best to worst for beginner...""" )

print(response.text)

# print(get_readme("inkeep", "agents")[:1000])