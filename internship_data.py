import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker("en_IN")

skills_pool = [
    "python","sql","ml","excel","java","html","css","javascript",
    "communication","sales","negotiation","powerbi","tableau",
    "c","c++","react","nodejs","marketing","seo","finance"
]

sectors = ["IT", "Marketing", "Finance", "Sales", "Consulting", "Data Science", "HR"]

def random_date():
    start = datetime(2025, 9, 1)
    end = datetime(2026, 3, 1)
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

def generate_internships(n=120):
    internships = []
    for i in range(1, n+1):
        start_date = random_date()
        end_date = start_date + timedelta(days=random.randint(60, 120))  # 2-4 months
        internships.append({
            "internship_id": i,
            "title": random.choice(["Intern", "Trainee", "Assistant"]) + " " + random.choice(sectors),
            "company": fake.company(),
            "sector": random.choice(sectors),
            "required_skills": ",".join(random.sample(skills_pool, k=random.randint(2,4))),
            "location_city": fake.city(),
            "location_district_code": random.choice(["BR01","BR12","BR15","DL01","MH01"]),
            "remote": random.choice([True, False]),
            "seats": random.randint(2, 10),
            "stipend": random.choice([5000, 7000, 8000, 10000, 12000]),
            "start_date": start_date.date(),
            "end_date": end_date.date()
        })
    return pd.DataFrame(internships)

internships_df = generate_internships(150)  # generate 150 internships
internships_df.to_csv("internships.csv", index=False)
print("✅ internships.csv generated with", len(internships_df), "rows")
