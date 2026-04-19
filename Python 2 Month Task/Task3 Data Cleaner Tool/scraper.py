import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

jobs = []
for job in soup.find_all("div", class_="card-content"):
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    jobs.append({"title": title, "company": company, "location": location})

df = pd.DataFrame(jobs)
df = df.drop_duplicates()
df = df.dropna()

df.to_csv("output.csv", index=False)

print(" Job data scraped & cleaned successfully!")

