import numpy as np
import pandas as pd

train_data = pd.read_csv('lending_train.csv', delimiter=',', header='infer', quotechar="\"", comment=None)

test_data = pd.read_csv('lending_topredict.csv', delimiter=',', header='infer', quotechar="\"", comment=None)

#calculate prior
prior = train_data.groupby('loan_paid').size().div(len(train_data))

want = ['fico_score_range_low', 'fico_score_range_high']


def make_inetvals(column_name, five=None):
    if five == None:
        five = np.percentile(train_data[column_name], [25, 50, 75])
        np.append(five, float('inf'))
        np.insert(five, 0, -1)
    
    temp_data = []
    i = 1
    for index in range(0, len(five) - 1):
        temp_data.append([five[index] + 1, five[index + 1], str(i)])
        i += 1

    intervals = pd.DataFrame(columns = ['From','To','Value'],
    data = temp_data)

    intervals = intervals.set_index(pd.IntervalIndex.from_arrays(intervals['From'], intervals['To']))['Value']

    test_data[column_name] = test_data[column_name].map(intervals)
    train_data[column_name] = train_data[column_name].map(intervals)

for i in want:
    make_inetvals(i)

make_inetvals('requested_amnt', [-1, 5000, 10000, 15000, 25000, float('inf')])
make_inetvals('annual_income', [-1, 20000, 45000, 140000, float('inf')])
#make_inetvals('revolving_balance', [-1, 5000, 10000, 25000, 50000,float('inf')])

feat_weight = {}

for feat in train_data.columns:
    if feat in want:
        feat_weight[feat] = train_data.groupby(['loan_paid', feat]).size().div(len(train_data)).div(prior)

majority_true = {}
majority_false = {}

for feat in train_data.columns:
    if feat in want:
        instnace_true = feat_weight[feat][1].idxmax()
        instnace_false = feat_weight[feat][0].idxmax()
        majority_true[feat] = instnace_true
        majority_false[feat] = instnace_false

def predec(row):
    P_yes = prior[1]
    P_no = prior[0]

    for feat in test_data.columns:
        if feat not in want:
            continue
        third_true = row[feat]
        third_false = row[feat]

        if pd.isna(third_true):
            third_true = majority_true[feat]
            third_false = majority_false[feat]
        try:
            P_yes *= feat_weight[feat][1][third_true]
            P_no *= feat_weight[feat][0][third_false]
        except:
            print("$$$$$$$$$$")
            print(feat)
            print(feat_weight[feat][1])
            print(third_true, third_false)
            print(majority_false[feat], majority_true[feat])
            continue
            #exit(1)
    global bar 
    bar += 1
    #print("{:.2f}".format(bar/len(test_data)))

    if P_yes > P_no:
        return 1
    return 0
    
bar = 0

test_data['loan_paid'] = test_data.apply(predec, axis=1)
#print(test_data['loan_paid'])

test_data.to_csv("NBC outpout limted feat.csv", columns=["ID", 'loan_paid'], index=False)