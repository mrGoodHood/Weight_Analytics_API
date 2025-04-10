from sqlalchemy.orm import Session
from sqlalchemy import text
from .models import RespondentData

def get_avg_weight_by_respondent(session: Session, condition: str) -> dict[int, float]:
    query = text(f"""
        SELECT respondent, AVG(weight) as avg_weight
        FROM respondents
        WHERE {condition}
        GROUP BY respondent
    """)
    result = session.execute(query)
    return {row[0]: row[1] for row in result}

def calculate_percent(aud1: dict[int, float], aud2: dict[int, float]) -> float:
    common = set(aud1.keys()) & set(aud2.keys())
    numerator = sum(aud2[r] for r in common)
    denominator = sum(aud1.values())
    if denominator == 0:
        return 0.0
    return round(numerator / denominator, 5)
