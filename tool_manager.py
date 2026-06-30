# import json
# from dotenv import load_dotenv
# import os

# load_dotenv()   # Loads variables from .env

# # youtube_key = os.getenv("YOUTUBE_API_KEY")
# # gemini_key = os.getenv("GEMINI_API_KEY")

# tool_registry = json.loads(os.getenv("TOOL_REGISTRY"))
from config.tool_reg import TOOL_REGISTRY

tool_registry = TOOL_REGISTRY

# print(type(tool_registry))

def get_rules():
    idRules = ""

    for tools in tool_registry:
        if(tool_registry[tools]["valid"]):
            text = f"- Return {tools} if the user is looking for:\n"
            idRules += text
            for rules in tool_registry[tools]["id_rules"]:
                idRules +=  f"- {rules} \n"
            idRules += f"\n"
    return idRules

def get_search_rules(): #selection is a list of valid tools
    
    search_rules = dict()

    for tools in tool_registry:
        rule = tool_registry[tools]["search_rules"]
        search_rules[tools] = rule
    return search_rules

def get_file (tool):
    return tool_registry[tool]["file_name"]

def get_func (tool):
    return tool_registry[tool]["function_name"]

print(get_rules())
print(get_search_rules())
print(get_file("GITHUB"))
print(get_func("GITHUB"))