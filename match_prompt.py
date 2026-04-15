from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate.from_template("""
Compare resume with job description.

Resume Data:
{resume_data}

Job Description:
{job_description}

Rules:
- Do NOT assume missing skills
- Only match exact or close skills

Return ONLY JSON:
{{
  "matching_skills": [],
  "missing_skills": []
}}
""")