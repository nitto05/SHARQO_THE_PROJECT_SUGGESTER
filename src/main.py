from roadmap_builder import get_roadmap



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

roadmap = get_roadmap(details)

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
                identd_str = identd_str + "\t" + phases[j][k] + "\n"
                if (k == "modules") : 
                    modules = phases["modules"]
                    identd_str + identd_str + k + ":"
                
    else : 
        identd_str = identd_str + i + " : " + roadmap[i] + "\n"
    # identd_str = identd_str + "\n"
    
    