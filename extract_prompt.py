from langchain_core.prompts import PromptTemplate
extract_prompt = PromptTemplate.from_template("""
You are an AI resume parser.

Extract ONLY from the resume:
- Skills
- Experience (in years if available)
- Tools

Resume:
{resume}
Rules:
- Do NOT assume anything
- Do NOT add extra info
- Return ONLY valid JSON
Format:
{{
  "skills": [],
  "experience": "",
  "tools": []
}}
""")