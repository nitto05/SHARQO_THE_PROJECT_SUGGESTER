import time
from google import genai
from tools.github_tool import get_repositories
from tools.arxiv_tool import get_papers
from tools.crossref_tool import get_crossref_papers
from tools.pubmed_tool import get_pubmed_papers
from dotenv import load_dotenv
import os

load_dotenv()   # Loads variables from .env

# youtube_key = os.getenv("YOUTUBE_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")

# print(youtube_key)
# print(gemini_key)

#sample input : I want to learn RAG using projects, research papers and journal articles

#output for it : 
# f """ 
# what do you need??? : I want to learn RAG using projects, research papers and journal articles
# Raw Gemini Output:
# TOOLS: GITHUB,ARXIV,CROSSREF

# GITHUB_QUERY: RAG implementation
# ARXIV_QUERY: "Retrieval Augmented Generation" OR RAG survey
# CROSSREF_QUERY: "Retrieval Augmented Generation" OR RAG journal
# Detected Tools:  ['GITHUB', 'ARXIV', 'CROSSREF']
# Search Query:  {'GITHUB_QUERY': 'RAG implementation', 'ARXIV_QUERY': '"Retrieval Augmented Generation" OR RAG survey', 'CROSSREF_QUERY': '"Retrieval Augmented Generation" OR RAG journal'}
# Searching GitHub...
# Searching Arxiv...
# Searching Crossref...


#  ==== GITHUB ====



#         Name: GenAI_Agents
#         Owner: NirDiamant
#         Stars: 22750
#         Description: 50+ tutorials and implementations for Generative AI Agent techniques, from basic conversational bots to complex multi-agent systems.
#         url : https://github.com/NirDiamant/GenAI_Agents
#         language : Jupyter Notebook
#         forks_count : 3824
#         html_url : https://github.com/NirDiamant/GenAI_Agents
#         topics : ['agentic-ai', 'agents', 'ai', 'ai-agents', 'autonomous-agents', 'genai', 'generative-ai', 'langchain', 'langgraph', 'llm', 'llms', 'machine-learning', 'mcp', 'multi-agent', 'multi-agent-systems', 'openai', 'python', 'rag', 'tutorials']
#         README : [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
# [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/nir-diamant-759323134/)
# [![Reddit](https://img.shields.io/badge/Reddit-Join%20our%20
        
#         Name: langchain4j
#         Owner: langchain4j
#         Stars: 12376
#         Description: LangChain4j is an idiomatic, open-source Java library for building LLM-powered applications on the JVM. It offers a unified API over popular LLM providers and vector stores, and makes implementing tool calling (including MCP support), agents and RAG easy. It integrates seamlessly with enterprise Java frameworks like Quarkus and Spring Boot.
#         url : https://github.com/langchain4j/langchain4j
#         language : Java
#         forks_count : 2318
#         html_url : https://github.com/langchain4j/langchain4j
#         topics : ['anthropic', 'chatgpt', 'chroma', 'embeddings', 'gemini', 'gpt', 'huggingface', 'java', 'langchain', 'llama', 'llm', 'llms', 'milvus', 'ollama', 'onnx', 'openai', 'openai-api', 'pgvector', 'pinecone', 'vector-database']
#         README : # LangChain4j: idiomatic, open-source Java library for building LLM-powered applications on the JVM

# [![Build Status](https://img.shields.io/github/actions/workflow/status/langchain4j/langchain4j/main.yaml?branch=main&style=for-the-badge&label=CI%20BUILD&logo=github)](https://github.com/langchain4j/
        
#         Name: nano-graphrag
#         Owner: gusye1234
#         Stars: 3890
#         Description: A simple, easy-to-hack GraphRAG implementation
#         url : https://github.com/gusye1234/nano-graphrag
#         language : Python
#         forks_count : 418
#         html_url : https://github.com/gusye1234/nano-graphrag
#         topics : ['gpt', 'gpt-4o', 'graphrag', 'learning-by-doing', 'llm', 'rag']
#         README : <div align="center">
#   <a href="https://github.com/gusye1234/nano-graphrag">
#     <picture>
#       <source media="(prefers-color-scheme: dark)" srcset="https://assets.memodb.io/nano-graphrag-dark.png">
#       <img alt="Shows the MemoDB logo" src="https://assets.memodb.io/nano-graphrag.png" width="512">
        
#         Name: Awesome-Context-Engineering
#         Owner: Meirtz
#         Stars: 3193
#         Description:  🔥 Comprehensive survey on Context Engineering: from prompt engineering to production-grade AI systems. hundreds of papers, frameworks, and  implementation guides for LLMs and AI agents.
#         url : https://github.com/Meirtz/Awesome-Context-Engineering
#         language : None
#         forks_count : 248
#         html_url : https://github.com/Meirtz/Awesome-Context-Engineering
#         topics : ['agent', 'agentic-ai', 'agi', 'awesome-list', 'cognitive-science', 'context-engineering', 'llm', 'rag']
#         README : # Awesome Context Engineering

# <div align="center">
#   <img src="cover.png" alt="Awesome Context Engineering Cover" width="800"/>
# </div>

# ## 💬 Join Our Community

# <div align="center">
#   <img src="assets/wechat_group.png" alt="WeChat Group" width="200"/>
#   <p><strong>Join our WeChat group for discussi
        
#         Name: Hands-On-AI-Engineering
#         Owner: Sumanth077
#         Stars: 2419
#         Description: A curated collection of practical AI projects implementing OCR systems, RAG, AI agents, and other AI use cases.
#         url : https://github.com/Sumanth077/Hands-On-AI-Engineering
#         language : Python
#         forks_count : 656
#         html_url : https://github.com/Sumanth077/Hands-On-AI-Engineering
#         topics : ['agents', 'ai', 'ai-agents', 'ai-engineering', 'generative-ai', 'llms', 'mcp', 'ocr', 'python', 'rag']
#         README : <p align="center">
#   <a href="https://aiengineering.beehiiv.com/">
#     <img src="assets/theaiengineering_logo.jpeg" alt="Hands-On AI Engineering Banner" width="150">
#   </a>
# </p>
# <div align="center">

# # 🚀 Hands-On AI Engineering

# [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](
        
#         Name: self-rag
#         Owner: AkariAsai
#         Stars: 2397
#         Description: This includes the original implementation of SELF-RAG: Learning to Retrieve, Generate and Critique through self-reflection by Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, and Hannaneh Hajishirzi.
#         url : https://github.com/AkariAsai/self-rag
#         language : Python
#         forks_count : 225
#         html_url : https://github.com/AkariAsai/self-rag
#         topics : []
#         README : # SELF-RAG: Learning to Retrieve, Generate and Critique through Self-reflection

# This includes the original implementation of [SELF-RAG: Learning to Retrieve, Generate and Critique through self-reflection](https://arxiv.org/abs/2310.11511) (ICLR 2024, Oral top 1%) by Akari Asai, Zeqiu Wu, Yizhong Wa
        
#         Name: RAG-Challenge-2
#         Owner: IlyaRice
#         Stars: 2375
#         Description: Implementation of my RAG system that won all categories in Enterprise RAG Challenge 2
#         url : https://github.com/IlyaRice/RAG-Challenge-2
#         language : Python
#         forks_count : 487
#         html_url : https://github.com/IlyaRice/RAG-Challenge-2
#         topics : []
#         README : # RAG Challenge Winner Solution

# **Read more about this project:**
# - Russian: https://habr.com/ru/articles/893356/
# - English: https://abdullin.com/ilya/how-to-build-best-rag/

# This repository contains the winning solution for both prize nominations in the RAG Challenge competition. The system achiev
        
#         Name: raptor
#         Owner: parthsarthi03
#         Stars: 1705
#         Description: The official implementation of RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval
#         url : https://github.com/parthsarthi03/raptor
#         language : Python
#         forks_count : 227
#         html_url : https://github.com/parthsarthi03/raptor
#         topics : ['agents', 'clustering', 'framework', 'language-model', 'llm', 'machine-learning', 'rag', 'retrieval', 'retrieval-augmented-generation', 'vector-database']
#         README : <!-- <p align="center">
#   <img align="center" src="raptor.jpg" width="1000px" />
# </p>
# <p align="left"> -->

# <!-- <picture>
#   <source media="(prefers-color-scheme: dark)" srcset="raptor.jpg" width="1000px">
#   <source media="(prefers-color-scheme: light)" srcset="raptor_dark.png" width="1000px">
  
# </
        
#         Name: generative-ai-use-cases
#         Owner: aws-samples
#         Stars: 1355
#         Description: Application implementation with business use cases for safely utilizing generative AI in business operations
#         url : https://github.com/aws-samples/generative-ai-use-cases
#         language : TypeScript
#         forks_count : 429
#         html_url : https://github.com/aws-samples/generative-ai-use-cases
#         topics : ['aws', 'bedrock', 'chatbot', 'claude', 'claude3', 'claude4', 'command-r', 'deepseek-r1', 'generative-ai', 'image-generation', 'lambda', 'llama3', 'llm', 'mistral', 'nova', 'rag', 'react', 'sagemaker', 'typescript']
#         README : <div markdown="1" align="center">
#   <h1>Generative AI Use Cases (GenU)</h1>

# [![](https://img.shields.io/badge/Documentation-Latest-blue)](https://aws-samples.github.io/generative-ai-use-cases/index.html) [![](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/aws-samples/generat
        
#         Name: llmwiki
#         Owner: lucasastorian
#         Stars: 1168
#         Description: Open Source Implementation of Karpathy's LLM Wiki. Upload documents, connect your Claude account via MCP, and have it write your wiki ! 
#         url : https://github.com/lucasastorian/llmwiki
#         language : Python
#         forks_count : 187
#         html_url : https://github.com/lucasastorian/llmwiki
#         topics : ['agents', 'ai-agents', 'claude', 'karpathy', 'knowledge-base', 'llm', 'llm-wiki', 'mcp', 'mcp-server', 'rag', 'supabase']
#         README : # LLM Wiki

# **An autonomous, self-maintaining personal Wikipedia built and maintained by AI.**

# [![License](https://img.shields.io/badge/license-Apache%202.0-green)](https://opensource.org/licenses/Apache-2.0)

# </div>

# LLM Wiki transforms your scattered reading and research into a persistent, AI-mai
        


#  ==== ARXIV ====



#             Title: FAIR-RAG: Faithful Adaptive Iterative Refinement for Retrieval-Augmented Generation
#             published : 2025-10-25T15:59:33Z
#             Abstract : While Retrieval-Augmented Generation (RAG) mitigates hallucination and knowledge staleness in Large Language Models (LLMs), existing frameworks often falter on complex, multi-hop queries that require synthesizing information from disparate sources. Current advanced RAG methods, employing iterative o
#             pdf : https://arxiv.org/pdf/2510.22344v1
        
#             Title: Engineering the RAG Stack: A Comprehensive Review of the Architecture and Trust Frameworks for Retrieval-Augmented Generation Systems
#             published : 2025-11-07T16:26:29Z
#             Abstract : This article provides a comprehensive systematic literature review of academic studies, industrial applications, and real-world deployments from 2018 to 2025, providing a practical guide and detailed overview of modern Retrieval-Augmented Generation (RAG) architectures. RAG offers a modular approach
#             pdf : https://arxiv.org/pdf/2601.05264v1
        
#             Title: Retrieval Augmented Generation (RAG) for Fintech: Agentic Design and Evaluation
#             published : 2025-10-29T13:41:36Z
#             Abstract : Retrieval-Augmented Generation (RAG) systems often face limitations in specialized domains such as fintech, where domain-specific ontologies, dense terminology, and acronyms complicate effective retrieval and synthesis. This paper introduces an agentic RAG architecture designed to address these chal
#             pdf : https://arxiv.org/pdf/2510.25518v1
        
#             Title: MultiHop-RAG: Benchmarking Retrieval-Augmented Generation for Multi-Hop Queries
#             published : 2024-01-27T11:41:48Z
#             Abstract : Retrieval-augmented generation (RAG) augments large language models (LLM) by retrieving relevant knowledge, showing promising potential in mitigating LLM hallucinations and enhancing response quality, thereby facilitating the great adoption of LLMs in practice. However, we find that existing RAG sys
#             pdf : https://arxiv.org/pdf/2401.15391v1
        
#             Title: Ask in Any Modality: A Comprehensive Survey on Multimodal Retrieval-Augmented Generation
#             published : 2025-02-12T22:33:41Z
#             Abstract : Large Language Models (LLMs) suffer from hallucinations and outdated knowledge due to their reliance on static training data. Retrieval-Augmented Generation (RAG) mitigates these issues by integrating external dynamic information for improved factual grounding. With advances in multimodal learning, 
#             pdf : https://arxiv.org/pdf/2502.08826v3
        
#             Title: Automated Literature Review Using NLP Techniques and LLM-Based Retrieval-Augmented Generation
#             published : 2024-11-27T18:27:07Z
#             Abstract : This research presents and compares multiple approaches to automate the generation of literature reviews using several Natural Language Processing (NLP) techniques and retrieval-augmented generation (RAG) with a Large Language Model (LLM). The ever-increasing number of research articles provides a h
#             pdf : https://arxiv.org/pdf/2411.18583v1
        
#             Title: Riddle Me This! Stealthy Membership Inference for Retrieval-Augmented Generation
#             published : 2025-02-01T04:01:18Z
#             Abstract : Retrieval-Augmented Generation (RAG) enables Large Language Models (LLMs) to generate grounded responses by leveraging external knowledge databases without altering model parameters. Although the absence of weight tuning prevents leakage via model parameters, it introduces the risk of inference adve
#             pdf : https://arxiv.org/pdf/2502.00306v2
        
#             Title: Retrieval-Augmented Generation for AI-Generated Content: A Survey
#             published : 2024-02-29T18:59:01Z
#             Abstract : Advancements in model algorithms, the growth of foundational models, and access to high-quality datasets have propelled the evolution of Artificial Intelligence Generated Content (AIGC). Despite its notable successes, AIGC still faces hurdles such as updating knowledge, handling long-tail data, miti
#             pdf : https://arxiv.org/pdf/2402.19473v6
        
#             Title: GFM-RAG: Graph Foundation Model for Retrieval Augmented Generation
#             published : 2025-02-03T07:04:29Z
#             Abstract : Retrieval-augmented generation (RAG) has proven effective in integrating knowledge into large language models (LLMs). However, conventional RAGs struggle to capture complex relationships between pieces of knowledge, limiting their performance in intricate reasoning that requires integrating knowledg
#             pdf : https://arxiv.org/pdf/2502.01113v3
        
#             Title: Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG
#             published : 2025-01-15T20:40:25Z
#             Abstract : Large Language Models (LLMs) have advanced artificial intelligence by enabling human-like text generation and natural language understanding. However, their reliance on static training data limits their ability to respond to dynamic, real-time queries, resulting in outdated or inaccurate outputs. Re
#             pdf : https://arxiv.org/pdf/2501.09136v4
        
#             Title: Overview of the TREC 2025 Retrieval Augmented Generation (RAG) Track
#             published : 2026-03-10T16:49:18Z
#             Abstract : The second edition of the TREC Retrieval Augmented Generation (RAG) Track advances research on systems that integrate retrieval and generation to address complex, real-world information needs. Building on the foundation of the inaugural 2024 track, this year's challenge introduces long, multi-senten
#             pdf : https://arxiv.org/pdf/2603.09891v1
        
#             Title: Improving the Domain Adaptation of Retrieval Augmented Generation (RAG) Models for Open Domain Question Answering
#             published : 2022-10-06T01:21:25Z
#             Abstract : Retrieval Augment Generation (RAG) is a recent advancement in Open-Domain Question Answering (ODQA). RAG has only been trained and explored with a Wikipedia-based external knowledge base and is not optimized for use in other specialized domains such as healthcare and news. In this paper, we evaluate
#             pdf : https://arxiv.org/pdf/2210.02627v1
        
#             Title: Harnessing Retrieval-Augmented Generation (RAG) for Uncovering Knowledge Gaps
#             published : 2023-12-12T23:22:57Z
#             Abstract : The paper presents a methodology for uncovering knowledge gaps on the internet using the Retrieval Augmented Generation (RAG) model. By simulating user search behaviour, the RAG system identifies and addresses gaps in information retrieval systems. The study demonstrates the effectiveness of the RAG
#             pdf : https://arxiv.org/pdf/2312.07796v1
        
#             Title: Scaling Beyond Context: A Survey of Multimodal Retrieval-Augmented Generation for Document Understanding
#             published : 2025-10-17T02:33:16Z
#             Abstract : Document understanding is critical for applications from financial analysis to scientific discovery. Current approaches, whether OCR-based pipelines feeding Large Language Models (LLMs) or native Multimodal LLMs (MLLMs), face key limitations: the former loses structural detail, while the latter stru
#             pdf : https://arxiv.org/pdf/2510.15253v3
        
#             Title: Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs
#             published : 2025-02-16T18:46:10Z
#             Abstract : Retrieval-augmented generation (RAG) enhances large language models (LLMs) for domain-specific question-answering (QA) tasks by leveraging external knowledge sources. However, traditional RAG systems primarily focus on relevance-based retrieval and often struggle with redundancy, especially when rea
#             pdf : https://arxiv.org/pdf/2502.11228v2
        
#             Title: Collab-RAG: Boosting Retrieval-Augmented Generation for Complex Question Answering via White-Box and Black-Box LLM Collaboration
#             published : 2025-04-07T10:52:22Z
#             Abstract : Retrieval-Augmented Generation (RAG) systems often struggle to handle multi-hop question-answering tasks accurately due to irrelevant context retrieval and limited complex reasoning capabilities. We introduce Collab-RAG, a collaborative training framework that leverages mutual enhancement between a 
#             pdf : https://arxiv.org/pdf/2504.04915v1
        
#             Title: A Collaborative Multi-Agent Approach to Retrieval-Augmented Generation Across Diverse Data
#             published : 2024-12-08T07:18:19Z
#             Abstract : Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by incorporating external, domain-specific data into the generative process. While LLMs are highly capable, they often rely on static, pre-trained datasets, limiting their ability to integrate dynamic or private data. Traditi
#             pdf : https://arxiv.org/pdf/2412.05838v1
        
#             Title: Auto-RAG: Autonomous Retrieval-Augmented Generation for Large Language Models
#             published : 2024-11-29T03:01:05Z
#             Abstract : Iterative retrieval refers to the process in which the model continuously queries the retriever during generation to enhance the relevance of the retrieved knowledge, thereby improving the performance of Retrieval-Augmented Generation (RAG). Existing work typically employs few-shot prompting or manu
#             pdf : https://arxiv.org/pdf/2411.19443v1
        
#             Title: A Comprehensive Survey of Retrieval-Augmented Generation (RAG): Evolution, Current Landscape and Future Directions
#             published : 2024-10-03T22:29:47Z
#             Abstract : This paper presents a comprehensive study of Retrieval-Augmented Generation (RAG), tracing its evolution from foundational concepts to the current state of the art. RAG combines retrieval mechanisms with generative language models to enhance the accuracy of outputs, addressing key limitations of LLM
#             pdf : https://arxiv.org/pdf/2410.12837v1
        
#             Title: A survey: Information search time optimization based on RAG (Retrieval Augmentation Generation) chatbot
#             published : 2025-11-10T22:39:26Z
#             Abstract : Retrieval-Augmented Generation (RAG) based chatbots are not only useful for information retrieval through questionanswering but also for making complex decisions based on injected private data.we present a survey on how much search time can be saved when retrieving complex information within an orga
#             pdf : https://arxiv.org/pdf/2601.07838v1
        


#  ==== CROSSREF ====



#                     Title : Efficient Information Retrieval and Response Generation with Retrieval-Augmented Generation (RAG)
#                     Year : unknown
#                     DOI : 10.59350/r9dj1-zkx52

                        
#                     Title : Efficient Information Retrieval and Response Generation with Retrieval-Augmented Generation (RAG)
#                     Year : unknown
#                     DOI : 10.59350/q2pq3-0fv85

                        
#                     Title : Retrieval Augmented Generation (RAG) Model
#                     Year : 2025
#                     DOI : 10.55248/gengpi.6.0125.0635

                        
#                     Title : Implementation of an Academic Information Chatbot Based on Retrieval-Augmented Generation (RAG) Using LLaMA 3.1
#                     Year : unknown
#                     DOI : 10.21070/ups.9995

                        
#                     Title : Understanding Retrieval Pitfalls: Challenges Faced by Retrieval Augmented Generation (RAG) models
#                     Year : unknown
#                     DOI : 10.59350/wek8b-sbj84

                        
#                     Title : Prospects of Retrieval Augmented Generation (RAG) for Academic Library Search and Retrieval
#                     Year : unknown
#                     DOI : 10.2139/ssrn.5295044

                        
#                     Title : Understanding Retrieval Pitfalls: Challenges Faced by Retrieval Augmented Generation (RAG) models
#                     Year : unknown
#                     DOI : 10.59350/xcq3s-jvk04

                        
#                     Title : Rag: The Revolution of Retrieval-Augmented Text Generation
#                     Year : unknown
#                     DOI : 10.2139/ssrn.5252835

                        
#                     Title : Introduction to Retrieval-Augmented Generation (RAG)
#                     Year : 2025
#                     DOI : 10.1007/979-8-8688-1808-0_1

                        
#                     Title : Review for "Text2SQL Business Intelligence System Based on Retrieval-Augmented Generation (RAG)"
#                     Year : 2025
#                     DOI : 10.1002/eng2.70249/v1/review2

                        

# Generating analysis...


#  ==== FINAL ANALYSIS ==== 

# Here's an analysis of the provided resources to help you learn RAG:

# ## RAG Learning Plan

# ### 1. Top 5 Resources Overall

# 1.  **Awesome-Context-Engineering (GitHub):** This is a fantastic starting point as it's a comprehensive survey with many papers, frameworks, and implementation guides. It acts as a meta-resource, pointing you to many other valuable materials.
# 2.  **A Comprehensive Survey of Retrieval-Augmented Generation (RAG): Evolution, Current Landscape and Future Directions (arXiv):** This survey paper provides a broad overview of RAG, its history, current trends, and future prospects. It's essential for understanding the RAG landscape.
# 3.  **GenAI_Agents (GitHub):** While broader than just RAG, this repository offers numerous tutorials and implementations for Generative AI Agents, many of which will involve RAG. Learning agentic systems is a natural progression from understanding RAG.
# 4.  **Engineering the RAG Stack: A Comprehensive Review of the Architecture and Trust Frameworks for Retrieval-Augmented Generation Systems (arXiv):** This paper dives deep into the architecture of RAG systems, which is crucial for building and understanding them effectively.
# 5.  **Hands-On-AI-Engineering (GitHub):** This repository focuses on practical AI projects, including RAG implementations. Hands-on experience is invaluable for solidifying theoretical knowledge.

# ### 2. Top 3 Beginner Resources

# 1.  **Awesome-Context-Engineering (GitHub):** Its "comprehensive survey" nature makes it a great entry point to get a lay of the land and discover introductory materials.
# 2.  **Introduction to Retrieval-Augmented Generation (RAG) (Crossref):** This appears to be a foundational resource explicitly covering the basics of RAG.
# 3.  **Hands-On-AI-Engineering (GitHub):** Practical examples are often easier to grasp for beginners than purely theoretical papers. This repo should offer concrete implementations.

# ### 3. Top 3 Advanced Resources

# 1.  **FAIR-RAG: Faithful Adaptive Iterative Refinement for Retrieval-Augmented Generation (arXiv):** This paper likely delves into more sophisticated RAG techniques, such as iterative refinement, which is an advanced topic.
# 2.  **MultiHop-RAG: Benchmarking Retrieval-Augmented Generation for Multi-Hop Queries (arXiv):** Handling multi-hop queries is a more complex challenge in RAG, indicating an advanced approach.
# 3.  **GFM-RAG: Graph Foundation Model for Retrieval Augmented Generation (arXiv):** Integrating graph foundation models with RAG suggests a cutting-edge and complex application of RAG principles.

# ### 4. Best Projects to Build

# 1.  **GenAI_Agents (GitHub):** Building an agent that uses RAG to answer questions based on a custom knowledge base would be a highly practical project.
# 2.  **Hands-On-AI-Engineering (GitHub):** Explore the RAG-specific projects here to get hands-on experience with implementation.
# 3.  **nano-graphrag (GitHub):** This project specifically mentions "GraphRAG," which is an interesting and potentially advanced area to explore for building a more sophisticated RAG system.

# ### 5. Best Research Papers to Read

# 1.  **A Comprehensive Survey of Retrieval-Augmented Generation (RAG): Evolution, Current Landscape and Future Directions (arXiv):** Essential for a broad understanding.
# 2.  **Engineering the RAG Stack: A Comprehensive Review of the Architecture and Trust Frameworks for Retrieval-Augmented Generation Systems (arXiv):** For a deep dive into the technical architecture.
# 3.  **FAIR-RAG: Faithful Adaptive Iterative Refinement for Retrieval-Augmented Generation (arXiv):** To understand advanced RAG techniques for improving faithfulness.
# 4.  **Retrieval Augmented Generation (RAG) for Fintech: Agentic Design and Evaluation (arXiv):** To see RAG applied in a specialized domain with an agentic approach.
# 5.  **Automated Literature Review Using NLP Techniques and LLM-Based Retrieval-Augmented Generation (arXiv):** A practical application of RAG for research itself.

# ### 6. Recommended Reading Order

# 1.  **Beginner Resources:** Start with "Introduction to Retrieval-Augmented Generation (RAG)" and explore "Hands-On-AI-Engineering" for practical examples.
# 2.  **Broad Overview:** Read "A Comprehensive Survey of Retrieval-Augmented Generation (RAG): Evolution, Current Landscape and Future Directions."
# 3.  **Architectural Deep Dive:** Study "Engineering the RAG Stack: A Comprehensive Review of the Architecture and Trust Frameworks for Retrieval-Augmented Generation Systems."
# 4.  **Key Concepts and Frameworks:** Dive into "Awesome-Context-Engineering" to discover more papers and frameworks.
# 5.  **Advanced Topics:** Explore papers like "FAIR-RAG," "MultiHop-RAG," and "GFM-RAG" as you gain more confidence.
# 6.  **Practical Implementation:** Refer to "GenAI_Agents" and "nano-graphrag" for project ideas and implementation details.

# ### 7. 30-Day Learning Roadmap

# This roadmap assumes you can dedicate a few hours per day.

# **Week 1: Foundations of RAG**

# *   **Days 1-3:** Read "Introduction to Retrieval-Augmented Generation (RAG)" and skim through "Awesome-Context-Engineering" to get a sense of the landscape.
# *   **Days 4-7:** Read "A Comprehensive Survey of Retrieval-Augmented Generation (RAG): Evolution, Current Landscape and Future Directions." Focus on understanding the core components (retriever, generator) and the evolution of RAG.

# **Week 2: RAG Architecture and Practicalities**

# *   **Days 8-11:** Read "Engineering the RAG Stack: A Comprehensive Review of the Architecture and Trust Frameworks for Retrieval-Augmented Generation Systems."
# *   **Days 12-14:** Start exploring "Hands-On-AI-Engineering." Try to run one of the RAG examples. Understand the code and the tools used (e.g., LangChain, vector databases).

# **Week 3: Exploring Advanced Concepts and Projects**

# *   **Days 15-18:** Begin with "FAIR-RAG: Faithful Adaptive Iterative Refinement for Retrieval-Augmented Generation." Focus on the challenges it addresses and its proposed solutions.
# *   **Days 19-21:** Explore "GenAI_Agents." Look for examples that specifically leverage RAG. Try to understand how agents interact with RAG components. Consider starting a small project from this repo.

# **Week 4: Deepening Knowledge and Specialization**

# *   **Days 22-25:** Read "MultiHop-RAG: Benchmarking Retrieval-Augmented Generation for Multi-Hop Queries" or "GFM-RAG: Graph Foundation Model for Retrieval Augmented Generation," depending on your interest. These are more specialized.
# *   **Days 26-28:** Explore "nano-graphrag" and "RAG-Challenge-2" for different RAG implementation strategies.
# *   **Days 29-30:** Review the "Awesome-Context-Engineering" list and pick 2-3 more papers or frameworks that pique your interest for further exploration. Reflect on what you've learned and identify areas for deeper study.

# ### 8. Skills That Will Be Learned

# *   **Understanding of RAG principles:** How retrieval and generation work together.
# *   **RAG architectures:** Different ways RAG systems can be designed and implemented.
# *   **Key RAG components:** Retrievers (vector databases, similarity search), generators (LLMs), and the integration layer.
# *   **Prompt Engineering for RAG:** Crafting effective prompts to guide RAG systems.
# *   **Vector Databases:** Concepts and practical usage (e.g., Chroma, Pinecone, Milvus).
# *   **LLM Integration:** How to connect and utilize LLMs within a RAG pipeline.
# *   **Evaluation of RAG systems:** Metrics and methods to assess RAG performance.
# *   **Advanced RAG techniques:** Iterative refinement, multi-hop reasoning, agentic RAG.
# *   **Context Engineering:** Broader concepts related to managing and utilizing context in AI systems.
# *   **Practical Implementation:** Building RAG applications using libraries like LangChain.

# ### 9. Resources That Can Be Skipped Initially

# *   **langchain4j (GitHub):** Unless you are specifically working with Java on the JVM, this resource is specialized and can be skipped for initial RAG learning.
# *   **RAG-Challenge-2 (GitHub):** While it showcases a winning solution, it might be more beneficial to understand the fundamentals first before diving into highly optimized or competitive solutions.
# *   **self-rag (GitHub):** This is a specific research implementation. It's valuable for understanding advanced concepts but might be too specific for an initial broad understanding of RAG.
# *   **raptor (GitHub):** Similar to `self-rag`, this is a specific RAG approach. It's good to know about but not essential for foundational learning.
# *   **llmwiki (GitHub):** This is an interesting application of RAG but might not be the most direct resource for learning the core RAG mechanisms.

# By following this plan, you should gain a solid understanding of RAG, from its fundamental principles to advanced applications and practical implementations. Good luck with your learning journey!
# completed in 24.33681869506836 seconds
# """

client = genai.Client (api_key = gemini_key)


goal = input("what do you need??? : ")
start = time.time()

# prompt = f""" 
# A user wants : {goal}

# if goal can be solved using github repos and all the stuff related to it... 

# then give output : "GITHUB" 

# else if the user wants to get data for research paper and stuff related to science and thesis...

# then give output : "OPENALEX"

# that's it...
# """

prompt = f"""
User request:

{goal}

Rules:

- Return GITHUB if the user is looking for:
  - projects
  - repositories
  - source code
  - implementation examples
  - learning by building
  - open-source tools

- Return ARXIV if the user is looking for:
  - research papers
  - academic publications
  - surveys
  - thesis topics
  - scientific literature
  - state-of-the-art research

- Return CROSSREF if the user mentions:
  - journal articles
  - journal papers
  - conference papers
  - citations
  - DOI information
  - scholarly publications

- Return PUBMED if the user is looking for:
  - medicine
  - healthcare
  - biology
  - biomedical research
  - clinical studies
  - diseases
  - drugs
  - genetics
  - public health

Query Generation Rules:

GITHUB_QUERY:
Convert the following request into a GitHub repository search query.
Focus on repositories, frameworks, implementations and open-source projects.
Return only the search query.

ARXIV_QUERY:
Convert the user's request into a good arXiv search query.
Focus on research topics, surveys and academic terminology.
Return only the search query.

CROSSREF_QUERY:
Convert the user's request into a good Crossref search query.
Focus on journal papers, conference papers and scholarly terminology.
Return only the search query.

PUBMED_QUERY:
Convert the user's request into a good PubMed search query.
Focus on medicine, healthcare, biology and biomedical terminology.
Return only the search query.


Rules:

- Return ALL relevant categories.
- Categories must be comma-separated.
- If only one category is relevant, return only that category.
- If multiple categories are relevant, return all of them.
- Do not explain.
- Do not add extra text.

Output EXACTLY in this format:

TOOLS: tool1,tool2,...

Then ONLY output query lines for the selected tools.

Example:

TOOLS: ARXIV,CROSSREF

ARXIV_QUERY: machine learning
CROSSREF_QUERY: machine learning

Do NOT output GITHUB_QUERY if GITHUB is not selected.
Do NOT output PUBMED_QUERY if PUBMED is not selected.
and similarly if any tools is not selected, do not give their query lines...

Only include query lines for selected tools.
"""

# prompt = f"""
# User request:

# {goal}

# Determine:

# 1. Which tools should be used
# 2. A search query suitable for all selected tools

# Available tools:

# GITHUB
# ARXIV
# CROSSREF
# PUBMED

# Output EXACTLY in this format:

# TOOLS: tool1,tool2,...

# QUERY: search query

# Example:

# TOOLS: GITHUB,ARXIV

# QUERY: ai agents

# Do not explain.
# Do not add extra text.
# """

response = client.models.generate_content(
    # model="gemini-2.5-flash",
    # model = "gemini-2.0-flash",
    model="gemini-2.5-flash-lite",
    
    contents= prompt
    
)


# choice = response.text.strip().upper()

print("Raw Gemini Output:")
print(response.text)

lines = response.text.strip().split("\n")

tools_line = ""
# query_line = ""
queries = {}

for line in lines:
    line = line.strip()

    if line.startswith("TOOLS:"):
        tools_line = line
    elif "_QUERY:" in line:
        # query_line = line
        key, value = line.split(":", 1)

        queries[key.strip()] = value.strip() 

tools_text = tools_line.split(":", 1)[1]
choices = [
    tool.strip().upper()
    # for choice in response.text.split(",")

    for tool in tools_text.split(",")

] # gathers all the choices made by the agent

# search_query = query_line.replace("QUERY:", "").strip()

########## this dictionary should be stored in database...



print("Detected Tools: ", choices)
print("Search Query: ", queries)

all_data = {}

if "GITHUB" in choices and "GITHUB_QUERY" in queries:

    

    print("Searching GitHub...")
    repo_data = get_repositories(queries["GITHUB_QUERY"])

    # print(repo_data)
    # all_data += "\n\n === GITHUB === \n\n"
    # all_data += repo_data
    all_data["GITHUB"] = repo_data

if "ARXIV" in choices and "ARXIV_QUERY" in queries:

    
    
    print("Searching Arxiv...")
    arxiv_data = get_papers(queries["ARXIV_QUERY"])

    # print(paper_data)
    # all_data += "\n\n === ARXIV === \n\n"
    # all_data += paper_data
    all_data["ARXIV"] = arxiv_data

    
if "CROSSREF" in choices and "CROSSREF_QUERY" in queries:

    

    print("Searching Crossref...")
    crossref_data = get_crossref_papers(queries["CROSSREF_QUERY"])

    # print(crossref_data)
    # all_data += "\n\n === CROSSREF === \n\n"
    # all_data += crossref_data
    all_data["CROSSREF"] = crossref_data

if "PUBMED" in choices and "PUBMED_QUERY" in queries:

    

    print("Searching PubMed...")
    pubmed_data = get_pubmed_papers(queries["PUBMED_QUERY"])

    # print(pubmed_data)
    # "\n\n === PUBMED === \n\n"
    # all_data += pubmed_data
    all_data["PUBMED"] = pubmed_data

# print(all_data)
for source, results in all_data.items():
    # formatted_data += f"\n\n ==== {source} ==== \n\n"
    # formatted_data += results
    print(f"\n\n ==== {source} ====\n\n")
    print(results)

print("\nGenerating analysis...\n")

formatted_data = ""

for source, results in all_data.items():
    formatted_data += f"\n\n ==== {source} ==== \n\n"
    formatted_data += results

analysis_prompt = f"""
USER GOAL:

{goal}

Retrieved Resources:

{formatted_data}

Act as an expert mentor.

Analyze the resources and provide:

1. Top 5 resources overall
2. Top 3 beginner resources
3. Top 3 advanced resources
4. Best projects to build
5. Best research papers to read
6. Recommended reading order
7. 30-day learning roadmap
8. Skills that will be learned
9. Resources that can be skipped initially

Explain your reasoning briefly.
"""

analysis_response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=analysis_prompt
)
final_analysis = analysis_response.text
print("\n ==== FINAL ANALYSIS ==== \n")
print(final_analysis)

end = time.time()

print(f"completed in {end-start} seconds")

