from fastapi import FastAPI, Query
from app.db import SessionLocal
from app.utils import get_avg_weight_by_respondent, calculate_percent

app = FastAPI()

@app.get("/getPercent")
def get_percent(audience1: str = Query(...), audience2: str = Query(...)):
    db = SessionLocal()
    try:
        aud1 = get_avg_weight_by_respondent(db, audience1)
        aud2 = get_avg_weight_by_respondent(db, audience2)
        percent = calculate_percent(aud1, aud2)
        return {"percent": percent}
    except Exception as e:
        return {"error": str(e)}
    finally:
        db.close()
