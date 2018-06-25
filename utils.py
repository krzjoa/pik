import pandas as pd

def make_submission(ids, predictions):
    df = pd.concat([ids, pd.Series(predictions)], axis=1)
    return df.rename(columns={0: 'value'})

from catboost import CatBoostRegressor, CatBoost


