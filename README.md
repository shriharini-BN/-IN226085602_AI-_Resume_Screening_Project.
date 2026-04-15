# AI-Powered Resume Screening System

## 📌 Project Overview
This project is an AI-based Resume Screening System built using Python, LangChain, Groq API, and LangSmith. It helps recruiters automatically evaluate resumes against a job description by extracting candidate skills, matching them with requirements, assigning a score, and generating explanations.

## 🎯 Objective
- Automate resume screening process
- Compare resumes with job descriptions
- Provide candidate fit score (0–100)
- Generate explainable results
- Use LangSmith for tracing and debugging

---

## 🛠️ Technologies Used
- Python
- LangChain
- Groq API
- LangSmith
- VS Code
- dotenv

---

## 📂 Project Structure

```bash
AI-powered Resume Screening System/
│── main.py
│── .env
│── job_description.txt
│── prompts/
│   ├── extract_prompt.py
│   ├── match_prompt.py
│   ├── score_prompt.py
│   └── explain_prompt.py
│── chains/
│   ├── extraction_chain.py
│   ├── matching_chain.py
│   ├── scoring_chain.py
│   └── explanation_chain.py
│── resumes/
│   ├── strong.txt
│   ├── average.txt
│   └── weak.txt


⚙️ Workflow

Plain text
Resume → Skill Extraction → Matching → Scoring → Explanation
Step 1: Skill Extraction
Extracts:
Skills
Experience
Tools
Step 2: Matching
Compares resume details with job description.
Step 3: Scoring
Assigns a score between 0–100.
Step 4: Explanation
Explains why the score was assigned.

🔐 Environment Variables

Create a .env file:
Environment
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=resume-screening

▶️ Installation

Bash
pip install langchain
pip install langchain-groq
pip install python-dotenv

▶️ Run Project

Bash
python main.py
📊 Sample Output
Plain text
===== Running for strong.txt =====

Extracted:
Skills: Python, SQL, Machine Learning

Match:
Strong skill match with job role

Score:
92

Explanation:

Candidate has strong technical skills and relevant experience.
📈 LangSmith Tracing

Used LangSmith for:
Pipeline tracing
Monitoring runs
Error debugging

Performance analysis

🐞 Debugging Example
Issue: Deprecated model error from Groq.
Fix: Updated model name to supported version.
✅ Features
AI Resume Screening
Candidate Ranking
Explainable AI Output
Tracing & Debugging
Modular Code Structure

🚀 Future Enhancements

Upload PDF Resume
Web Interface using Streamlit
Store results in database
Rank multiple candidates automatically
