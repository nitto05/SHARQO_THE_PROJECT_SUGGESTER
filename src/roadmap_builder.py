from pydantic import config
import json
from google import genai
from google.genai import types

from dotenv import load_dotenv
import os
import sys
from pathlib import Path
from api_helper import safe_generate_json

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = gemini_key)

# details = home_get_inp() #this fucntions brings the details of goal, exp, time from the webpage in string format...





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
• CRITICAL : GENERATE the JSON in MINIFIED format (no indented, no newlines, no extra spaces) to avoid hitting output token limits.
• Keep descriptions for all modules, fields, and unified data contract fields strictly UNDER 12 words.

• Ensure every key in the JSON is unique; do NOT duplicate, merge, or repeat keys (like 'userRole' or 'userName').
• Do NOT repeat the field definitions inside 'unified_data_contract.fields'. Every field must be declared exactly once.

The JSON MUST contain:

{output_format}

"""

    config = types.GenerateContentConfig(
        max_output_tokens=65536,
        response_mime_type = "application/json"
    )

    response = safe_generate_json(client, "gemini-2.5-flash", prompt, config)
    
    res = response.text

    # start_idx = res.find('{')
    # end_idx = res.rfind('}')
    
    # if start_idx != -1 and end_idx != -1:
    #     res = res[start_idx : end_idx + 1]

    return res.strip()

    # try :
    #     blueprint_dict = json.loads(res)
    #     print("successfully converted json to dict")
    #     print(blueprint_dict["project_name"])
    #     print(blueprint_dict.keys())
    # except json.JSONDecodeError as e:
    #     print(f"Failed to parse JSON : {e}")




