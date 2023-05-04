from utils import load_ml_model
import pandas as pd
from app.models import  RequestEvaluation
model = load_ml_model.load_ml_model("./model.pkl")
from utils import amortization as Amortization
print(model)

async def evaluate(req: RequestEvaluation):
    print(req)
    df = pd.DataFrame({
        "int_rate": [req.int_rate],
        "out_prncp": [req.out_prncp],
        "total_rec_prncp": [req.total_rec_prncp],
        "last_pymnt_amnt": [req.last_pymnt_amnt],
        "addr_state": [req.addr_state],
        "grade": [req.grade],
        "sub_grade": [req.sub_grade],
        "total_pymnt": [req.total_pymnt]
    })
    pred = model.predict_proba(df)[0]
    default_prob = pred[1]
    print(default_prob)

    amort = Amortization(100_000,0.5,12,default_prob)
    opt_Rate = Amortization.optimize_expected_irr(0,amort)

    return{
        "pd": f"{default_prob*100:.2f}%",
        "interest_rate": f"{opt_Rate:.4f}%"
    }

