from flask import Blueprint, jsonify

from backend.models.student import Student


student_bp = Blueprint(
    "student",
    __name__,
    url_prefix="/api/students"
)


@student_bp.get("/<int:student_id>")
def get_student(student_id):
    student = Student.query.get(student_id)

    if student is None:
        return jsonify({
            "success": False,
            "error": "Student not found"
        }), 404

    return jsonify({
        "success": True,
        "data": student.to_dict()
    }), 200