def generate_explanation(resume_skills, jd_text):
    explanation = ""

    if "Python" not in resume_skills:
        explanation += "Missing Python. "

    if "Machine Learning" in resume_skills:
        explanation += "Strong in ML. "

    return explanation