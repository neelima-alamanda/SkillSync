from backend.integration.career_analysis import analyze_student_job_match


class MockStudent:
    id = 2
    skills = {
        "Python": 80,
        "Flask": 60,
        "SQL": 70,
    }


class MockJob:
    id = 1
    title = "Python Developer"
    company = "TechNova"
    required_skills = {
        "Python": 70,
        "Flask": 70,
        "SQL": 60,
    }


result = analyze_student_job_match(MockStudent(), MockJob())

print(result)

assert result["student_id"] == 2
assert result["job_id"] == 1
assert result["match_score"] == 95
assert "Flask" in result["missing_skills"]
assert result["skill_gaps"][0]["skill"] == "Flask"

print("PASS: database career integration")