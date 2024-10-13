import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

table = pd.read_csv('./database/database.csv')
table = table.drop(columns=['nameOrig', 'nameDest'])
table['step'] = table['step'] % 24

encoder = LabelEncoder()

table['type'] = encoder.fit_transform(table['type'])

x = table.drop(columns='isFraud')
y = table['isFraud']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

model = DecisionTreeClassifier()

model.fit(x_train, y_train)

predict = model.predict(x_test)

print(f'Modelo: {round(accuracy_score(y_test, predict) * 100, 2)}% de precisão.')

with open('model/model.pkl', 'wb') as file:
    pickle.dump(model, file)

with open('model/encoder.pkl', 'wb') as file:
    pickle.dump(encoder, file)
