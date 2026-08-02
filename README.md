<p align="center">
  <img src="assets/SHARQO.png" alt="SHARQO Logo" width="400" />
</p>

<h1 align="center">SHARQO</h1>

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-MVP%20COMPLETED-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-LOCAL%20QWEN%204B-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-GEMINI%20API-blue?style=for-the-badge&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/VECTOR%20DB-QDRANT-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/BACKEND-FASTAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
</p>

> SHARQO is an AI assistant that helps users plan their software projects by generating personalized roadmaps, recommending the required technologies, and providing curated learning resources to turn ideas into reality.

---

## Overview

SHARQO begins with three simple inputs:

- **Project Idea**
- **User Experience** *(Beginner, Intermediate, Advanced)*
- **Target Completion Time**

Using these inputs, SHARQO generates a personalized **project roadmap** that outlines the major milestones required to complete the project.

Based on the generated roadmap, SHARQO identifies the required **technology stack**, **programming languages**, **frameworks**, **libraries**, **APIs**, **core concepts**, **domain knowledge**, and **potential features**.

To ensure users can confidently build their projects, SHARQO searches multiple trusted platforms and gathers relevant learning resources, organizing them into a structured format so users know exactly **what to learn, when to learn it, and where to learn it**.

---

## Problem Statement

Many aspiring developers, students, and first-time founders have innovative project ideas but hesitate to pursue them because they are unsure whether their ideas are feasible.

Even when an idea is viable, they often struggle with questions such as:

- What technologies do I need?
- Where should I start?
- Which concepts should I learn first?
- Which APIs or frameworks are appropriate?
- How do all these pieces fit together?

To overcome these uncertainties, many turn to general-purpose AI chatbots.

While these tools can provide useful information, their responses are often long, unstructured, and overwhelming. Users receive large amounts of disconnected suggestions without a clear learning path or implementation strategy.

For someone who is already uncertain about their abilities, this information overload often leads to frustration, causing many promising ideas to be abandoned before development even begins.

---

## Vision

SHARQO is designed to become an intelligent project mentor rather than just another AI chatbot.

Instead of immediately recommending technologies or tutorials, SHARQO first helps users understand the journey ahead by generating a structured roadmap tailored to their experience level and project goals.

Once the roadmap is established, SHARQO identifies the appropriate technologies, programming languages, frameworks, APIs, concepts, and optional features required to build the project successfully.

However, knowing **what** to use is only part of the journey.

To empower users with complete control over their projects, SHARQO also discovers and organizes high-quality learning resources for every recommended technology and concept. This enables users not only to build the proposed solution but also to expand upon it with their own creativity and ideas.

The journey doesn't end once development begins.

As users build their projects, SHARQO aims to assist them by identifying implementation issues, suggesting code improvements, explaining difficult concepts, and recommending architectural changes whenever necessary. If project requirements evolve, SHARQO can even revise the roadmap to reflect the new direction.

Ultimately, SHARQO strives to become a long-term development companion that transforms uncertainty into confidence.

Its mission is simple:

> **No great startup or innovative idea should fail simply because its creator didn't know where to start or what to learn next.**

---

# Workflow

```text
Project Idea
     │
     ▼
Roadmap Builder (Gemini / Caching)
     │
     ▼
Determine Learning Objectives
     │
     ▼
Query Analyzer & TechStack Analyzer (Local Qwen / Phase-Targeted Loops)
     │
     ├── Tech Stack
     ├── Libraries
     ├── APIs
     ├── Concepts
     ├── Domain Knowledge
     └── Optional Features
     │
     ▼
Material Fetcher (Parallel ThreadPool API Workers)
     │
     ├── YouTube Data API
     ├── GitHub Search API
     ├── Google Books API
     └── arXiv Catalog API
     │
     ▼
Final Curriculum & Learning Roadmap (Gemini Cloud)
     │
     ▼
Learn & Build
```

---

# Completed MVP Architecture

## 1. Roadmap Builder
Transforms the raw project description, user experience level, and timeline into a structured, modular development roadmap.
* **JSON Schema Enforcement:** Enforces strict fields for phase milestones and data contract outputs, stripping unneeded fields to limit context window bloat.
* **Try/Except Caching Fail-safe:** If Gemini encounters Rate Limits (429/ResourceExhausted), the script automatically falls back to local disk cache (`roadmap_cache.json`).
* **Validation Locks:** Only updates the disk cache if the returned API string is verified as syntactically valid JSON.

## 2. Techstack Analyzer (Phase-Targeted Nested Loops)
Maps technical stacks to domain concepts phase-by-phase.
* **GPU OOM Optimization:** Solves the CUDA Out-of-Memory (500 Server Error) crash on budget 6GB VRAM cards.
* **Micro-Prompt Design:** Refactored from a single giant 8,000+ token query into small, sequential **Phase-Targeted Nested Loops** (Loop 1: Phase 1 MVP, Loop 2: Phase 2 Scalability upgrades). Keeps active token contexts under **~350 tokens** to prevent VRAM overflow.
* **Local Qwen Routing:** Integrates local Qwen-4B via a FastAPI server, automatically falling back to Gemini Cloud if the server is offline.

## 3. Material Fetcher (Parallel Resource Router)
Discovers and compiles curated developer learning links for every service and concept.
* **Multi-Threaded Concurrency:** Launches queries concurrently across multiple search tools (`YOUTUBE`, `GITHUB`, `GOOGLE_BOOKS`, `ARXIV`) using Python's `concurrent.futures.ThreadPoolExecutor`. 
* **Fetch Latency Reduction:** Cuts sequential HTTP search API time from **40+ seconds down to ~12 seconds**.
* **Direct Gemini Synthesis:** Packages the top-5 resource links fetched by the threads and passes them directly to Gemini 2.5 Flash to write a detailed, structured 30-day learning curriculum.

## 4. Tool Manager
Serves as the centralized registry interface for all search tools, abstracting tool metadata (functions, search rules, files) from the router script.

---

# Features

## Completed MVP Features
* **Interactive Roadmap Generator:** Builds logic-driven, timeline-aware engineering guides.
* **Offline Caching:** Full try/except local disk failover capability for roadmaps and techstacks.
* **Parallel Material Search:** Concurrently crawls GitHub, YouTube, arXiv, and Google Books.
* **Self-Healing API Core:** Custom retry helper (`safe_generate_json`) that intercepts rate limits (429) and performs exponential backoff.

## Planned Features
* **Weak Topic Detection:** Analyzing mock test scores to dynamically output study cards.
* **Spaced Repetition:** Flashcard generators based on notes.
* **Doubt Solver:** Voice and image-based document question-answering.
* **Admin Dashboard:** Console interfaces for handbook uploads.

---

# Repository Structure

```text
SHARQO/
│
├── config/
│   └── tool_reg.py
│
├── src/
│   ├── api_helper.py
│   ├── local_llm_client.py
│   ├── main.py
│   ├── material_fetcher.py
│   ├── roadmap_builder.py
│   ├── techstack_analyzer.py
│   └── tool_manager.py
│
├── tools/
│   ├── arxiv_tool.py
│   ├── github_tool.py
│   ├── google_books_tool.py
│   ├── web_search_tool.py
│   └── youtube_tool.py
│
├── requirements.txt
└── README.md
```

---

# Technologies

SHARQO is built using the following core technologies:

* **Development Language:** Python 3.10+
* **Local LLM Engine:** Qwen 4B Instruct (`unsloth/Qwen3-4B-Instruct-2507-unsloth-bnb-4bit` quantized in 4-bit) running on a local CUDA FastAPI server.
* **Cloud LLM Integration:** Google Gemini API (via `google-genai` SDK).
* **Vector Database:** Qdrant Cloud.
* **Search / API Services:** Tavily API, YouTube Data API v3, GitHub Search API, arXiv API, Google Books API.

---

# Project Status

🚧 **This project is currently under active development.**

Features, architecture, and modules are continuously evolving.

---

# Future Goals

SHARQO is being developed as an extensible platform. The following capabilities are planned for future releases:

- Personalized learning roadmaps based on the user's experience and goals.
- Interactive project planning with dynamic roadmap updates.
- Multi-agent architecture for specialized planning, analysis, and mentoring tasks.
- AI-powered code review and debugging assistance.
- Architectural improvement and optimization suggestions.
- Automatic project folder structure generation.
- Technology stack comparison and recommendation engine.
- Curated resource ranking based on quality, relevance, and difficulty.
- Progress tracking with milestone-based learning.
- Resume-oriented project recommendations and portfolio guidance.
- AI-generated documentation and project reports.
- Support for multiple AI providers and interchangeable LLM backends.
- Browser extension for contextual project assistance.
- Full-stack web application with user authentication and cloud synchronization.
- Team collaboration features for group projects and startup development.
- Integration with GitHub for repository analysis and project evolution.
- Continuous roadmap adaptation as project requirements evolve.

---

# Contributing

Contributions are always welcome!

Whether it's fixing bugs, improving documentation, adding new tool integrations, enhancing the architecture, or suggesting new ideas, every contribution helps make SHARQO better.

If you'd like to contribute:

1. Fork the repository.
2. Create a new feature or bug-fix branch.
3. Commit your changes with clear commit messages.
4. Submit a Pull Request describing your changes.

If you have ideas for new features, architectural improvements, or integrations, feel free to open an Issue and start a discussion before implementing them.

Together, we can build an AI assistant that empowers developers to turn ideas into reality.

---

# License

> *To be added.*
