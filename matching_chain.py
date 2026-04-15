from langchain_groq import ChatGroq
from prompts.match_prompt import match_prompt
import os

def get_llm():
    models = [
        "llama-3.1-8b-instant",
        "gemma-7b-it",
        "llama3-8b-8192"
    ]
    
    for m in models:
        try:
            return ChatGroq(
                model=m,
                api_key=os.getenv("GROQ_API_KEY")
            )
        except:
            continue

    raise ValueError("No working Groq model found")

llm = get_llm()

matching_chain = match_prompt | llm