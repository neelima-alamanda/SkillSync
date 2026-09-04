from backend.integration.recommendation_service import get_job_recommendations


class MockStudent:
    id = 2
    skills = {
        "Python": 80,
        "Flask": 60,
        "SQL": 70,
    }


class EmptySkillsStudent:
    id = 3
    skills = None


class PythonJob:
    id = 1
    title = "Python Developer"
    company = "TechNova"
    required_skills = {
        "Python": 70,
        "Flask": 70,
        "SQL": 60,
    }


class DataJob:
    id = 2
    title = "Data Analyst"
    company = "DataWorks"
    required_skills = {
        "Python": 70,
        "SQL": 70,
        "Power BI": 60,
    }


class EmptySkillsJob:
    id = 3
    title = "General Internship"
    company = "TestCompany"
    required_skills = None


student = MockStudent()

# Test normal recommendations
results = get_job_recommendations(
    student,
    [DataJob(), PythonJob()],
)

assert len(results) == 2
assert results[0]["job_id"] == 1
assert results[0]["match_score"] == 95
assert results[1]["job_id"] == 2
assert results[1]["match_score"] == 67

# Test empty job list
empty_results = get_job_recommendations(student, [])
assert empty_results == []

# Test student with no skills
no_skill_results = get_job_recommendations(
    EmptySkillsStudent(),
    [PythonJob()],
)

assert len(no_skill_results) == 1
assert no_skill_results[0]["match_score"] == 0

# Test job with no required skills
empty_job_results = get_job_recommendations(
    student,
    [EmptySkillsJob()],
)

assert len(empty_job_results) == 1
assert empty_job_results[0]["match_score"] == 0

print("PASS: recommendation service edge cases")