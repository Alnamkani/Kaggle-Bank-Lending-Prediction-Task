import pandas as pd

data = pd.read_csv("NBC outpout limted feat.csv",delimiter=',', header='infer', quotechar="\"", comment=None)

# print(len(data[data['race'] =='W']))
# print((data['race'].value_counts()))