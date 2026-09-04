from backend.services.matching_service import calculate_match
from backend.services.skill_gap_service import calculate_skill_gaps
from backend.integration.career_engine import analyze_career_match


def test_matching():
    student_skills = {
        "Python": 80,
        "SQL": 60,
        "Flask": 30,
    }

    required_skills = {
        "Python": 70,
        "SQL": 60,
        "Flask": 50,
    }

    result = calculate_match(student_skills, required_skills)

    assert result["match_score"] == 87
    assert result["matched_skills"] == ["Python", "SQL"]
    assert result["missing_skills"] == ["Flask"]

    print("PASS: matching service")


def test_skill_gap():
    student_skills = {
        "Python": 80,
        "SQL": 60,
        "Flask": 30,
    }

    required_skills = {
        "Python": 70,
        "SQL": 60,
        "Flask": 50,
    }

    result = calculate_skill_gaps(
        student_skills,
        required_skills,
    )

    assert result == [
        {
            "skill": "Flask",
            "current": 30,
            "required": 50,
            "gap": 20,
        }
    ]

    print("PASS: skill gap service")


def test_career_engine():
    student_skills = {
        "Python": 80,
        "SQL": 60,
        "Flask": 30,
    }

    required_skills = {
        "Python": 70,
        "SQL": 60,
        "Flask": 50,
    }

    result = analyze_career_match(
        student_skills,
        required_skills,
    )

    assert result["match_score"] == 87
    assert result["matched_skills"] == ["Python", "SQL"]
    assert result["missing_skills"] == ["Flask"]
    assert result["skill_gaps"][0]["gap"] == 20

    print("PASS: career engine")


if __name__ == "__main__":
    test_matching()
    test_skill_gap()
    test_career_engine()

    print("\nAll backend core tests passed.")