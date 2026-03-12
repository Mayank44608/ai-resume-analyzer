import re

required_skills = ["python", "sql", "machine learning", "data analysis", "flask"]

def analyze_resume(text):
    found_skills = []

    for skill in required_skills:
        if re.search(skill, text.lower()):
            found_skills.append(skill)

    score = (len(found_skills) / len(required_skills)) * 100

    return found_skills, score


resume_text = """
Python developer with experience in Flask, SQL and data analysis.
"""

skills, score = analyze_resume(resume_text)

print("Skills Found:", skills)
print("Match Score:", score)
