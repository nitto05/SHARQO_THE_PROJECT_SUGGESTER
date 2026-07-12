from roadmap_builder import get_roadmap
from techstack_analyzer import get_techstack
import json



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


    