from src.parser import parse_resume
from src.embeddings import get_embedding
from src.scorer import compute_similarity

# Sample Resume
resume_text = """
Skills: Python, SQL, Machine Learning
Experience: 2 years Data Analyst
"""

# Job Description
jd_text = "Looking for Python and Machine Learning engineer with SQL experience"

parsed = parse_resume(resume_text)

resume_emb = get_embedding(parsed["skills"])
jd_emb = get_embedding(jd_text)

score = compute_similarity(resume_emb, jd_emb)

print("Match Score:", score)