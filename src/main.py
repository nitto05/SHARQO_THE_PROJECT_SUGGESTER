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

# print(raw_roadmap_string[61900:62200])  # shows the broken area
print("LENGTH:", len(raw_roadmap_string))
print(raw_roadmap_string[1950:2350])
print(raw_roadmap_string[-300:])
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




tech_stack = get_techstack(details, ind_roadmap)
print(tech_stack)

