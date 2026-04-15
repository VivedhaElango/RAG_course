# Mastering RAG — The Brain Friendly Way

This repository contains the notebooks and code for the **Mastering RAG — Brain Friendly Way** course. Each module builds on the last, taking you from "what is an LLM?" all the way to production-grade, agentic RAG systems.

---

## Course Overview

### Module 1: Understanding LLMs and Why We Need RAG

**Big question:** "What does your LLM actually know, how it knows, and what happens when it doesn't know enough?"

- [Lesson 1.1 — What Are Large Language Models?](https://vivedhaelango.substack.com/p/lesson-11-what-are-large-language)
- [Lesson 1.2 — How Do LLMs Actually Work Under the Hood?](https://vivedhaelango.substack.com/p/lesson-12-how-do-llms-actually-work)
- [Lesson 1.3 — Why Do LLMs Confidently Make Things Up?](https://vivedhaelango.substack.com/p/lesson-13-why-do-llms-confidently)
- [Lesson 1.4 — Why Do You Need RAG?](https://vivedhaelango.substack.com/p/lesson-14-why-do-you-need-rag)

---

### Module 2: How the RAG Pipeline Fits Together

**Big question:** "What are the moving parts of a RAG system and how do they talk to each other?"

- [Lesson 2.1 — What Does a RAG Pipeline Look Like End to End?](https://vivedhaelango.substack.com/p/lesson-21-what-does-a-rag-pipeline)
- [Lesson 2.2 — What Are the Failure Points in a Basic RAG System?](https://vivedhaelango.substack.com/p/what-are-the-failure-points-in-a)
- Lesson 2.3 — How to Build a Minimal Working RAG System?

---

### Module 3: Chunking

**Big question:** "Why can't you just feed the whole document to the LLM, and how do you break it up the right way?"

- Lesson 3.1 — Why Can't I Just Feed the Whole Document to the LLM?
- Lesson 3.2 — What Is a Chunk and How Big Should It Be?
- Lesson 3.3 — What Are the Different Chunking Strategies and When Do I Use Each?
- Lesson 3.4 — What Is Chunk Overlap and When Does It Help?
- Lesson 3.5 — How Do I Chunk PDFs, HTML, and Scanned Documents?
- Lesson 3.6 — How Do I Handle Tables, Code Blocks, and Lists?

---

### Module 4: Embeddings — Turning Words into Meaning

**Big question:** "How do you turn text into numbers that actually capture what the text means?"

- Lesson 4.1 — What Is an Embedding, Really?
- Lesson 4.2 — How Does an Embedding Model Work?
- Lesson 4.3 — How Do I Choose the Right Embedding Model for My RAG App?
- Lesson 4.4 — Should I Fine-Tune My Embedding Model?

---

### Module 5: Vector Databases — Your AI's Long-Term Memory

**Big question:** "Where do you store millions of embeddings and how do you search them in milliseconds?"

- Lesson 5.1 — How to Choose the Right VectorDB for Your RAG Application?
- Lesson 5.2 — How to Choose the Right Search Algorithm for Your VectorDB?
- Lesson 5.3 — What Is Metadata Filtering and Why Does It Change Everything?
- Lesson 5.4 — How Do I Handle Vector Database Updates and Deletions?

---

### Module 6: Search Strategies — Beyond Simple Similarity

**Big question:** "Why does pure semantic search sometimes return useless results, and what are your options when it does?"

- Lesson 6.1 — Why Doesn't Semantic Search Always Work?
- Lesson 6.2 — What Is BM25 and Why Do People Keep Reaching for It?
- Lesson 6.3 — What Is Hybrid Search and How Do You Combine the Scores?
- Lesson 6.4 — What Is a Reranker and When Do You Actually Need One?
- Lesson 6.5 — How Do I Measure Whether My Retrieval Is Any Good?

---

### Module 7: Prompting and Context — Making the LLM Use What You Retrieved

**Big question:** "You've retrieved the right documents — so why is the LLM still giving you a bad answer?"

- Lesson 7.1 — How Do You Write a RAG Prompt That Actually Works?
- Lesson 7.2 — What Is Context Stuffing and Why Does It Backfire?
- Lesson 7.3 — How Do You Manage Context When You Have More Chunks Than Fit?
- Lesson 7.4 — How Do You Tell the LLM to Say "I Don't Know"?
- Lesson 7.5 — What Is a RAG Answer Citation and How Do You Implement It?

---

### Module 8: When Simple RAG Breaks — Advanced Retrieval Patterns

**Big question:** "Why do complex, multi-part questions defeat basic RAG — and what architectures handle them?"

- Lesson 8.1 — Why Does My RAG Fail on Multi-Hop and Complex Questions?
- Lesson 8.2 — What Is Query Rewriting and How Does It Help Retrieval?
- Lesson 8.3 — What Is Multi-Query Retrieval and When Do You Use It?
- Lesson 8.4 — What Is Parent-Child Retrieval and Small-to-Big Chunking?
- Lesson 8.5 — What Is a Knowledge Graph and When Does GraphRAG Win?
- Lesson 8.6 — What Is Self-RAG and Corrective RAG?

---

### Module 9: Multi-Modal and Structured RAG

**Big question:** "What do you do when your documents contain images, tables, and charts — or when your data lives in a database?"

- Lesson 9.1 — How Do You Build a RAG System That Understands Images and Tables?
- Lesson 9.2 — How Do You RAG Over Structured Data Without Writing SQL by Hand?
- Lesson 9.3 — How Do You Handle Multilingual Documents in RAG?

---

### Module 10: Agentic RAG — When One Retrieval Step Isn't Enough

**Big question:** "What changes when your RAG system needs to plan, decide, and retrieve in multiple steps?"

- Lesson 10.1 — What Is Agentic RAG and How Is It Different from Standard RAG?
- Lesson 10.2 — Why Is Context the Real Reason Your Agent Breaks Down?
- Lesson 10.3 — What Is the Model Context Protocol and Why Does It Matter for RAG?
- Lesson 10.4 — How Do You Route Queries Between Different Retrieval Strategies?
- Lesson 10.5 — How Do You Evaluate an Agentic RAG System?

---

### Module 11: Evaluation — How Do You Know Your RAG Is Working?

**Big question:** "Everyone says 'evaluate your RAG' — but what do you measure and how do you do it without labelling thousands of examples by hand?"

- Lesson 11.1 — What Are the Right Evaluation Metrics for a RAG System?
- Lesson 11.2 — How Do You Build a Golden Evaluation Dataset Without Dying?
- Lesson 11.3 — How Do You Use an LLM as a Judge for RAG Evaluation?
- Lesson 11.4 — How Do You Detect Hallucinations in RAG Output?
- Lesson 11.5 — What Is Eval-Driven Development for RAG?
- Lesson 11.6 — How Do You Monitor RAG in Production Over Time?

---

### Module 12: Production RAG — Performance, Cost, Security, and Maintainability

**Big question:** "Your RAG works in the demo — now how do you make it fast, cheap, safe, and maintainable in the real world?"

- Lesson 12.1 — Why Is My RAG Fast in Dev and Slow in Production?
- Lesson 12.2 — How Do You Add Caching to a RAG System?
- Lesson 12.3 — How Do You Optimize RAG for Cost Without Killing Quality?
- Lesson 12.4 — What Security Holes Exist in RAG Systems That You Can't See?
- Lesson 12.5 — How Do You Handle PII and Sensitive Data in Your Document Store?
- Lesson 12.6 — What Technical Debts Accumulate Fastest in RAG Systems?
- Lesson 12.7 — What Does a Production-Grade RAG Architecture Look Like?
