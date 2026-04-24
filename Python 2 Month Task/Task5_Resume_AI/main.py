import os
import pdfplumber
import pandas as pd

# Extract text from PDF
def extract_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()

# Input Job Description
print("Paste Job Description (skills required):")
jd = input().lower()

jd_keywords = [word.strip().lower() for word in jd.replace(",", " ").split()]

folder = "resumes"
results = []

for file in os.listdir(folder):
    if file.endswith(".pdf"):
        path = os.path.join(folder, file)

        text = extract_text(path)

        score = 0
        matched = []

        for word in jd_keywords:
            if word in text:
                score += 1
                matched.append(word)

        results.append({
            "Resume": file,
            "Score": score,
            "Matched Keywords": ", ".join(set(matched))
        })

# Convert to DataFrame
df = pd.DataFrame(results)

# Ranking
df = df.sort_values(by="Score", ascending=False)

# Save report
df.to_csv("final_results.csv", index=False)

print("\nRanking:\n")
print(df)

print("\nBest Candidate:", df.iloc[0]["Resume"])