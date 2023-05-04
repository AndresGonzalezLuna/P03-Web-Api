from pydantic import BaseModel

class RequestEvaluation(BaseModel):
    int_rate: float
    out_prncp: float
    total_rec_prncp: float
    last_pymnt_amnt: float
    addr_state: str
    grade: str
    sub_grade: str
    total_pymnt:float

