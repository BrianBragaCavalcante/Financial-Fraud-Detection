from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import pickle

def import_model() -> DecisionTreeClassifier:
    try:
        with open('./model/model.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        raise('Run model.ipynb or create_model.py for create and use the model')

def process_data(table: pd.DataFrame):
    table = table.drop(columns=['nameOrig', 'nameDest'])
    table['step'] = table['step'] % 24

    try:
        with open('./model/encoder.pkl', 'rb') as file:
            encoder: LabelEncoder = pickle.load(file)

        table['type'] = encoder.fit_transform(table['type'])

    except FileNotFoundError:
        raise('Run model.ipynb or create_model.py for create and use the model')

    return table, table.drop(columns='isFraud'), table['isFraud']

