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

details = {
    "goal" : "I want to build an AI-powered resume analyzer that compares resumes with job descriptions and suggests improvements using LLMs.",
    "exp" : "beginner",
    "time" : "5"
}



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

Examples:
- Healthcare
- Football
- Finance
- Education
- Cybersecurity
- Agriculture
- E-Commerce

4. APIs / External Services

Infer useful APIs or external services.

Examples:
- Football Data API
- OpenWeather API
- Stripe
- Google Maps
- Firebase
- Twilio

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
- Prioritize simplicity.
- Recommend beginner-friendly technologies.
- Minimize setup complexity.
- Prefer free and open-source tools whenever possible.
- Focus on helping the user successfully complete the project.
- Avoid enterprise technologies unless absolutely necessary.

If the developer is Intermediate:
- Recommend industry-standard technologies.
- Introduce professional development practices.
- Balance simplicity and scalability.
- Recommend tools commonly used in software companies.
- Assume the user is comfortable learning moderately advanced concepts.

If the developer is Advanced:
- Recommend the most suitable architecture for the project.
- Optimize for scalability, maintainability, and performance.
- Recommend production-grade technologies when appropriate.
- Do not simplify recommendations unnecessarily.

Time Rules:

The available development time determines the scope of the project.

- Short durations should focus on an MVP.
- Medium durations should introduce additional features and cleaner architecture.
- Long durations should recommend scalable designs, advanced features, and production-ready practices.

Selection Rules:

- Think like an experienced Software Architect mentoring the given developer.
- Recommend only technologies that are appropriate for BOTH the user's experience level AND available development time.
- Do NOT list every possible technology.
- Choose one preferred technology whenever multiple alternatives exist.
- Order every list from highest priority to lowest priority.
- Focus on helping the user build the project successfully rather than maximizing completeness.

Phase Rules:

- Phase 1 should contain everything required to build the first complete working version (MVP) of the project.

- Phase 2 should contain ONLY the additional technologies, concepts, APIs, and features that should be introduced after Phase 1 is completed.

- Do NOT repeat anything already listed in Phase 1.

- Every item in Phase 2 must represent a genuine upgrade, enhancement, or scalability improvement over Phase 1.

- Assume Phase 1 has already been implemented successfully.

- Phase 2 should focus on improving scalability, maintainability, usability, security, or adding advanced features.

Technology Selection Rules

- Every recommended technology must have a clear purpose in the project.

- Do not recommend technologies that only improve developer experience.

- Do not recommend technologies that duplicate the role of another recommended technology.

- Do not recommend technologies that would require rewriting the project architecture.

- Prefer technologies that naturally extend the previous phase.

- Before recommending a technology, ask:
    "Is this actually necessary for this project at this stage?"

If the answer is no, do not include it.

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




