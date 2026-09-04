from flask import Blueprint, jsonify

from backend.models.student import Student
from backend.models.job import Job
from backend.services.skill_gap_service import calculate_skill_gaps


skill_gap_bp = Blueprint(
    "skill_gap",
    __name__,
    url_prefix="/api/skill-gap"
)


@skill_gap_bp.get("/<int:student_id>")
def get_skill_gap(student_id):
    student = Student.query.get(student_id)

    if student is None:
        return jsonify({
            "success": False,
            "error": "Student not found"
        }), 404

    jobs = Job.query.all()

    if not jobs:
        return jsonify({
            "success": True,
            "data": []
        }), 200

    job_gaps = []

    for job in jobs:
        gaps = calculate_skill_gaps(
            student.skills or {},
            job.required_skills or {}
        )

        job_gaps.append({
            "job_id": job.id,
            "title": job.title,
            "company": job.company,
            "skill_gaps": gaps
        })

    return jsonify({
        "success": True,
        "data": job_gaps
    }), 200