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

def get_inp():

    goal = input ("HOW MAY WE HELP YOU??? : ")

    exp = input("what is your experience??? : ")

    time = input("how much time??? : ")
    
    output_format = """{
    "techstack" : [],
    "concepts" : [],
    "domain" : [],
    "apis" : [],
    "optional_features" : []
    }"""

    prompt = f"""
You are an expert Soft Architect and Technical Mentor.

A user has described a software project.

Your task is NOT to recommend learning resources.

Your task is to analyze the project idea and infer everything that a developer would need to build it.

User Project:

{goal}

Analyze the project and identify : 

1. Tech Stack
- Programming languages
- Frameworks
- Libraries
- Databases
- Cloud services
- Deployement technologies
- DevOps tools

2. Core Concepts
- Computer Science concepts
- AI/ML cocnepts
- Software concepts
- Networking concepts
- Database Concepts
- Mathematical concepts 
- any other important technical concepts

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
Suggest useful advanced features that could improve the project.

Rules : 

- Infer missing requirements logically.
- Include all important technologies.
- Do not include explanations.
- Remove duplicates.
- Use concise names.
- Return only valid JSON.
- Do not use Markdown.
- Do not wrap the JSON inside ```.

Return exactly in this format:

{output_format}


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




