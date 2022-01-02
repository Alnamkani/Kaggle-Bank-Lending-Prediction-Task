# Kaggle-Bank-Lending-Prediction-Task
This code was written as part of a class competition. The class is CS373 taught at Purdue University in the fall 2021 semester.
I'm unable to share the csv files and data due to size and privacy restrictions.
The following link takes you to the Kaggle competition page: https://www.kaggle.com/c/bank-lending-prediction-task/overview

***

## The vis.py, side.py, and data.py files

I have used these two files to examine the data before training and making predictions and making the output match the requirements of Kaggle. 

***

## Approaches 
1. NBC.py 
    * This approach uses a naive Bayes classifier with feature engineering. 
    * In the data examination and visualization part, it was clear that the data was biased and unbalanced. It was biased in the sense that the "race" variable was a confounder variable for other variables. In other words, the test and training data didn't have a similar distribution. therefore, I performed confounder adjustment methods to the training data.
3. tree.py
    * This is a gradient boosting trees approach.
    * I have performed data up-sampling to balance the data, and removed some of the biased variables.
    * using the sklearn library I made a GradientBoostingClassifier.
    * With the model, I scored a 0.21811 score which is the top 25% in the leaderboard (there were 78 participants)  

My name is C-3PO on the leaderboard.   
