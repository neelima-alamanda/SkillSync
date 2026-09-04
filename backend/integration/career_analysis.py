from typing import Any

from backend.integration.career_engine import analyze_career_match
from backend.models.job import Job
from backend.models.student import Student


def analyze_student_job_match(
    student: Student,
    job: Job,
) -> dict[str, Any]:
    student_skills = student.skills or {}
    required_skills = job.required_skills or {}

    result = analyze_career_match(
        student_skills=student_skills,
        required_skills=required_skills,
    )

    return {
        "student_id": student.id,
        "job_id": job.id,
        "job_title": job.title,
        "company": job.company,
        **result,
    }