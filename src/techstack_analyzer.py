import requests 
from bs4 import BeautifulSoup


import json
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import sys
from pathlib import Path

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



def scrape_page(url: str) -> str:
    """
    Scrapes a webpage and returns its plain text content.
    """

    try:
        response = requests.get(url, timeout = 10)
        soup = BeautifulSoup (response.text, "html.parser")
        raw_text = soup.get_text(separator = "", strip = True)[:3000]
    # except Exception as e :
    #     return f"[Error scraping {url} : {str(e)}]"
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

        filter_response = client.models.generate_content(
            model = "gemini-2.5-flash-lite",
            contents = filter_prompt
        )
        return filter_response.text
    except Exception as e:
        return f"[Error scraping {url} : {str(e)}]"


def get_techstack(details, ind_roadmap):

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
    response = client.models.generate_content(
        # model="gemini-2.5-flash",
        # model = "gemini-2.0-flash",
        model="gemini-2.5-flash", # gemini-2.5-flash-lite or gemini-2.5-flash
        
        contents= prompt,

        config = types.GenerateContentConfig(tools = [web_search, scrape_page])
        
    )

    res = response.text

    # res = response.text
    print("RAW RESPONSE:", res)  # add this to see what came back
    print("CANDIDATES:", response.candidates)  # shows tool call vs text


    if res is None:
        print("Gemini returned None — likely made tool calls without final text")
        print("Full response:", response)
        return "{}"  # return empty JSON safely

    res = res.strip()

    if res.startswith("```json"):
        res = res [7:]
    elif res.startswith("```"):
        res = res[3:]
    if res.endswith("```"):
        res = res [:-3]

    res = res.strip()

    return res



# get_inp()




