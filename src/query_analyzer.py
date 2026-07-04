import json
from google import genai

from dotenv import load_dotenv
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = gemini_key)

# details = home_get_inp() #this fucntions brings the details of goal, exp, time from the webpage in string format...

# details = {
#     "goal" : "I want to build an AI-powered resume analyzer that compares resumes with job descriptions and suggests improvements using LLMs.",
#     "exp" : "beginner",
#     "time" : "5"
# }



def get_inp():

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

User Project:
{goal}

Developer Experience:
{exp}

Available Development Time:
{time}

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
- Do not wrap the JSON inside ```.

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
- Strict Exclusion Rule: Do not repeat any technological dependency (e.g., specific languages or core frameworks like Python or Streamlit) in Phase 2 if they are already declared in Phase 1. Phase 2 lists only additions.
- Feature Alignment: If a feature is purely analytical or programmatic (e.g., prompt logic, structured LLM JSON outputs), it belongs in Phase 1. Do not push pure logic features to Phase 2 if they rely on Phase 1 tech. Phase 2 features should focus on infrastructure changes (e.g., adding user auth, cloud sync, data persistence).
- Dynamic Scaling Rule: Phase 1 must focus exclusively on in-memory, local execution. For an MVP, data should live inside application variables or transient session state. Do NOT include cloud databases, external database client libraries, or user authentication in Phase 1, as configuring them during week one creates boilerplate friction for a beginner. Move persistent cloud storage, database integrations (like Supabase/Firebase), and authentication strictly into Phase 2 as scalability and data-retention upgrades.

Technology Selection & Architectural Compatibility Rules:
- Every recommended technology must have an explicit purpose. Do not recommend tools that duplicate roles.
- ARCHITECTURAL LOCK-IN: Ensure Phase 1 and Phase 2 architectures are vertically compatible. Never recommend a Phase 1 framework that must be completely deleted or rewritten to implement Phase 2 (e.g., Do not recommend Flask in Phase 1 and Streamlit in Phase 2). Phase 2 must naturally extend Phase 1.
- INFRASTRUCTURE SANITY CHECK: Ensure your deployment target handles your database selection natively. If you use a cloud provider with an ephemeral file system (e.g., Render free tier, Heroku), do NOT pair it with a file-based database (e.g., SQLite) without explicitly addressing persistent disks, or swap the database to a serverless/cloud database API (e.g., Supabase, MongoDB Atlas) to prevent instant data loss.
- RUNTIME SANITY CHECK: Identify the chosen framework's core execution behavior. For frameworks that rerun scripts on state changes (e.g., Streamlit), you MUST introduce State Management concepts and local storage libraries directly into Phase 1 to prevent runtime bugs or duplicate API calls.
- PIPELINE PREREQUISITES: If an API library (e.g., google-genai) relies heavily on data schemas or local keys for its core feature to work cleanly, instantly include its dependent tools (e.g., Pydantic for structured JSON matching, python-dotenv for API keys) into Phase 1 alongside it.
- Deployment Streamlining: Match your deployment target strictly to your framework. If a framework provides a native, zero-configuration cloud hosting solution designed specifically for its platform (e.g., Streamlit Community Cloud), prioritize it over general containerization or multi-purpose hosts (e.g., Docker, Render) to minimize environment overhead for low-experience developers.

Return exactly in this format:
{op_format}
"""
    response = client.models.generate_content(
        # model="gemini-2.5-flash",
        # model = "gemini-2.0-flash",
        model="gemini-2.5-flash", # gemini-2.5-flash-lite or gemini-2.5-flash
        
        contents= prompt
        
    )

    print("Raw Gemini Output:")
    print(response.text)

get_inp()




