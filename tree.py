import numpy as np
import pandas as pd

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import preprocessing

all_train_data = pd.read_csv('lending_train.csv', delimiter=',', header='infer', quotechar="\"", comment=None)
test_data = pd.read_csv('lending_topredict.csv', delimiter=',', header='infer', quotechar="\"", comment=None)

all_train_data = all_train_data.fillna(0)
test_data = test_data.fillna(0)

def fun(x):
    if isinstance(x, int):
        return x

    x = x.replace('+' , ' ')

    x = [int(s) for s in x.split() if s.isdigit()]
    if len(x) == 0:
        return 0
    return x[0]

all_train_data['loan_duration'] = all_train_data['loan_duration'].map(lambda x: int(x.split(" ")[1]))
test_data['loan_duration'] = test_data['loan_duration'].map(lambda x: int(x.split(" ")[1]))

all_train_data['employment_length'] = all_train_data['employment_length'].map(lambda x: fun(x))
test_data['employment_length'] = test_data['employment_length'].map(lambda x: fun(x))

dont_want = ['employment', 'race', 'reason_for_loan', 'extended_reason']
non_cat = ['employment', 'race', 'reason_for_loan', 'extended_reason', 
'employment_verified', 'zipcode', 'state', 'home_ownership_status', 'type_of_application', 'ID']

test_data_IDs = test_data['ID']

all_train_data = all_train_data.drop(columns=non_cat)
test_data = test_data.drop(columns=non_cat)
test_data = test_data.drop(columns=['loan_paid'])

# DO BALANCE


one = all_train_data.groupby('loan_paid').get_group(1)
zero = all_train_data.groupby('loan_paid').get_group(0)
all_train_data = pd.concat([zero, one, zero, zero])

# train_data = all_train_data.sample(frac = 0.8)
# val_data = all_train_data.drop(index = train_data.index)

X_train, X_test, y_train, y_test = train_test_split(all_train_data.drop('loan_paid', axis=1), all_train_data['loan_paid'], test_size=0.2)

# scaler = preprocessing.StandardScaler().fit(X_train)
# X_train_transformed = scaler.transform(X_train)
# X_test_transformed = scaler.transform(X_test)

gbc = GradientBoostingClassifier(n_estimators=500, learning_rate=0.05, random_state=100, max_features=5)

gbc.fit(X_train, y_train)

# print((gbc.predict(X_test)))

to_print = pd.DataFrame()
to_print['ID'] = test_data_IDs
to_print['loan_paid'] = gbc.predict(test_data)

to_print.to_csv("Tree.csv", index=False)

# print("GBC accuracy is %2.2f" % accuracy_score(y_test, gbc.predict(X_test)))

