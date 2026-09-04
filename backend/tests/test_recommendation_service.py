from backend.integration.recommendation_service import get_job_recommendations


class MockStudent:
    id = 2
    skills = {
        "Python": 80,
        "Flask": 60,
        "SQL": 70,
    }


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


student = MockStudent()

results = get_job_recommendations(
    student,
    [DataJob(), PythonJob()],
)

print(results)

assert len(results) == 2
assert results[0]["match_score"] >= results[1]["match_score"]
assert results[0]["job_id"] == 1
assert results[1]["job_id"] == 2

print("PASS: recommendation service")