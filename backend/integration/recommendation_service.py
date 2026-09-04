from typing import Any

from backend.integration.career_analysis import analyze_student_job_match
from backend.models.job import Job
from backend.models.student import Student


def get_job_recommendations(
    student: Student,
    jobs: list[Job],
) -> list[dict[str, Any]]:
    recommendations = []

    for job in jobs:
        result = analyze_student_job_match(student, job)

        recommendations.append({
            "job_id": result["job_id"],
            "title": result["job_title"],
            "company": result["company"],
            "match_score": result["match_score"],
            "matched_skills": result["matched_skills"],
            "missing_skills": result["missing_skills"],
        })

    recommendations.sort(
        key=lambda item: item["match_score"],
        reverse=True,
    )

    return recommendations