import pandas as pd
import random
from faker import Faker

fake = Faker("en_IN")  # Indian names

skills_pool = [
    "python","sql","ml","excel","java","html","css","javascript",
    "communication","sales","negotiation","powerbi","tableau",
    "c","c++","react","nodejs","marketing","seo","finance","excel"
]

def generate_students(n=200):
    students = []
    for i in range(1, n+1):
        students.append({
            "student_id": i,
            "name": fake.name(),
            "age": random.randint(20, 25),
            "gender": random.choice(["M","F"]),
            "category": random.choice(["GEN","OBC","SC","ST"]),
            "district_code": random.choice(["BR01","BR12","BR15","DL01","MH01"]),
            "education": random.choice(["BSc CS","BTech IT","MBA","BA","BCom","Diploma"]),
            "skills": ",".join(random.sample(skills_pool, k=random.randint(2,5))),
            "experience_months": random.randint(0, 24),
            "past_internships": random.randint(0, 2)
        })
    return pd.DataFrame(students)

students_df = generate_students(250)  # generate 250 students
students_df.to_csv("students.csv", index=False)
print("✅ students.csv generated with", len(students_df), "rows")
