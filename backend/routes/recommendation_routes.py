from flask import Blueprint, jsonify

from backend.models.student import Student
from backend.models.job import Job
from backend.integration.recommendation_service import get_job_recommendations


recommendation_bp = Blueprint(
    "recommendation",
    __name__,
    url_prefix="/api/recommendations"
)


@recommendation_bp.get("/<int:student_id>")
def get_recommendations(student_id):
    student = Student.query.get(student_id)

    if student is None:
        return jsonify({
            "success": False,
            "error": "Student not found"
        }), 404

    jobs = Job.query.all()

    recommendations = get_job_recommendations(
        student,
        jobs
    )

    return jsonify({
        "success": True,
        "data": recommendations
    }), 200