from model import import_model, process_data
import pandas as pd

table = pd.read_csv('./database/database.csv')

table, x, y = process_data(table)

model = import_model()

predict = model.predict(x)

print(predict)
