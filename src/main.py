from roadmap_builder import get_roadmap
from techstack_analyzer import get_techstack
import json



details = {
    "goal" : """
Business Idea:

I want to build an AI-powered GATE preparation platform called GateSter that acts as a
personal mentor for GATE aspirants. The application helps students learn concepts, revise
topics, practice previous year questions, take mock tests, and track their performance —
all through a single conversational AI interface. Instead of being a generic chatbot,
GateSter uses an internal tool routing system where specialized AI tools handle different
types of requests. Responses are grounded in real GATE material through a RAG pipeline
backed by Qdrant Cloud vector database. The MVP is designed to be modular so that
advanced features can be added later without major rewrites.

Target Users:

- GATE CS aspirants
- Engineering students preparing for GATE in any stream
- Working professionals attempting GATE alongside jobs
- College seniors guiding their juniors (future)

Workflow:

1. The user opens the application.

2. The landing page explains what GateSter is and invites the user to start chatting.

3. The user registers an account or logs in.

4. The user is taken to the main chat interface.

5. The user types a query — a concept doubt, a revision request, a PYQ, or a study plan.

6. The backend receives the query.

7. The Intent Detector classifies the query into one of five categories:
   - Concept
   - Revision
   - PYQ
   - Strategy
   - Teaching

8. The Tool Router selects the appropriate tool based on the detected intent.

9. If multiple tools are needed, they execute sequentially and their outputs are merged.

10. The selected tool sends a semantic search query to Qdrant Cloud.

11. Qdrant retrieves the most relevant GATE material chunks from the matching
    subject collection.
    - Collections include: OS, DBMS, CN, TOC, Compiler Design, DSA,
      Algorithms, COA, Digital Logic, Engineering Mathematics, Aptitude,
      Formula Sheets, Previous Year Questions.

12. Retrieved chunks are reranked and the top chunks are selected.

13. A structured prompt is assembled containing:
    - Tool-specific system prompt
    - Top retrieved chunks from Qdrant
    - Conversation summary
    - Last N messages
    - Current user query

14. The prompt is sent to Gemini API.

15. Gemini generates a response grounded in the retrieved GATE material.

16. The response is returned to the frontend and displayed in the chat interface.

17. The chat message pair (user + assistant) is stored in PostgreSQL.

18. Older chat history is periodically summarized and stored as compact memory
    to reduce future prompt size.

19. The user can navigate to the Mock Test section.

20. The user selects a test type:
    - Subject-wise test
    - Multi-subject test
    - Full-length mock test

21. The Mock Test Engine generates questions from the question bank stored in PostgreSQL.

22. The user takes the test in a timed interface with:
    - Countdown timer
    - Question navigation panel
    - Flag for review option
    - Auto-submission when timer expires

23. On submission, the Python backend scores the test programmatically.
    - No LLM is used for scoring.
    - Scores, accuracy, subject-wise breakdown, and topic-wise breakdown are computed.

24. Results are stored in PostgreSQL and displayed to the user.

25. The user can ask GateSter to explain their performance in natural language.
    - The AI reads the computed result data and responds like a mentor.
    - It does not recalculate anything.

26. A News Panel inside the chat interface displays real-time GATE updates:
    - Official GATE notifications
    - IIT announcements
    - Admit card alerts
    - Answer key releases
    - Result notifications
    - Syllabus changes

27. Weak topics are inferred from chat history by tracking which topics the user
    asks about most frequently.

Future Roadmap:

Phase 2

28. Weak topic detection is enhanced by combining mock test scores with chat history.

29. Personalized revision plans are generated based on weak topic data.

30. Adaptive mock tests increase difficulty on strong topics and focus on weak ones.

31. A daily study planner generates AI-driven targets each morning.

32. Flashcard generation from subject notes.

33. Spaced repetition system for formula and concept retention.

34. Voice conversations with GateSter.

35. Image-based doubt solving — the user uploads a photo of a handwritten problem.

36. PDF interaction — the user uploads any document and asks questions about it.

37. Community discussion forum with AI-assisted answers.

38. Gamification system with streaks, XP, levels, badges, and leaderboards.

39. Detailed progress reports covering performance trends, subject mastery,
    mock comparison, and revision history.

40. Admin dashboard for content upload and knowledge base management.

41. Mobile application for iOS and Android.

42. Multi-language support.

43. Support for multiple LLM providers including OpenAI, Claude, and Gemini.

44. Cloud deployment with auto-scaling for high traffic periods around GATE season.

Business Goals:

- Build a focused, functional MVP for GATE CS aspirants.
- Make the AI feel like a real mentor, not a generic chatbot.
- Keep token usage minimal through intelligent routing and context compression.
- Design the system so that Phase 2 features can be added without rewriting the core.
- Eventually grow GateSter into a full AI-powered EdTech SaaS platform for GATE.

""",
    "exp" : "beginner",
    "time" : "10"
}

raw_roadmap_string = get_roadmap(details)

roadmap = json.loads(raw_roadmap_string)

#keys are to be extracted and i am thinking to keep the response in an indented string 

rdmap_keys = ["project_name", "design_philosophy","phases"]
# if (i == "phases"):
phas_keys = ["phase_number", "description", "modules"]
# if (j == "modules"):
mod_keys = ["name", "description", "phase", "type", "critical", "complexity", "responsibilities"]

identd_str = ""

# print(identd_str)

for i in rdmap_keys : 
    
    if (i == "phases") :
        phases = roadmap["phases"]
        identd_str = identd_str + i + ":" + "\n"
        for j in range(0, len(phases)):
            for k in phas_keys:
                
                if (k == "modules") : 
                    modules = phases[j]["modules"]
                    identd_str = identd_str + k + ":" + "\n"
                    for l in range (0, len(modules)):
                        
                        for m in mod_keys:
                            value = modules[l].get(m, "N/A")
                            if (isinstance (value, list)):
                                identd_str = identd_str + "\t\t" + m + ":" + "\n"
                                for item in value : 
                                    identd_str = identd_str + "\t\t\t -" + str(item) + "\n" 
                            else :
                                identd_str = identd_str + "\t\t" + m + ":" + str(value) + "\n" + "\n"
                else :

                    value = str(phases[j].get(k, "N/A")) 
                    identd_str = identd_str + "\t" + k + ":" + value + "\n"

    else : 
        value = str(roadmap.get(i, "N/A"))
        identd_str = identd_str + i + " : " + value + "\n"


ind_roadmap = identd_str

# ind_roadmap = """
# project_name : AI-Powered Resume Analyzer
# design_philosophy : This architecture is designed for progressive enhancement, starting with a beginner-friendly MVP that prioritizes simplicity and directness of workflow. It employs a modular, technology-agnostic approach to ensure that future features can be introduced through extension and composition, minimizing refactoring of core components. The unified data contract establishes a stable, canonical model from Phase 1, enabling seamless data flow across all architectural layers and future evolutionary stages. Cohesion within modules and loose coupling between them are paramount, facilitating independent development and maintenance.
# phases:
#         phase_number:1
#         description:Establish a functional Minimum Viable Product (MVP) that allows job seekers to analyze their resumes against job descriptions, receive AI-powered feedback, and download reports. This phase prioritizes simplicity, direct synchronous workflows, and avoids persistent storage for core analysis data, focusing on session-based interactions.
# modules:
#                 name:User Interface Module
#                 description:Manages the web-based user interface, accepting inputs and displaying analysis results.
#                 phase:1
#                 type:Presentation Layer
#                 critical:True
#                 complexity:Medium
#                 responsibilities:['Render application pages and forms', 'Handle user inputs for resume and job description uploads/pastes', 'Display structured analysis results', 'Initiate report downloads', 'Allow copying of individual suggestions']
#                 name:Document Ingestion Module
#                 description:Receives user-provided resume and job description inputs, validating their format and basic properties.
#                 phase:1
#                 type:Processing Layer
#                 critical:True
#                 complexity:Low
#                 responsibilities:['Accept resume files (PDF/DOCX)', 'Accept job description text or files', 'Validate uploaded file types', 'Validate uploaded file sizes', 'Reject unsupported or invalid files']
#                 name:Content Processing Module
#                 description:Extracts text from documents and performs cleaning and normalization on both resume and job description text.
#                 phase:1
#                 type:Processing Layer
#                 critical:True
#                 complexity:Medium
#                 responsibilities:['Extract text content from PDF and DOCX resume files', 'Extract text content from job description files (if uploaded)', 'Remove unnecessary whitespace from extracted text', 'Remove formatting artifacts and control characters', 'Normalize text for consistent processing (e.g., lowercase, stemming if needed)']
#                 name:Analysis Orchestration Module
#                 description:Coordinates the entire analysis workflow, from prompt construction to LLM interaction, response validation, and structuring of the final results.
#                 phase:1
#                 type:Business Logic Layer
#                 critical:True
#                 complexity:Medium
#                 responsibilities:['Construct a structured prompt for the LLM using resume text, job description, and analysis instructions', 'Initiate communication with the AI Integration Module to send the prompt', 'Receive and validate the raw response from the LLM', "Parse the LLM's raw response into a structured format", 'Structure the final analysis results into categories (match score, skills, ATS, etc.)', 'Update analysis status throughout the workflow', 'Delegate storage of analysis data to Session Management Module']
#                 name:AI Integration Module
#                 description:Handles communication with the underlying Large Language Model provider to perform the resume analysis.
#                 phase:1
#                 type:Integration Layer
#                 critical:True
#                 complexity:Low
#                 responsibilities:['Send structured prompts to the LLM', 'Receive raw responses from the LLM', 'Handle basic LLM communication protocols']
#                 name:Report Generation Module
#                 description:Creates a downloadable PDF report based on the structured analysis results.
#                 phase:1
#                 type:Processing Layer
#                 critical:True
#                 complexity:Medium
#                 responsibilities:['Format structured analysis data into a report layout', 'Generate a PDF file containing the complete analysis']
#                 name:Session Management Module
#                 description:Manages temporary, in-memory storage of analysis data for an unauthenticated user's session.
#                 phase:1
#                 type:System Layer
#                 critical:True
#                 complexity:Low
#                 responsibilities:['Generate unique session identifiers', 'Store analysis results and associated data temporarily for a session', 'Retrieve session data upon request', 'Clear session data upon explicit request or session expiration']
#         phase_number:2
#         description:Extend the MVP to a full-fledged SaaS platform by introducing user accounts, persistent storage for resumes and analyses, advanced comparison features, additional AI capabilities, and recruiter-specific workflows. This phase focuses on building new modules that compose around and enhance Phase 1's core functionality without requiring significant rewrites.
# modules:
#                 name:Identity and Authentication Module
#                 description:Manages user registration, login, and secure authentication, ensuring authorized access to user-specific data.
#                 phase:2
#                 type:Security Layer
#                 critical:False
#                 complexity:Medium
#                 responsibilities:['Register new user accounts', 'Authenticate existing users (login)', 'Manage user sessions and tokens securely', 'Handle password hashing and verification']
#                 name:User Profile Module
#                 description:Manages user-specific preferences and profile details for registered users.
#                 phase:2
#                 type:Business Logic Layer
#                 critical:False
#                 complexity:Low
#                 responsibilities:['Store and retrieve user profile information', 'Manage user notification preferences', 'Manage user language preferences']
#                 name:Persistent Storage Module
#                 description:Provides durable storage and retrieval services for all application data, including user accounts, resumes, job descriptions, and analyses.
#                 phase:2
#                 type:Persistence Layer
#                 critical:False
#                 complexity:Medium
#                 responsibilities:['Store new data records', 'Retrieve existing data records by identifier or query', 'Update existing data records', 'Delete data records', 'Manage data integrity and consistency']
#                 name:Analysis History Module
#                 description:Enables authenticated users to save, view, and manage their past resume analyses and uploaded documents.
#                 phase:2
#                 type:Business Logic Layer
#                 critical:False
#                 complexity:Medium
#                 responsibilities:['Associate analyses and uploaded documents with a specific user account', 'Save resume files and job descriptions for future use', 'Save completed analysis reports persistently', "Retrieve a user's complete history of analyses", 'Allow viewing of individual past analysis reports']
#                 name:Comparison Engine Module
#                 description:Provides tools for comparing multiple resumes against a single job description, or one resume against multiple job descriptions, and tracking improvement over time.
#                 phase:2
#                 type:Business Logic Layer
#                 critical:False
#                 complexity:Medium
#                 responsibilities:['Retrieve multiple `analysisResultStructured` objects for comparison', 'Compute and present comparison metrics between resumes/job descriptions', 'Track and visualize resume improvement trends over time', 'Generate side-by-side comparison views']
#                 name:Advanced AI Capabilities Module
#                 description:Expands AI functionality beyond basic resume analysis to include features like AI-generated interview questions and personalized learning recommendations.
#                 phase:2
#                 type:AI Layer
#                 critical:False
#                 complexity:Medium
#                 responsibilities:['Generate relevant interview questions based on job description content', 'Provide learning resource recommendations for identified missing skills', 'Integrate with external learning platforms (conceptual)']
#                 name:Recruiter Workflow Module
#                 description:Provides specialized features for recruiters to manage multiple candidates, including bulk resume uploads and automated ranking.
#                 phase:2
#                 type:Business Logic Layer
#                 critical:False
#                 complexity:Medium
#                 responsibilities:['Allow recruiters to upload multiple resumes simultaneously', 'Process multiple resumes against a single job description', 'Generate automatic candidate rankings based on match scores and other criteria', 'Provide bulk analysis reports for recruitment pipelines']
#                 name:Analytics and Reporting Module
#                 description:Collects, aggregates, and visualizes application usage statistics and key performance indicators for administrators.
#                 phase:2
#                 type:Analytics Layer
#                 critical:False
#                 complexity:Medium
#                 responsibilities:['Track key application events (e.g., resume uploads, analyses run, reports generated)', 'Aggregate usage data and statistics', 'Provide an admin dashboard for viewing application metrics', 'Generate periodic operational reports']
#                 name:Notification Module
#                 description:Sends automated notifications to users, such as analysis completion emails, based on user preferences.
#                 phase:2
#                 type:Notification Layer
#                 critical:False
#                 complexity:Low
#                 responsibilities:['Dispatch email notifications', 'Integrate with notification service providers (conceptual)', 'Adhere to user notification preferences']
#                 name:Internationalization Module
#                 description:Manages multilingual support for the application's user interface and potentially localized content.
#                 phase:2
#                 type:System Layer
#                 critical:False
#                 complexity:Medium
#                 responsibilities:['Store and retrieve application text translations', "Apply user's preferred language to the UI", 'Provide language selection mechanisms']
#                 name:LLM Orchestration Module
#                 description:Provides an abstraction layer to support integration with multiple Large Language Model providers, allowing dynamic selection and unified interaction.
#                 phase:2
#                 type:Integration Layer
#                 critical:False
#                 complexity:Medium
#                 responsibilities:['Manage configuration for multiple LLM providers', 'Select the appropriate LLM based on criteria (e.g., cost, performance, features)', "Route `llmPrompt` to the chosen LLM provider's API", 'Normalize responses from different LLM providers into a consistent format']

# """


tech_stack = get_techstack(details, ind_roadmap)
print(tech_stack)


    