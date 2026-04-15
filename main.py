import os
from dotenv import load_dotenv

# Force load env file
load_dotenv(dotenv_path=".env", override=True)

# Debug check
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("❌ GROQ API KEY NOT LOADED")

print("✅ API Loaded Successfully")
from chains.extraction_chain import extraction_chain
from chains.matching_chain import matching_chain
from chains.scoring_chain import scoring_chain
from chains.explanation_chain import explanation_chain

# Load Job Description
with open("job_description.txt") as f:
    job_description = f.read()

files = ["strong.txt", "average.txt", "weak.txt"]

for file in files:
    print(f"\n===== Running for {file} =====")

    with open(f"resumes/{file}") as f:
        resume = f.read()

    # Step 1: Extraction
    resume_data = extraction_chain.invoke(
        {"resume": resume},
        config={"tags": ["extraction"]}
    )
    print("\nExtracted:", resume_data.content)

    # Step 2: Matching
    match_data = matching_chain.invoke(
        {
            "resume_data": resume_data.content,
            "job_description": job_description
        },
        config={"tags": ["matching"]}
    )
    print("\nMatch:", match_data.content)

    # Step 3: Scoring
    score = scoring_chain.invoke(
        {"match_data": match_data.content},
        config={"tags": ["scoring"]}
    )
    print("\nScore:", score.content)

    # Step 4: Explanation
    explanation = explanation_chain.invoke(
        {
            "score": score.content,
            "match_data": match_data.content
        },
        config={"tags": ["explanation"]}
    )
    print("\nExplanation:", explanation.content)