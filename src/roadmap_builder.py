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
    "goal" : """
    Business Idea:

I want to build an AI-powered Resume Analyzer that helps job seekers improve their resumes according to specific job descriptions. The application should analyze the resume, identify missing skills, provide ATS optimization suggestions, and recommend improvements using Large Language Models. Initially, the application should be beginner-friendly to build, but it should also be designed so that additional features can be added later without major rewrites.

Target Users:

- Students
- Freshers
- Working professionals
- Recruiters (future)

Workflow:

1. The user opens the application.

2. The home page explains what the application does and provides options to upload a resume and enter a job description.

3. The user uploads a resume in PDF or DOCX format.

4. The application validates the uploaded file.
   - Check file type.
   - Check file size.
   - Reject unsupported files.

5. The application extracts text from the uploaded resume.

6. The extracted text is cleaned.
   - Remove unnecessary spaces.
   - Remove formatting artifacts.
   - Normalize text.

7. The user pastes a job description or uploads it as a document.

8. The job description is cleaned and preprocessed.

9. The application creates a structured prompt containing:
   - Resume text
   - Job description
   - Analysis instructions

10. The prompt is sent to an LLM.

11. The LLM analyzes:
    - Skill matching
    - Missing keywords
    - ATS compatibility
    - Resume strengths
    - Resume weaknesses
    - Grammar and wording
    - Formatting suggestions

12. The application receives the structured response.

13. The response is validated.

14. The results are displayed in multiple sections:
    - Overall Match Score
    - Missing Skills
    - Existing Skills
    - ATS Suggestions
    - Resume Improvements
    - Final Summary

15. The user can copy individual suggestions.

16. The user can download the complete analysis as a PDF.

17. The application stores the current analysis temporarily during the session.

18. If the user refreshes the page, the temporary session is cleared.

Future Roadmap:

Phase 2

19. Users create an account.

20. Users log in securely.

21. Every uploaded resume is saved.

22. Previous analyses can be viewed.

23. Users can compare multiple resumes against the same job description.

24. Users can compare one resume against multiple job descriptions.

25. Users can track resume improvement over time.

26. Users receive AI-generated interview questions based on the job description.

27. Users receive learning recommendations for missing skills.

28. Recruiters can upload multiple resumes and rank candidates automatically.

29. Admin dashboard displays application statistics.

30. Email notifications inform users when analyses are completed.

31. Users can export reports in multiple formats.

32. The system can support multiple LLM providers.

33. The application can support multiple languages.

34. Organizations can use the platform for campus recruitment.

Business Goals:

- First build a functional MVP.
- Make it useful for students and job seekers.
- Keep development beginner-friendly.
- Ensure that Phase 2 can be implemented without rewriting the entire application.
- Eventually grow the application into a SaaS platform.


""",
    "exp" : "beginner",
    "time" : "5"
}



def get_roadmap(details):

    # goal = input ("HOW MAY WE HELP YOU??? : ")
    goal = details["goal"]
    # exp = input("what is your experience??? : ")
    exp = details["exp"]
    # time = input("how much time??? : ")
    time = details ["time"]
    

    try : 
        time_limit = int(time)
    except ValueError:
        time_limit = 4
    
    
    module_template = """{
                    "module_id": "...",
                    "name": "...",
                    "description": "...",
                    "phase": 1,
                    "priority": 1,
                    "type": "...",
                    "critical": true,
                    "complexity": "...",
                    "depends_on": [],
                    "interfaces": {
                        "consumes": [],
                        "produces": []
                    },
                    "responsibilities": [],
                    "inputs": [],
                    "outputs": [],
                    "state": {
                        "owner": "...",
                        "lifetime": "...",
                        "location": "...",
                        "persistence": "..."
                    },
                    "capabilities": []
                }"""
    if time_limit < 4:
        phase_structure = f"""
        [
            {{
                "phase_number": 1,
                "description": "...",
                "modules":  [{module_template}]
            }}
        ]
        """
    else :
        module_template_p2 = module_template.replace('"phase": 1', '"phase": 2').replace('"critical": true', '"critical": false')
        phase_structure = f"""[

            {{
                "phase_number": 1,
                "description": "...",
                "modules": [{module_template}]
            }},
            {{
                "phase_number": 2,
                "description": "...",
                "modules": [{module_template_p2}]
            }}
        ]
            
        """

    output_format = f"""{{
        
        "project_name": "...",
        "architecture_version": "...",
        "design_philosophy": "...",
        "phases": {phase_structure},
        "unified_data_contract": {{
            "name": "...",
            "description": "...",
            "fields": [
            {{
                "name": "...",
                "type": "...",
                "description": "...",
                "required": true,
                "nullable": false,
                "example": "..."
            }}
            ]

        }}
    }}
        """
    prompt = f"""

You are an expert Principal Software Architect, Systems Design Engineer, and Technical Consultant.

A user has provided a Business Idea, Product Vision, Functional Workflow, and Future Roadmap.

Your task is to derive a complete, technology-agnostic Architectural Blueprint and Unified Data Contract from the provided requirements.

Your objective is NOT to recommend programming languages, frameworks, databases, cloud providers, APIs, libraries, or implementation technologies.

Your objective is to design a software architecture that another software architect could directly use to select technologies, implementation strategies, deployment models, and engineering practices.

Infer only those architectural details that are necessary to produce a complete and internally consistent architecture.

Do not invent functionality that is not reasonably implied by the requirements.

--------------------------------------------------
USER REQUIREMENTS
--------------------------------------------------

{goal}

--------------------------------------------------
DEVELOPER EXPERIENCE LEVEL: {exp}
--------------------------------------------------

--------------------------------------------------
ARCHITECTURAL DESIGN RULES BY EXPERIENCE
--------------------------------------------------

• If the developer is a Beginner:
  - Keep the module design highly consolidated (fewer modules overall).
  - Prefer simple, synchronous workflow designs over asynchronous or multi-threaded setups.
  - Keep module complexity ratings primarily at 'Low' or 'Medium'.
  - Avoid complex enterprise design patterns (like event sourcing, microservices, or complex background queues).
• If the developer is Intermediate:
  - Design a standard layered modular architecture (Presentation, Business Logic, Processing, Integration, Persistence).
  - Use standard, clean separation of concerns.
• If the developer is Advanced:
  - Design production-grade, highly decoupled architectures.
  - Include modules dedicated to telemetry, structured logging, background task queues, and caching strategies.

--------------------------------------------------
ARCHITECTURAL OBJECTIVES
--------------------------------------------------

Design an architecture that satisfies the following principles:

• Phase 1 should produce a complete MVP.
• Phase 1 should minimize infrastructure complexity.
• Phase 1 should avoid persistent storage whenever it is not functionally required.
• Phase 2 should introduce additional capabilities by composing new modules around existing ones rather than replacing or restructuring Phase 1 modules.
• Every module should represent a cohesive architectural component with a single primary responsibility.
• The architecture should maximize cohesion within modules and minimize coupling between modules.
• Modules should communicate exclusively through well-defined interfaces and explicit data contracts.
• Data structures produced in Phase 1 should remain valid throughout all future phases.
• The architecture should support future evolution through extension rather than modification.
• The architecture should be scalable, maintainable, reusable, and internally consistent.

--------------------------------------------------
DESIGN RESPONSIBILITIES
--------------------------------------------------

For every architectural module:

• Define its purpose.
• Define the responsibilities owned exclusively by that module.
• Define the architectural interfaces through which it communicates.
• Define the data it consumes.
• Define the data it produces.
• Define how long that data exists.
• Define where that data logically resides.
• Define whether the module is critical for the MVP.
• Define how the module interacts with other modules.

When Phase 2 introduces new capabilities, those capabilities must integrate with the existing architecture rather than replacing or restructuring existing modules.

--------------------------------------------------
ARCHITECTURAL GUIDELINES
--------------------------------------------------

Focus on architectural responsibilities, component boundaries, interfaces, state management, and data flow rather than implementation details or technology choices.

Do NOT recommend:

• Programming Languages
• Frameworks
• Libraries
• Databases
• Cloud Platforms
• Deployment Providers
• Authentication Providers
• AI Providers
• Vendor-specific products

Instead describe architectural roles such as:

• Presentation Layer
• Business Logic Layer
• Processing Layer
• Integration Layer
• Persistence Layer
• Notification Layer
• Authentication Layer
• Scheduling Layer
• Analytics Layer

Model architectural intent rather than implementation mechanics.

Use functional capabilities instead of technologies.

Example:

GOOD

Document Parsing

Prompt Construction

Structured AI Processing

Persistent Storage

Identity Management

Notification Delivery

BAD

PyPDF

FastAPI

Supabase

Next.js

OpenAI


--------------------------------------------------
MODULE DESIGN REQUIREMENTS
--------------------------------------------------

{module_template}

Definitions:

• Critical indicates whether the module is required for a functional MVP.

• Priority represents the recommended implementation order within its phase.

• Complexity refers to implementation effort and architectural sophistication rather than computational complexity.

• Dependencies represent logical execution or communication dependencies between architectural components, never implementation dependencies.

• Capabilities describe reusable architectural capabilities provided by the module, independent of any implementation technology.

• Interfaces describe the explicit communication contract between architectural modules.

Prefer fewer, well-defined architectural components over many narrowly scoped components unless additional decomposition is clearly justified by the project requirements.

--------------------------------------------------
ARCHITECTURAL VALIDATION
--------------------------------------------------

Before producing the final JSON, verify that:

• Every module belongs to exactly one phase.
• Every dependency references an existing module.
• Every consumed input is produced by another module or originates from the user.
• Every output is consumed by another module or represents a final application output.
• No duplicate responsibilities exist across modules.
• Every module has a clearly defined architectural boundary.
• Every module communicates only through declared interfaces.
• The unified data contract is sufficient for communication between every module.
• The architecture is internally consistent.
• The final JSON payload has zero duplicate keys and completely valid, parseable JSON syntax.


--------------------------------------------------
UNIFIED DATA CONTRACT
--------------------------------------------------

Design one unified application data contract.

The unified data contract must:

• Be produced during Phase 1.
• Remain unchanged throughout later phases.
• Serve as the communication contract between all architectural modules.
• Be directly suitable for persistent storage.
• Avoid translation layers between architectural phases.
• Represent the canonical application model rather than a database schema.

Do NOT include implementation-specific storage details such as database identifiers, storage paths, or persistence metadata unless they are part of the application's domain model.

For every field specify:

• name
• type
• description
• required
• nullable
• example

Use consistent naming conventions:

• Module identifiers → snake_case
• Human-readable names → Title Case
• Data contract fields → camelCase

--------------------------------------------------
OUTPUT REQUIREMENTS
--------------------------------------------------

Assume this document will serve as the canonical architectural specification for all subsequent planning stages, including:

• Technology Selection
• Concept Identification
• Database Design
• Folder Structure Generation
• API Planning
• Testing Strategy
• Deployment Planning
• Infrastructure Planning
• Code Generation

Return ONLY one valid JSON object.

Do NOT use Markdown.

Do NOT explain your reasoning.

Do NOT output any text outside the JSON.

Do NOT wrap the JSON inside triple backticks.

Do NOT output ```json or ```.

The first character of your response MUST be {{

The last character of your response MUST be }}

Your entire response must be a single valid JSON object.

JSON QUALITY & CONCISENESS RULES:
• Keep descriptions for all modules and fields concise to prevent truncation or generation drift.
• Ensure every key in the JSON is unique; do NOT duplicate, merge, or repeat keys (like 'userRole' or 'userName').
• Do NOT repeat the field definitions inside 'unified_data_contract.fields'. Every field must be declared exactly once.

The JSON MUST contain:

{output_format}

"""
    response = client.models.generate_content(
        # model="gemini-2.5-flash",
        # model = "gemini-2.0-flash",
        model="gemini-2.5-flash-lite", # gemini-2.5-flash-lite or gemini-2.5-flash
        
        contents= prompt
        
    )

    # print("Raw Gemini Output:")
    # print(response.text)

    
    res = response.text

    res = res.strip()

    if res.startswith("```json"):
        res = res [7:]
    elif res.startswith("```"):
        res = res[3:]
    if res.endswith("```"):
        res = res [:-3]

    res = res.strip()

    return res

    # try :
    #     blueprint_dict = json.loads(res)
    #     print("successfully converted json to dict")
    #     print(blueprint_dict["project_name"])
    #     print(blueprint_dict.keys())
    # except json.JSONDecodeError as e:
    #     print(f"Failed to parse JSON : {e}")




