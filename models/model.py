import pickle
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler as SVC
import pandas as pd
from sklearn.model_selection import train_test_split
from tranformers.ColumnSelectorTransformer import ColumnSelectorTransformer
from tranformers.BinningTransformer import BinningTransformer
from tranformers.WOETransformer import WOETransformer
from sklearn.pipeline import Pipeline
from bins import bins
from sklearn.linear_model import LogisticRegression


DataCredit = pd.read_csv("credit_risk_data_v2.csv",low_memory=False)
# Obtener una lista de las columnas que contienen solo valores en blanco
empty_columns = [col for col in DataCredit.columns if DataCredit[col].isnull().all()]
# Eliminar las columnas que contienen solo valores en blanco
DataCredit.drop(empty_columns, axis=1, inplace=True)
# Se borrran las columnas que son identificadores ya que no nos sirven para nuestros modelos
DataCredit.drop(['id','member_id'],axis=1, inplace=True)
# btener una Serie con la cantidad de valores nulos en cada columna
null_counts = DataCredit.isnull().sum()
# Filtrar las columnas con valores nulos y ordenarlas de manera ascendente
null_cols = null_counts[null_counts > 0].sort_values()
ListColumns = ['loan_amnt','int_rate','installment','emp_length',
               'annual_inc','dti','revol_bal','revol_util','total_acc',
               'total_pymnt','total_rec_prncp','total_rec_int','recoveries',
               'last_pymnt_amnt','grade','term','home_ownership','purpose',
               'pymnt_plan','addr_state','initial_list_status','status']
DataCredit_clean = DataCredit[ListColumns]
X_train = DataCredit.drop('status', axis=1)
Y_train = DataCredit['status']
x_train ,x_test, y_train, y_test = train_test_split(X_train, Y_train, test_size=.30, random_state=42)

cols_to_keep = ['loan_amnt','int_rate','installment',
               'annual_inc','dti','revol_bal','total_acc',
               'grade','term','home_ownership','purpose',
               'pymnt_plan']
seed = 102

ml_pipe = Pipeline([
    ('col selector', ColumnSelectorTransformer(columns=cols_to_keep)),
    ('bins', BinningTransformer(bins=bins)),
    ('woe', WOETransformer(columns=cols_to_keep)),
    ('logistic regression', LogisticRegression(random_state=seed))
    #('gdbt', GradientBoostingClassifier(random_state=seed))
])

with open("./model.pkl","wb") as file:
    pickle.dump(ml_pipe, file)

