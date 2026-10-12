# 🤖 AI Job Matcher Agent

An automated job search pipeline that fetches listings matching custom target roles, evaluates postings against a candidate background profile using Large Language Models (LLM), and logs structured match scores and skill gap analyses to a local database.

---

## 🎯 Key Features

* **Multi-Role Job Scraping:** Queries live job listings using SerpAPI (Google Jobs API).
* **Automated Candidate Evaluation:** Utilizes LLM orchestration (LangChain with Groq / Gemini) to score candidate fit on a 0–100 scale.
* **Structured JSON Insights:** Extracts matching technical skills, missing qualifications/gaps, fit summaries, and application recommendations (`Apply Immediately`, `Consider`, or `Skip`).
* **Local Data Persistence:** Automatically writes evaluated postings into a local **DuckDB** database for easy querying and reporting.

---

## 🏗️ Architecture & Project Structure

├── main.py                # Pipeline orchestrator
├── job_fetcher.py         # Job posting ingestion via SerpAPI
├── eval_prompt.py         # Structured output schema (Pydantic) & LLM instantiation
├── job_matching.py        # Core prompt execution & matching logic
├── storage_automation.py  # DuckDB table creation & data insertion
├── profile.json           # Candidate experience, skills, and target parameters
└── .env                   # Environment variable secrets (API Keys)

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **LLM Orchestration:** LangChain, Pydantic
* **LLM Providers:** Groq (`llama-3.1-8b-instant`) / Google AI Studio (`gemini-2.0-flash`)
* **Job Search API:** SerpAPI (Google Jobs)
* **Storage & Analytics:** DuckDB, Pandas

---

## 🚀 Quickstart Guide

## 1. Clone the Repository

```
git clone [https://github.com/YOUR_GITHUB_USERNAME/jobAgent.git](https://github.com/YOUR_GITHUB_USERNAME/jobAgent.git)
cd jobAgent

```

## 2. Set Up Virtual Environment & Install Dependencies

```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install requests python-dotenv langchain-core langchain-groq duckdb pandas pydantic

```
## 3. Configure Environment Variables
Create a .env file in the project root:

```

SERPAPI_API_KEY=your_serpapi_key_here
GROQ_API_KEY=your_groq_api_key_here

```
## 4. Run the Pipeline
```
python main.py

```
📊 Viewing Stored Results
To view matches directly from your local DuckDB database using Python:

```
import duckdb
import pandas as pd

con = duckdb.connect("job_matches.db")
df = con.execute("SELECT job_title, company_name, match_score, recommendation FROM matches ORDER BY match_score DESC").df()
print(df)
con.close()

```

---

### Quick GitHub Repository Setup Checklist
1. **Repository Description (GitHub About Box):**
   > *An automated AI agent built with LangChain, Groq/Gemini, and DuckDB to fetch, score, and store job listings matching candidate backgrounds.*
2. **Topics/Tags:** `python`, `langchain`, `llm`, `groq`, `duckdb`, `job-search`, `ai-agent`
3. **`.gitignore` Check:** Ensure your `.gitignore` file includes `.env` and `job_matches.db` so API keys and local data files are not pushed to GitHub!
