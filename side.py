import pandas as pd
import random



data = pd.read_csv('NBC outpout.csv')


data.to_csv("rand output.csv", columns=["ID", 'loan_paid'], index=False)
