from langchain_core.prompts import PromptTemplate
explain_prompt = PromptTemplate.from_template("""
Explain the score clearly.

Score:
{score}

Match Data:
{match_data}

Rules:
- Mention strengths
- Mention missing skills
- Keep simple English

Answer:
""")