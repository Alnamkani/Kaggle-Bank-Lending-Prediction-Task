import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


train_data = pd.read_csv('lending_train.csv', delimiter=',', header='infer', quotechar="\"", comment=None)

test_data = pd.read_csv('lending_topredict.csv', delimiter=',', header='infer', quotechar="\"", comment=None)
print((train_data['race'].value_counts()))

# train_data.boxplot(column=['annual_income'], by='loan_paid')

# train_data = train_data.fillna(0)

# # print(train_data['loan_duration'])

# def fun(x):
#     if isinstance(x, int):
#         return x

#     x = x.replace('+' , ' ')

#     x = [int(s) for s in x.split() if s.isdigit()]
#     if len(x) == 0:
#         return 0
#     return x[0]

# train_data['employment_length'] = train_data['employment_length'].map(lambda x: fun(x))

# print(train_data.describe())


# #corr_matrix_train = train_data.corr(method='pearson')
# #print(corr_matrix_train['loan_paid'])

# # dont_want = ['employment', 'race', 'reason_for_loan', 'extended_reason']