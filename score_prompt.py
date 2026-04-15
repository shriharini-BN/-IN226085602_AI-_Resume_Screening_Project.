from langchain_core.prompts import PromptTemplate
score_prompt = PromptTemplate.from_template("""
Give a score between 0 to 100.

Matching Data:
{match_data}
Rules:
- More matching skills → higher score
- Missing important skills → reduce score
- No explanation

Return ONLY JSON:
{{
  "score": number
}}
""")