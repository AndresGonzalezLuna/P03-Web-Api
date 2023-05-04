import pandas as pd
import numpy as np
from typing import List, Dict

class ColumnSelectorTransformer:
    def __init__(self, columns: List[str]):
        self.columns = columns

    def transform(self, X: pd.DataFrame, y: pd.DataFrame = None) -> pd.DataFrame:
        return X.loc[:, self.columns]

    def fit(self, *args, **kwargs):
        return self

    def __str__(self) -> str:
        return f"ColumnSelectorTransformer({self.columns})"

    def __repr__(self) -> str:
        return f"ColumnSelectorTransformer({self.columns})"