from backend.models import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    phone = db.Column(db.String(20))
    institution = db.Column(db.String(200))
    course = db.Column(db.String(100))
    graduation_year = db.Column(db.Integer)
    career_interest = db.Column(db.String(200))
    skills = db.Column(db.JSON)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "institution": self.institution,
            "course": self.course,
            "graduation_year": self.graduation_year,
            "career_interest": self.career_interest,
            "skills": self.skills or {}
        }