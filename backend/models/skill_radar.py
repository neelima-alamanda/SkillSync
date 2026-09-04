from backend.models import db


class SkillRadar(db.Model):
    __tablename__ = "skill_radar"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )

    skill = db.Column(
        db.String(100),
        nullable=False
    )

    score = db.Column(
        db.Integer,
        nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "skill": self.skill,
            "score": self.score
        }
    