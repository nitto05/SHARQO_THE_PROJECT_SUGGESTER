from httpcore._async import connection_pool
from httpcore._async import connection_pool
from httpcore._async import connection_pool
from httpcore._async import connection_pool
from httpcore._async import connection_pool
from asyncio import protocols
import concurrent.futures
import time
import json
import importlib
import os
import re
from dotenv import load_dotenv
from google import genai
from tool_manager import get_file, get_func,tool_registery
from google.genai import types
from api_helper import safe_generate_json

def clean_term(text:str) -> str:
    """
    Cleans up search (e.g. removing parenthese and clean punctuation).
    Example : "Data Structures (lists, dictionaries) -> Data Structures"
    """

    if "(" in text:
        text = text.split("(")[0]

        text = text.replace(",", "").replace("-", "").strip()
        return re.sub(r'\s+', ' ', text)
def build_search_queries(services: list, concepts : list, mappings : list) -> dict:
    """
    Statistically constructs tool search queries using python string formatting.
    Returns a dictionary of {(category, item, tool) : query_string}
    """

    queries = {}

    for service, concept in mappings:
        clean_s = clean_term(service)
        clean_c = clean_term(concept)

        for tool in ["YOUTUBE", "GITHUB", "GOOGLE_BOOKS"]:
            queries[("service_with_concept", f"{service} + {concept}", tool)] = f"{clean_s} {clean_c}"

    for concept in concepts:
        clean_c = clean_term(concept)
        for tool in ["ARXIV", "GOOGLE_BOOKS", "YOUTUBE"]:
            queries[("concept", concept, tool)] = clean_c
    
    for service in services:
        clean_s = clean_term(service)
        for tool in ["YOUTUBE", "GITHUB", "GOOGLE_BOOKS"]:
            queries [("service", service, tool)] = clean_s
    return queries

def execute_single_tool(tool: str, query: str) -> tuple:
    """
    Dynamically loads and runs a search tool fucntion in a background thread.
    Restricts outputs to the top 5 items to save model context space.
    """

    try:
        file_name = get_file(tool)
        func_name = get_func(tool)

        module = importlib.import_module(f"tools.{file_name}")
        function = getattr(module, func_name)

        result = function(query)

        separator = "=" * 50
        if separator in result:
            parts = result.split(separator)
            if len(parts)> 5:
                result = separator.join(parts[:5]) + "\n" + separator
        return tool, result

    except Exception as e:
        return tool, f"Error running tool {tool}: {e}"
    
def fetch_resources_parallel(queries_dict: dict) -> dict:
    results = {}
    with concurrent.futures.ThreadPoolExecture() as executor:
        #submit all tasks
        future_to_task = {
            executor.submit(execute_single_tool, tool, query): (category, item, tool)
            for (category, item, tool), query in queries_dict.items()
        }
        #gather results
        for future in concurrent.futures.as_completed(future_to_task):
            category, item, tool = future_to_task[future]
            try:
                _, resource_text = future.result() #we dont again need the tool name(since it is mentioned in the loop context) that the future result returns

                results[(category, item, tool)] = resource_text
            except Exception as e:
                results[(category, item, tool)] = f"Exectution failed {e}"
    return results

def generate_study_guide(goal:str, retrieved_data: dict) -> str:
    """
    Sends the compiled search resources to gemini to generate 
    a structured study curriculum and roadmap
    """
    formatted_data = ""

    for (category, item, tool), content in retrieved_data.items():
        formatted_data += f"\n\n ==== Tool : {tool} | Target:{item} ==== \n\n{content}"
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

        Explain your reasoning briefly
        """
        try:
            client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

            config = types.GenerateContentConfig(
                temperature = 0.2,
                max_output_tokens = 2048
            )

            response = safe_generate_json(
                client = client,
                model = "gemini-2.5-flash",
                prompt = analysis_prompt,
                config = config,
                llm = "gemini"
            )

            return response.text
        except Exception as e:
            return f"Cloud synthesis failed ({e}). Returning raw links: \n {formatted_data}"








            