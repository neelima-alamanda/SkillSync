from flask import Blueprint, request, jsonify

from backend.models import db
from backend.models.application import Application
from backend.models.student import Student
from backend.models.job import Job


application_bp = Blueprint(
    "application",
    __name__,
    url_prefix="/api/applications"
)


# POST create an application
@application_bp.post("")
def create_application():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "error": "Request body is required"
        }), 400

    student_id = data.get("student_id")
    job_id = data.get("job_id")

    if not student_id or not job_id:
        return jsonify({
            "success": False,
            "error": "student_id and job_id are required"
        }), 400

    student = Student.query.get(student_id)

    if student is None:
        return jsonify({
            "success": False,
            "error": "Student not found"
        }), 404

    job = Job.query.get(job_id)

    if job is None:
        return jsonify({
            "success": False,
            "error": "Job not found"
        }), 404

    application = Application(
        student_id=student_id,
        job_id=job_id,
        status="applied"
    )

    db.session.add(application)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Application submitted successfully",
        "data": application.to_dict()
    }), 201


# GET application by ID
@application_bp.get("/<int:application_id>")
def get_application(application_id):
    application = Application.query.get(application_id)

    if application is None:
        return jsonify({
            "success": False,
            "error": "Application not found"
        }), 404

    return jsonify({
        "success": True,
        "data": application.to_dict()
    }), 200


# GET applications for a student
@application_bp.get("/student/<int:student_id>")
def get_student_applications(student_id):
    student = Student.query.get(student_id)

    if student is None:
        return jsonify({
            "success": False,
            "error": "Student not found"
        }), 404

    applications = Application.query.filter_by(
        student_id=student_id
    ).all()

    return jsonify({
        "success": True,
        "data": [
            application.to_dict()
            for application in applications
        ]
    }), 200


# PUT update application status
@application_bp.put("/<int:application_id>")
def update_application(application_id):
    application = Application.query.get(application_id)

    if application is None:
        return jsonify({
            "success": False,
            "error": "Application not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "error": "Request body is required"
        }), 400

    if "status" not in data:
        return jsonify({
            "success": False,
            "error": "Status is required"
        }), 400

    application.status = data["status"]

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Application status updated successfully",
        "data": application.to_dict()
    }), 200