# -*- coding: utf-8 -*-
"""
Created on Sun Aug 06 16:41:44 2017

@author: Sachin
"""

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
res=len(features_train[0])
print(len(features_train[0]))
print(res)