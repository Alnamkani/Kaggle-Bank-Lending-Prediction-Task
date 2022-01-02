import pandas as pd
import random



data = pd.read_csv('NBC outpout.csv')


data.to_csv("rand output.csv", columns=["ID", 'loan_paid'], index=False)

#######sudo shit delete 
# features = [Season, heating-system]

# create root node 
# growTree(root, examples, features)

# growTree(node, example, features):
#     maxScore= 0
#     maxFeature = null
#     for each feature in features:
#         D1 = examples that pass feature
#         D2 = examples that fail feature
#         if maxScore < f(D1, D2):
#             maxScore = f(D1, D2)
#             maxFeature = feature  
#     if maxFeature == null:
#         nodeClassDist = distrubtion of class labels
#         return 
#     else:
#         nodeFeature = maxFeature
#         create a left and a right child nodes
#         left child examples = examples that pass nodeFeature
#         right child examples = examples that fail nodeFeature

#   growTree(left child, left child examples, features - nodeFeature)
#   growTree(right child, right child examples, features - nodeFeature)