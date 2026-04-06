from sklearn.metrics.pairwise import cosine_similarity

skills_list = [
    "python", "machine learning", "deep learning", "sql",
    "nlp", "data analysis", "pandas", "numpy", "tensorflow"
]

def extract_skills(text):
    text = text.lower()
    return [skill for skill in skills_list if skill in text]

def compute_similarity(emb1, emb2):
    return cosine_similarity(emb1, emb2)[0][0]

def generate_feedback(score, matched, missing):
    if score > 0.75:
        level = "Excellent Match"
    elif score > 0.6:
        level = "Good Match"
    else:
        level = "Low Match"

    feedback = f"""
    Match Level: {level}

    Matched Skills: {', '.join(matched) if matched else 'None'}

    Missing Skills: {', '.join(missing) if missing else 'None'}

    Suggestions:
    """
    
    if missing:
        feedback += f"Consider learning: {', '.join(missing)}"
    else:
        feedback += "You meet all key requirements!"

    return feedback 