from google import genai
from tools.github_tool import get_repositories, get_readme

# client = genai.Client(api_key="AQ.Ab8RN6LH84vj_fFBjgtDsdiSsi8lYJ4vtVmSqViPIFDi4rJrCg")

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