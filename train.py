from src.llm_module import generate_explanation

explanation = generate_explanation(parsed["skills"], jd_text)

print("Explanation:", explanation)