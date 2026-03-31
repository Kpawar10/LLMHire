import streamlit as st
from src.parser import parse_resume
from src.embeddings import get_embedding
from src.scorer import compute_similarity
from src.llm_module import generate_explanation

st.title("AI Resume Screener")

resume = st.text_area("Paste Resume")
jd = st.text_area("Paste Job Description")

if st.button("Evaluate"):
    parsed = parse_resume(resume)

    resume_emb = get_embedding(parsed["skills"])
    jd_emb = get_embedding(jd)

    score = compute_similarity(resume_emb, jd_emb)
    explanation = generate_explanation(parsed["skills"], jd)

    st.write("Match Score:", score)
    st.write("Explanation:", explanation)