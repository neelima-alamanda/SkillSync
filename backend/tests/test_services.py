from backend.services.matching_service import calculate_match


# Edge case: no required skills
result = calculate_match(
    {"Python": 80},
    {},
)

assert result["match_score"] == 0
assert result["matched_skills"] == []
assert result["missing_skills"] == []


# Edge case: student has none of the required skills
result = calculate_match(
    {},
    {"Python": 70, "SQL": 60},
)

assert result["match_score"] == 0
assert result["matched_skills"] == []
assert result["missing_skills"] == ["Python", "SQL"]


# Edge case: student exceeds required skill level
result = calculate_match(
    {"Python": 100},
    {"Python": 70},
)

assert result["match_score"] == 100
assert result["matched_skills"] == ["Python"]

print("PASS: matching service edge cases")