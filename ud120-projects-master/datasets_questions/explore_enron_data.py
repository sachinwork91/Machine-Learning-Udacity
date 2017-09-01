#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pandas as pd
enron_data = pickle.load(open("D:/ud120-projects-master/ud120-projects-master/final_project/final_project_dataset.pkl", "r"))

data=pd.read_csv("D:/ud120-projects-master/ud120-projects-master/final_project/poi_names.txt")

enron_data['PRENTICE JAMES']['total_stock_value']



enron_data['COLWELL WESLEY']['from_this_person_to_poi']
enron_data['SKILLING JEFFREY K']['total_stock_value'] #Jeffrey K Skilling']
count=0
for pr,pv in enron_data.items():
    if(pv['total_payments']=='NaN'):
        count=count+1
        
print(count)        