from __future__ import annotations

from typing import Any


def calculate_skill_gaps(
    student_skills: dict[str, int],
    required_skills: dict[str, int],
) -> list[dict[str, Any]]:
    """
    Calculate missing skill levels between a student's current
    proficiency and the required proficiency for a target.

    Args:
        student_skills: Mapping of skill names to current scores (0-100).
        required_skills: Mapping of skill names to required scores (0-100).

    Returns:
        A list of skill-gap records sorted by largest gap first.
    """
    gaps: list[dict[str, Any]] = []

    for skill, required_score in required_skills.items():
        current_score = student_skills.get(skill, 0)

        gap = max(required_score - current_score, 0)

        if gap > 0:
            gaps.append(
                {
                    "skill": skill,
                    "current": current_score,
                    "required": required_score,
                    "gap": gap,
                }
            )

    return sorted(gaps, key=lambda item: item["gap"], reverse=True)