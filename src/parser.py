import re

def parse_resume(text):
    skills = re.findall(r"Skills:(.*)", text)
    experience = re.findall(r"Experience:(.*)", text)

    return {
        "skills": skills[0].strip() if skills else "",
        "experience": experience[0].strip() if experience else ""
    }