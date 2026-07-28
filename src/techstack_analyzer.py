from urllib3 import response
import requests 
from bs4 import BeautifulSoup


import json
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import sys
from pathlib import Path
from api_helper import safe_generate_json
from local_llm_client import query_local_llm

tools_dir = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "tools"
    )
)

sys.path.insert(0, tools_dir)

from web_search_tool import get_search_results as web_search

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

client = genai.Client(api_key = gemini_key)



def scrape_page(url: str, llm : str = "gemini", concepts : str = "") -> str:
    """
    Scrapes a webpage and processes it:
    - Gemini: Extracts technology name listings.
    - Qwen: Evaluates architectural compatibility and setup templates.
    """

    try:
        response = requests.get(url, timeout = 10)
        soup = BeautifulSoup (response.text, "html.parser")
        raw_text = soup.get_text(separator = "", strip = True)[:3000]
    # except Exception as e :
    #     return f"[Error scraping {url} : {str(e)}]"
        if llm == "gemini" :
            filter_prompt = f"""
            You are a tech stack extraction bot.
    You were given this raw text scraped from a website.
    Your job is to:
    1. Decide if this text is relevant to tech stack selection. (YES or NO)
    2. If YES, extract only the technology names mentioned (libraries, frameworks, databases, tools).
    3. Return a structured JSON list.
    Text:
    {raw_text}
            """
            print(f"[Scraper] Parsing page details via Gemini Cloud...")
            

            filter_response = client.models.generate_content(
                model = "gemini-2.5-flash-lite",
                contents = filter_prompt
            )
            return filter_response.text

        elif llm == "qwen" :
            compatibility_prompt = f"""
                You are a Software Compatibility and Feature Analyzer.
            You are given this raw documentation text scraped from a website:
            
            {raw_text}
            
            We want to verify if this technology can implement these specific concepts:
            Target Concepts: {concepts}
            
            Analyze the documentation and output:
            1. Which of the target concepts can ACTUALLY be implemented using this technology? (List them).
            2. Explain briefly how this technology implements each of those concepts based on the documentation.
            3. Are there any known conflicts or version locks (e.g. CUDA, Python versions) mentioned?
            """
            print(f"[Scraper] Verifying concept compatibility locally using Qwen...")
            filter_response = query_local_llm(compatibility_prompt, max_tokens= 384, temperature = 0.1)
            return filter_response
    
    except Exception as e:
        return f"[Error scraping {url} : {str(e)}]"




def get_techstack(details:dict, ind_roadmap:str) -> dict:

    # goal = input ("HOW MAY WE HELP YOU??? : ")
    goal = details["goal"]
    # exp = input("what is your experience??? : ")
    exp = details["exp"]
    # time = input("how much time??? : ")
    time = details ["time"]
    op_format_simple = """{
    "techstack" : [],
    "concepts" : [],
    "domain" : [],
    "apis" : [],
    "optional_features" : []
    }"""

    op_format_phased = """{
    "techstack" : {"phase1" : [], "phase2" : []},
    "concepts" : {"phase1" : [], "phase2" : []},
    "domain" : [],
    "apis" : {"phase1" : [], "phase2" : []},
    "optional_features" : {"phase1" : [], "phase2" : []}
    }"""

    if (int(time) <= 4):
        op_format = op_format_simple
    else:
        op_format = op_format_phased

    prompt = f"""
You are an expert Software Architect and Technical Mentor.
A user has described a software project.
Your task is NOT to recommend learning resources.
Your task is to analyze the project idea and infer everything that a developer would need to build it.
User Project Goal:
{goal}
Project Roadmap & Modules:
{ind_roadmap}
Developer Experience:
{exp}
Available Development Time:
{time}

Architectural Search & Synthesis Workflow:
Simulate the following workflow of an advanced developer starting a project from scratch:

1. Classify the Project Type:
   First, identify what kind of deliverable this project produces. Examples:
   - Web Application (browser-accessible frontend + API backend)
   - Mobile Application (iOS/Android native or cross-platform)
   - Desktop Application (GUI on Windows/macOS/Linux)
   - CLI Tool (terminal-based, no UI)
   - API/Backend Service (no frontend, just endpoints)
   - Data Pipeline (batch processing, ETL, automation)
   - Embedded/IoT System (hardware-attached software)
   - Hybrid (e.g., a web app with a mobile companion app)
   A project may belong to more than one type.

2. Segment into Architectural Pillars:
   Based on the project type, select ONLY the architectural pillars that are relevant:
   - INTERFACE: How users interact with the system (Frontend, Mobile UI, Desktop GUI, CLI, None).
   - SERVER: How the business logic is hosted and routed (API backend, serverless functions, none if client-side only).
   - BRAIN: Core computational logic (LLM interaction, ML models, rule engines, algorithms, data processing).
   - STORAGE: How data is persisted (relational DB, vector DB, object storage, file system, none if stateless).
   - INFRASTRUCTURE: Deployment, CI/CD, containerization (only if the project scope requires it).
   Do NOT force pillars that do not apply.

3. Look for Precedents:
   For each active pillar, use the web_search tool to find similar successful open-source projects at the appropriate experience level.
   Combine the most common, well-maintained libraries from those precedents.

4. Verify via Developer Search:
   Use the web_search and scrape_page tools to prioritize technologies with active community support, modern documentation, and clear beginner integration guides.
   Reject libraries that are outdated, unmaintained, or have high setup friction for the given experience level.


Analyze the project and identify:
1. Tech Stack
- Programming Languages
- Frameworks
- Libraries
- Databases
- Cloud Services
- Deployment Technologies
- DevOps Tools
2. Core Concepts
- Computer Science Concepts
- AI / ML Concepts
- Software Engineering Concepts
- Networking Concepts
- Database Concepts
- Mathematical Concepts
- Any other important technical concepts
3. Domain Knowledge
Determine the application's domain(s).
4. APIs / External Services
Infer useful APIs or external services.
5. Optional Features
Suggest additional features that are realistic for the given experience level and available development time.
Rules:
Rules:
- MANDATORY TOOL CALL: You are STRONGLY REQUIRED to execute at least two web_search tool calls BEFORE generating any JSON output. Do NOT rely solely on internal training memory.
- Infer missing requirements logically.
- Do not include explanations.
- Remove duplicates.
- Use concise names.
- Return only valid JSON.
- Do not use Markdown.
- Do not wrap the JSON inside triple backticks.
Experience Rules:
If the developer is a Beginner:
- Prioritize simplicity and minimize setup complexity.
- Choose low-boilerplate, fast-prototyping frontend tools (e.g., Streamlit, Gradio) over full MVC frameworks (e.g., Django, Flask, React) unless required by project scale.
- Prefer free and open-source tools with managed free tiers.
- Avoid enterprise or self-hosted container technologies unless absolutely necessary.
If the developer is Intermediate:
- Recommend industry-standard technologies and professional development practices.
- Balance simplicity and scalability.
- Assume comfort learning moderately advanced engineering concepts.
If the developer is Advanced:
- Recommend the most suitable production-grade architecture (e.g., Microservices, Event-driven).
- Optimize strictly for scalability, maintainability, and performance.
Time Rules:
The available development time determines the scope of the project.
- Short durations (under 4 weeks) must focus strictly on an MVP.
- Medium durations (4-8 weeks) should introduce essential data persistence and cleaner separation of concerns.
- Long durations (over 8 weeks) should recommend production-ready architectures, pipelines, and advanced features.
Selection Rules:
- Redundancy Suppression: Never pair wrapper frameworks (e.g., LangChain, LlamaIndex) with a provider's native SDK (e.g., google-generativeai) in Phase 1; prioritize direct SDK usage to keep boilerplate low.
- Ecosystem Deduplication: Do not list generic cloud ecosystems (e.g., Google Cloud Platform) or sub-components (e.g., PostgreSQL) if specific targets (e.g., Google Gemini API, Supabase) are already declared.
- Recommend only technologies appropriate for BOTH the experience level AND timeline.
- Do NOT list every alternative; choose the single best-fit technology for each role.
- Order every list from highest priority/execution sequence to lowest.
Phase Rules:
- Phase 1 must contain everything required to build the first complete working version (MVP).
- Phase 2 must contain ONLY upgrades, enhancements, scalability improvements, or features added after Phase 1 is complete.
- Strict Exclusion Rule: Do not repeat any technological dependency (e.g., specific languages or core frameworks like Python or React) in Phase 2 if they are already declared in Phase 1. Phase 2 lists only additions.
- Feature Alignment: If a feature is purely analytical or programmatic (e.g., prompt logic, structured LLM JSON outputs), it belongs in Phase 1. Do not push pure logic features to Phase 2 if they rely on Phase 1 tech. Phase 2 features should focus on infrastructure changes (e.g., adding user auth, cloud sync, data persistence).
- Dynamic Scaling Rule: Phase 1 must focus exclusively on in-memory, local execution. For an MVP, data should live inside application variables or transient session state. Do NOT include cloud databases, external database client libraries, or user authentication in Phase 1, as configuring them during week one creates boilerplate friction for a beginner. Move persistent cloud storage, database integrations (like Supabase/Firebase), and authentication strictly into Phase 2 as scalability and data-retention upgrades.
Technology Selection & Architectural Compatibility Rules:
- Every recommended technology must have an explicit purpose. Do not recommend tools that duplicate roles.
- ARCHITECTURAL LOCK-IN: Ensure Phase 1 and Phase 2 architectures are vertically compatible. Never recommend a Phase 1 framework that must be completely deleted or rewritten to implement Phase 2. Phase 2 must naturally extend Phase 1.
- INFRASTRUCTURE SANITY CHECK: Ensure your deployment target handles your database selection natively. If you use a cloud provider with an ephemeral file system (e.g., Render free tier, Heroku), do NOT pair it with a file-based database (e.g., SQLite) without explicitly addressing persistent disks, or swap the database to a serverless/cloud database API (e.g., Supabase, MongoDB Atlas) to prevent instant data loss.
- RUNTIME SANITY CHECK: Identify the chosen framework's core execution behavior.
- PIPELINE PREREQUISITES: If an API library (e.g., google-genai) relies heavily on data schemas or local keys for its core feature to work cleanly, instantly include its dependent tools (e.g., Pydantic for structured JSON matching, python-dotenv for API keys) into Phase 1 alongside it.
- Deployment Streamlining: Match your deployment target strictly to your framework.
Return exactly in this format:
{op_format}
"""

    try:
        config = types.GenerateContentConfig(tools = [web_search, scrape_page])
        response = safe_generate_json(client, "gemini-2.5-flash", prompt, config)
        res = response.text.strip()

        try:
            json.loads(res)
            with open("techstack_cache.json", "w", encoding = "utf-8") as f:
                f.write(res)
        except Exception as cache_err:
            print(f"Warning: Failed to update techstack cache: {cache_err}")
    except Exception as e:
        cache_path = "techstack_cache.json"
        if os.path.exists(cache_path):
            print(f"Live techstack API call failed ({e}). Returning cached techstack.")
            with open(cache_path, "r", encoding = "utf-8") as f:
                res = f.read()
        else:
            raise e
    # print("RAW RESPONSE:", res)  # add this to see what came back
    # print("CANDIDATES:", response.candidates)  # shows tool call vs text


    # if res is None:
    #     print("Gemini returned None — likely made tool calls without final text")
    #     print("Full response:", response)
    #     return "{}"  # return empty JSON safely


    res = res.strip()

    if res.startswith("```json"):
        res = res [7:]
    elif res.startswith("```"):
        res = res[3:]
    if res.endswith("```"):
        res = res [:-3]

    res = res.strip()

    concept_map = {}

    try : 
        res_dict = json.loads(res)

        # tech_list = []
        # raw_tech = res_dict.get("techstack", [])
        # if isinstance(raw_tech, dict):
        #     for phase, list_of_techs in raw_tech.items():
        #         if isinstance(list_of_techs, list):
        #             tech_list.extend()

        # phase wise learning...
        

        fin_data = dict()
        fin_data ["techstack"] = list(set(res_dict["techstack"]["phase2"]).union(set(res_dict["techstack"]["phase1"])))
        fin_data ["concepts_p1"] = (res_dict["concepts"]["phase1"])
        fin_data ["concepts_p2"] = (res_dict["concepts"]["phase2"])

        concepts_p1 = fin_data["concepts_p1"]
        concepts_p2 = fin_data["concepts_p2"]

        concept_map = {}

        print("\n Starting Phase targeted compatibility loop...")

        for tech in fin_data["techstack"]:
            print(f"\n Analyzing {tech}...")
            q1_prompt = f"""
                You are a Search Optimizer. Write a single search query to verify if the technology '{tech}' can implement these Phase 1 concepts:
                {", ".join(concepts_p1)}

                Return ONLY the plain text search query. Do not add quotes, explanations, or markdown.
            """
            query_p1 = query_local_llm(q1_prompt, max_tokens = 32, temperature = 0.1).strip().replace('"', '').replace("'", "")

            results_p1 = web_search(query_p1)

            verify_p1_prompt = f"""
                You are a technical Allocator. Read this search context:
                {results_p1}

                Determine which of the following Phase 1 concepts can ACTUALLY be implemented by '{tech}' :
                Target Concepts : {", ".join(concepts_p1)}

                Return a raw JSON list of only the concepts from the target list that are compatible.
                Example format:
                ["HTTP/REST", "API Design"]
                Do not include markdown wraps(```) or explanation text. 
            """
            raw_res_p1 = query_local_llm(verify_p1_prompt, max_tokens = 128, temperature = 0.1)
            try:
                matched_p1 = json.loads(raw_res_p1.replace("```json", "").replace("```", "").strip())
            except Exception : 
                matched_p1 = []

            q2_prompt = f"""
                You are a Search Optimizer.
                Write a single search query to verify if the technology '{tech}' can implement these phase 2 concepts:
                {", ".join(concepts_p2)}

                Return ONLY the plain text search query. Do not add quotes, explanation, or markdown.
            """

            query_p2 = query_local_llm(q2_prompt, max_tokens = 32, temperature = 0.1).strip().replace('"', '').replace("'", "")

            results_p2 = web_search(query_p2)

            verify_p2_prompt = f"""
                You are a technical Allocator. Read this search context:
                {results_p2}

                Determine which of the following Phase 2 concepts can ACTUALLY be implemented by '{tech}' :
                Target Concepts : {", ".join(concepts_p2)}

                Return a raw JSON list of only the concepts from the target list that are compatible.
                Example format:
                ["HTTP/REST", "API Design"]
                Do not include markdown wraps(```) or explanation text. 
            """
            raw_res_p2 = query_local_llm(verify_p2_prompt, max_tokens = 128, temperature = 0.1)
            try:
                matched_p2 = json.loads(raw_res_p2.replace("```json", "").replace("```", "").strip())
            except Exception:
                matched_p2 = []
            concept_map [tech] = [matched_p1, matched_p2]

        # clean_qwen = qwen_res.replace("```json","").replace("```", "").strip()
        # concept_map = json.loads(clean_qwen)

        fin_data["mappings"] = concept_map
        ret_dict = dict()
        ret_dict["techstack"] = res
        ret_dict["map"] = json.dumps(fin_data, indent =4)
        # return res, json.dumps(fin_data, indent =4)
        return ret_dict

    except Exception as e:
        print(f"\n Error generating concept lifecycle mapping ; {e}")     
        err_dict = dict()
        err_dict["techstack"] = res
        err_dict["map"] = "{}"
        return err_dict   


        


    # return res



# get_inp()




