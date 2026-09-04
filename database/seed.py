import sqlite3
import json
from pathlib import Path


DATABASE_PATH = Path(__file__).resolve().parent.parent / "skillsync.db"


def seed_database():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    # Students
    students = [
        (
            "Ananya",
            "ananya@example.com",
            "demo_hash_1",
            "9876543210",
            "ABC Engineering College",
            "Computer Science",
            2027,
            "Software Developer",
            ["Python", "Flask", "SQL"]
        ),
        (
            "Rahul",
            "rahul@example.com",
            "demo_hash_2",
            "9876543211",
            "XYZ Institute of Technology",
            "Information Technology",
            2026,
            "Data Analyst",
            ["Python", "SQL", "Power BI"]
        )
    ]

    for student in students:
        cursor.execute(
            """
            INSERT OR IGNORE INTO students
            (
                name,
                email,
                password_hash,
                phone,
                institution,
                course,
                graduation_year,
                career_interest,
                skills
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                student[0],
                student[1],
                student[2],
                student[3],
                student[4],
                student[5],
                student[6],
                student[7],
                json.dumps(student[8])
            )
        )

    # Jobs
    jobs = [
        (
            "Python Developer",
            "TechNova",
            "Develop backend applications using Python and Flask.",
            ["Python", "Flask", "SQL"],
            "Hyderabad",
            "Full-time"
        ),
        (
            "Data Analyst",
            "DataWorks",
            "Analyze business data and create useful dashboards.",
            ["Python", "SQL", "Power BI"],
            "Bangalore",
            "Internship"
        )
    ]

    for job in jobs:
        cursor.execute(
            """
            INSERT INTO jobs
            (
                title,
                company,
                description,
                required_skills,
                location,
                type
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                job[0],
                job[1],
                job[2],
                json.dumps(job[3]),
                job[4],
                job[5]
            )
        )

    connection.commit()

    print("Database seed completed successfully.")

    connection.close()


if __name__ == "__main__":
    seed_database()