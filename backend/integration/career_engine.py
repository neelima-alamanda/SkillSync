from __future__ import annotations

from typing import Any

from backend.services.matching_service import calculate_match
from backend.services.skill_gap_service import calculate_skill_gaps


def analyze_career_match(
    student_skills: dict[str, int],
    required_skills: dict[str, int],
) -> dict[str, Any]:
    """
    Run skill-gap analysis and job matching together.
    """

    match_result = calculate_match(
        student_skills,
        required_skills,
    )

    skill_gaps = calculate_skill_gaps(
        student_skills,
        required_skills,
    )

    return {
        "match_score": match_result["match_score"],
        "matched_skills": match_result["matched_skills"],
        "missing_skills": match_result["missing_skills"],
        "skill_gaps": skill_gaps,
    }