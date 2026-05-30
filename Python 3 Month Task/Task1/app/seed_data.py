from .database import SessionLocal
from .models import FAQ

db = SessionLocal()

faq_items = [
    {
        "keyword": "python internship",
        "response": "Our Python internship covers APIs, AI tools, and backend projects."
    },
    {
        "keyword": "courses",
        "response": "We offer Python, AI, Web Development, and Data Analytics."
    },
    {
        "keyword": "duration",
        "response": "Internship duration is 2 to 3 months."
    },
    {
        "keyword": "fees",
        "response": "Fees vary depending on the selected course."
    }
]

for item in faq_items:

    existing = db.query(FAQ).filter(
        FAQ.keyword == item["keyword"]
    ).first()

    if not existing:

        faq = FAQ(
            keyword=item["keyword"],
            response=item["response"]
        )

        db.add(faq)

db.commit()
db.close()

print("FAQ data inserted successfully.")