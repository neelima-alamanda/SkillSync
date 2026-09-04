from __future__ import annotations

from typing import Any


def calculate_match(
    student_skills: dict[str, int],
    required_skills: dict[str, int],
) -> dict[str, Any]:
    """
    Calculate a student's match score against a job's required skills.

    Each skill contributes a maximum of 100%.
    Missing skills contribute 0%.
    """

    if not required_skills:
        return {
            "match_score": 0,
            "matched_skills": [],
            "missing_skills": [],
        }

    matched_skills: list[str] = []
    missing_skills: list[str] = []
    skill_scores: list[float] = []

    for skill, required_score in required_skills.items():
        current_score = student_skills.get(skill, 0)

        if required_score <= 0:
            contribution = 100.0
        else:
            contribution = min(
                (current_score / required_score) * 100,
                100,
            )

        skill_scores.append(contribution)

        if current_score >= required_score:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    match_score = round(sum(skill_scores) / len(skill_scores))

    return {
        "match_score": match_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }