from fastapi import FastAPI
from app.models import RequestEvaluation
import pandas as pd


app = FastAPI()

@app.get("/heath")
def health_check():
    return {"is_alive": True}


@app.post("/evaluate")
async def evaluate(req: RequestEvaluation):
    print(req)

    df = pd.DataFrame({
        "int_rate": [req.int_rate],
        "out_prncp":[req.out_prncp],
        "total_rec_prncp":[req.total_rec_prncp],
        "last_pymnt_amnt":[req.last_pymnt_amnt],
        "addr_state":[req.addr_state],
        "grade":[req.grade],
        "sub_grade":[req.sub_grade],
        "total_pymnt":[req.total_pymnt]
    })
    print(df)