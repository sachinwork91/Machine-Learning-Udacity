#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("D:/ud120-projects-master/ud120-projects-master/tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


from sklearn import tree
from sklearn.metrics import accuracy_score
clf=tree.DecisionTreeClassifier(min_samples_split=40)

t0 = time()
clf.fit(features_train,labels_train)
print "Decision Training time:", round(time()-t0, 3), "s"


pred=clf.predict(features_test)
print "Decision predicting time:", round(time()-t0, 3), "s"

accuracy=accuracy_score(pred, labels_test  )
print(accuracy)
#print('Accuracy is : ' + accuracy)
res=len(features_train[0])
print(len(features_train[0]))
#########################################################
### your code goes here ###


#########################################################


