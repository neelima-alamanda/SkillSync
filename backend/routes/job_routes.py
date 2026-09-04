from flask import Blueprint, request, jsonify

from backend.models import db
from backend.models.job import Job


job_bp = Blueprint(
    "job",
    __name__,
    url_prefix="/api/jobs"
)


# GET all jobs
@job_bp.get("")
def get_jobs():
    jobs = Job.query.all()

    return jsonify({
        "success": True,
        "data": [job.to_dict() for job in jobs]
    }), 200


# GET job by ID
@job_bp.get("/<int:job_id>")
def get_job(job_id):
    job = Job.query.get(job_id)

    if job is None:
        return jsonify({
            "success": False,
            "error": "Job not found"
        }), 404

    return jsonify({
        "success": True,
        "data": job.to_dict()
    }), 200


# POST create a job
@job_bp.post("")
def create_job():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "error": "Request body is required"
        }), 400

    title = data.get("title")
    company = data.get("company")

    if not title or not company:
        return jsonify({
            "success": False,
            "error": "Title and company are required"
        }), 400

    job = Job(
        title=title,
        company=company,
        description=data.get("description"),
        required_skills=data.get("required_skills", {}),
        location=data.get("location"),
        type=data.get("type")
    )

    db.session.add(job)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Job created successfully",
        "data": job.to_dict()
    }), 201


# PUT update a job
@job_bp.put("/<int:job_id>")
def update_job(job_id):
    job = Job.query.get(job_id)

    if job is None:
        return jsonify({
            "success": False,
            "error": "Job not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "error": "Request body is required"
        }), 400

    if "title" in data:
        job.title = data["title"]

    if "company" in data:
        job.company = data["company"]

    if "description" in data:
        job.description = data["description"]

    if "required_skills" in data:
        job.required_skills = data["required_skills"]

    if "location" in data:
        job.location = data["location"]

    if "type" in data:
        job.type = data["type"]

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Job updated successfully",
        "data": job.to_dict()
    }), 200


# DELETE a job
@job_bp.delete("/<int:job_id>")
def delete_job(job_id):
    job = Job.query.get(job_id)

    if job is None:
        return jsonify({
            "success": False,
            "error": "Job not found"
        }), 404

    db.session.delete(job)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Job deleted successfully"
    }), 200
