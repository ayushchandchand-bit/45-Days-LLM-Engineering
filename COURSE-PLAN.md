# SSAI-101 — 45-Day Course Plan (Day by Day)

**Softpro School of AI — AI Development Summer Training**
3 hours/day · 45 days · 4 phases · **3 mini-projects + 1 capstone**, all deployed to public URLs.

> Days **1–7** are a Python power-up (prerequisite skills locked in before any LLM work). The AI
> track begins Day 8. Every phase ends with a shipped, deployed project.

---

## Daily 3-hour session structure
Each day is a single 3-hour block:

| Block | Time | Activity |
|-------|:----:|----------|
| Concept + live coding | 75 min | Trainer-led walkthrough of the day's modules; questions welcome |
| Guided build (code-along) | 45 min | Students type along, TA floats for help |
| Independent work | 45 min | Exercises / mini-project work / doubt-solving |
| Standup + wrap-up | 15 min | Recap, blockers, preview of next day |

Each day in this repo maps to a `Day-XX-Topic/` folder with numbered modules (`01-…`, `02-…`),
runnable examples, and an `exercises/` set.

---

## Phase overview

| Phase | Days | Focus | Ships |
|-------|:----:|-------|-------|
| 1 — Foundations | 1–15 | Python + first LLM app | **Project 1: Content Summarizer** |
| 2 — RAG & Memory | 16–25 | External knowledge / retrieval | **Project 2: Document Q&A** |
| 3 — Agents & Tools | 26–37 | Agents that take actions | **Project 3: Research Agent** |
| 4 — Capstone + Placement | 38–45 | Portfolio-grade project + job-ready | **Capstone** |

---

## Phase 1 — Foundations (Days 1–15)
*Goal: everyone at baseline; first working, deployed LLM app.*

### Python week (Days 1–7)
| Day | Topic | Key modules |
|----:|-------|-------------|
| 1 | Python setup, data types, operators & variables | running-python, numbers, operators, comments, variables, naming, assignment-ops, print |
| 2 | Strings, f-strings & string methods | strings, indexing, slices, escape/triple-quote, len/input/type-casting, f-strings, methods |
| 3 | Booleans, conditionals & logical operators | booleans, comparison, truthiness, if/elif/else, random, nesting, and/or/not, precedence |
| 4 | Loops | while, for, range, break/continue, nested loops |
| 5 | Functions & scope | params, return, default/keyword args, scope (LEGB), global, `*args`/`**kwargs` |
| 6 | Data structures | lists, dicts, tuples, sets (methods, slicing, iteration, mutability) |
| 7 | Errors, modules & OOP | error types, try/except, modules & pip, classes, methods, inheritance, `super()` |

### LLM foundations (Days 8–15)
| Day | Topic |
|----:|-------|
| 8 | Python for AI: `requests`, async basics, `dotenv`, **Pydantic**, type hints |
| 9 | LLM fundamentals: tokens, context windows, sampling (temperature, top-p), model families — **first Gemini API call** |
| 10 | Prompt engineering I: system prompts, zero-shot, few-shot, chain-of-thought |
| 11 | Prompt engineering II: structured outputs with Pydantic, JSON mode |
| 12 | Multi-provider patterns: one abstraction over Gemini, Groq, Ollama |
| 13 | Working with data: JSON, CSV, PDF (PyPDF2/pdfplumber), lightweight scraping (BeautifulSoup) |
| 14 | Streamlit crash course + error handling, retries, rate limits, cost awareness |
| 15 | **Mini-project 1 build + deploy + demo** |

**🚀 Project 1 — AI Content Summarizer.** Input: PDF / article URL / transcript. Output:
structured summary (key points, TL;DR, action items). Stack: Streamlit + Gemini + Python.
Deployed free on Hugging Face Spaces or Streamlit Community Cloud.

---

## Phase 2 — RAG & Memory (Days 16–25)
*Goal: apps that use external knowledge — the single most employable AI skill right now.*

| Day | Topic |
|----:|-------|
| 16 | Embeddings fundamentals: what they are; free options (sentence-transformers, Gemini embeddings) |
| 17 | Semantic search from scratch (numpy + cosine similarity, no framework) |
| 18 | Chroma — first vector DB: persistence, collections |
| 19 | pgvector via Supabase — local Chroma → cloud Postgres (free tier) |
| 20 | Chunking strategies: fixed, recursive, semantic, parent-document |
| 21 | Retrieval: k-NN, hybrid search (BM25 + vector) |
| 22 | Re-ranking with sentence-transformers cross-encoders |
| 23 | LlamaIndex introduction — when it beats raw code |
| 24 | **Mini-project 2 build day** |
| 25 | **Mini-project 2 deploy + demo** |

**🚀 Project 2 — Document Q&A System.** Input: upload notes / textbooks / papers. Output:
natural-language questions → cited answers. Stack: Streamlit + Chroma or pgvector + Gemini +
LlamaIndex. Deployed free on HF Spaces.

---

## Phase 3 — Agents & Tools (Days 26–37)
*Goal: go from Q&A bots to agents that take actions — the differentiator.*

| Day | Topic |
|----:|-------|
| 26 | Tool use / function calling — first principles, no framework |
| 27 | LangChain basics — chains, memory, the 20% you actually need |
| 28 | LangGraph — state machines for AI, when it makes sense |
| 29 | Building a ReAct agent with LangChain (research + summarize tool) |
| 30 | CrewAI — role-based multi-agent, made simple |
| 31 | AutoGen (Microsoft) — conversation-based multi-agent |
| 32 | OpenClaw — lightweight agentic framework |
| 33 | Framework comparison workshop — same agent in 3 frameworks, pick which fits |
| 34 | Observability: Langfuse — tracing an agent, debugging failures |
| 35 | Guardrails & safety: prompt-injection defense, output validation |
| 36 | **Mini-project 3 build day** |
| 37 | **Mini-project 3 deploy + demo** |

**🚀 Project 3 — Personal Research Agent.** Researches a topic across the web, takes notes,
produces a briefing. Student picks the framework (LangGraph / CrewAI / AutoGen). Must use 3+
tools. Traced in Langfuse. Deployed free.

---

## Phase 4 — Capstone + Placement (Days 38–45)
*Goal: ship one portfolio-grade project + get placement-ready.*

| Day | Activity |
|----:|----------|
| 38 | Capstone ideation workshop + scoping |
| 39 | 1:1 architecture review with trainer + project setup |
| 40 | Build sprint — day 1 (daily standups, trainer check-ins) |
| 41 | Build sprint — day 2 |
| 42 | Build sprint — day 3 + deployment (CI/CD basics, env vars, monitoring) |
| 43 | Demo day + peer code review |
| 44 | Resume + LinkedIn + GitHub polish + mock interviews |
| 45 | Portfolio site launch (Vercel) + certificate ceremony |

**🏁 Capstone (student picks one, must be deployed + demoable):**
1. Multi-agent research assistant — topic in, briefing out, with citations
2. WhatsApp AI business assistant — Twilio + Gemini + Supabase
3. AI customer support for a local business — RAG on their FAQ/catalog
4. Code review agent — runs on a GitHub repo, posts PR comments
5. Educational tutor for one subject — adaptive study buddy
6. AI finance tracker — ingests statements, natural-language insights
7. AI recipe generator — dietary-aware, grocery-list output
8. AI news briefing agent — daily personalized digest, scheduled

---

## Deliverables — what every student walks out with
- **4 deployed projects** (3 mini + 1 capstone), all public on GitHub with polished READMEs
- **Portfolio site** on Vercel (free), all projects linked
- **4 demo videos** (~2 min each, Loom/YouTube)
- LinkedIn optimized + project-announcement posts
- Certificate from Softpro School of AI

## The free-tier stack (₹0 infra)
Gemini (primary) · Groq · Ollama (local) · Hugging Face · Chroma / pgvector + Supabase ·
Streamlit / Gradio · Langfuse · GitHub · deployed on HF Spaces / Streamlit Cloud / Render / Vercel.
