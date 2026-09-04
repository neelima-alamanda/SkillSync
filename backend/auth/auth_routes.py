from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from backend.models import db
from backend.models.student import Student


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({
            "message": "All fields are required"
        }), 400

    existing_student = Student.query.filter_by(email=email).first()

    if existing_student:
        return jsonify({
            "message": "Email already registered"
        }), 409

    password_hash = generate_password_hash(password)

    student = Student(
        name=name,
        email=email,
        password_hash=password_hash
    )

    db.session.add(student)
    db.session.commit()

    return jsonify({
        "message": "Student registered successfully",
        "student": student.to_dict()
    }), 201
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "message": "Email and password are required"
        }), 400

    student = Student.query.filter_by(email=email).first()

    if not student:
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    if not check_password_hash(student.password_hash, password):
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    return jsonify({
        "message": "Login successful",
        "student": student.to_dict()
    }), 200