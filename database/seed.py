import sqlite3
import json
from pathlib import Path

DATABASE_PATH = Path(__file__).resolve().parent.parent / "instance" / "skillsync.db"


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
            {"Python": 80, "Flask": 60, "SQL": 70}
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
            {"Python": 80, "SQL": 70, "Power BI": 65}
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
            {"Python": 70, "Flask": 60, "SQL": 50},
            "Hyderabad",
            "Full-time"
        ),
        (
            "Data Analyst",
            "DataWorks",
            "Analyze business data and create useful dashboards.",
            {"Python": 80, "SQL": 70, "Power BI": 65},
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