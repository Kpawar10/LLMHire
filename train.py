from src.parser import parse_resume
from src.embeddings import get_embedding
from src.scorer import compute_similarity
from src.llm_module import generate_explanation

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# -------------------------
# STEP 1: Input Data
# -------------------------
resume_text = """
Skills: Python, SQL, Machine Learning
Experience: 2 years Data Analyst
"""

jd_text = "Looking for Python and Machine Learning engineer with SQL experience"

# -------------------------
# STEP 2: Parse Resume
# -------------------------
parsed = parse_resume(resume_text)

# -------------------------
# STEP 3: Embeddings
# -------------------------
resume_emb = get_embedding(parsed["skills"])
jd_emb = get_embedding(jd_text)

# -------------------------
# STEP 4: Similarity Score
# -------------------------
score = compute_similarity(resume_emb, jd_emb)

print("Match Score:", score)

# -------------------------
# STEP 5: LLM Explanation
# -------------------------
explanation = generate_explanation(parsed["skills"], jd_text)

print("Explanation:", explanation)

# -------------------------
# STEP 6: Train ML Model
# -------------------------
data = pd.DataFrame({
    "similarity": [0.9, 0.2, 0.75, 0.3],
    "label": [1, 0, 1, 0]
})

X = data[["similarity"]]
y = data["label"]

model = LogisticRegression()
model.fit(X, y)

# -------------------------
# STEP 7: Prediction
# -------------------------
pred = model.predict([[score]])

print("Final Selection:", "Selected" if pred[0] == 1 else "Rejected")

# -------------------------
# STEP 8: Evaluation
# -------------------------
y_pred = model.predict(X)
print("Accuracy:", accuracy_score(y, y_pred))