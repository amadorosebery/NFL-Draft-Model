# -*- coding: utf-8 -*-

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from sklearn import tree
##################################################
<<<<<<< HEAD
cfb_drafted = pd.read_excel("/Users/connorlevenson/Downloads/NFL-Draft-Model-master-3/CFB_Stats.xlsx", sheet_name="CFB Drafted")

cfb_undrafted = pd.read_excel("/Users/connorlevenson/Downloads/NFL-Draft-Model-master-3/CFB_Stats.xlsx", sheet_name="CFB Not Drafted")

cfb_drafted_2014to2017 = pd.read_excel("/Users/connorlevenson/Downloads/NFL-Draft-Model-master-3/CFB_Stats.xlsx", sheet_name="CFB 2014-2017")

cfb_drafted_2000to2013 = pd.read_excel("/Users/connorlevenson/Downloads/NFL-Draft-Model-master-3/CFB_Stats.xlsx", sheet_name="CFB 2000-2013")
=======
cfb_drafted = pd.read_excel("/Users/kenpo/Desktop/CFB_Stats_New_04022019", sheet_name="CFB Drafted")

cfb_undrafted = pd.read_excel("/Users/kenpo/Desktop/CFB_Stats_New_04022019", sheet_name="CFB Not Drafted")

cfb_drafted_2014to2017 = pd.read_excel("/Users/kenpo/Desktop/CFB_Stats_New_04022019.xlsx", sheet_name="CFB 2014-2017")

cfb_drafted_2000to2013 = pd.read_excel("/Users/kenpo/Desktop/CFB_Stats_New_04022019.xlsx", sheet_name="CFB 2000-2013")
>>>>>>> 625b08395ab173ce806b6b13962384a72e4b0fd4

##################################################

cfb_drafted_G = np.array(cfb_drafted["G"])
cfb_drafted_Cmp = np.array(cfb_drafted["Cmp"])
cfb_drafted_Att = np.array(cfb_drafted["Att"])
cfb_drafted_Pct = np.array(cfb_drafted["Pct"])
cfb_drafted_Yds = np.array(cfb_drafted["Yds"])
cfb_drafted_TD = np.array(cfb_drafted["TD"])
cfb_drafted_Int = np.array(cfb_drafted["Int"])
cfb_drafted_Rate = np.array(cfb_drafted["Rate"])

#################################################

cfb_undrafted_G = np.array(cfb_undrafted["G"])
cfb_undrafted_Cmp = np.array(cfb_undrafted["Cmp"])
cfb_undrafted_Att = np.array(cfb_undrafted["Att"])
cfb_undrafted_Pct = np.array(cfb_undrafted["Pct"])
cfb_undrafted_Yds = np.array(cfb_undrafted["Yds"])
cfb_undrafted_TD = np.array(cfb_undrafted["TD"])
cfb_undrafted_Int = np.array(cfb_undrafted["Int"])
cfb_undrafted_Rate = np.array(cfb_undrafted["Rate"])

#######################################################

##What do yu want to predict?
target = cfb_drafted_2000to2013["Drafted?"]

##Figure out which stats you want the classifier to use
<<<<<<< HEAD
features_training = cfb_drafted_2000to2013[["G","Cmp","Pct","Yds","Y/A","TD*Cmp/Att"]].values

## create a decision
CFB_training_tree = tree.DecisionTreeClassifier()
CFB_training_tree = CFB_training_tree(features_training, target)
print(CFB_training_tree.feature_importances_)

## Create a prediction using past data
test_features = cfb_drafted_2014to2017[["G","Cmp","Pct","Yds","Y/A","TD*Cmp/Att"]].values
=======
features_training = cfb_drafted_2000to2013[["G","Cmp","Pct","Yds","Y/A","TDC"]].values #Last year TD * CMP/ATT

## create a decision
CFB_training_tree = tree.DecisionTreeClassifier()
CFB_training_tree.fit = CFB_training_tree(features_training, target)
print(CFB_training_tree.feature_importances_)

## Create a prediction using past data
test_features = cfb_drafted_2014to2017[["G","Cmp","Pct","Yds","Y/A","TDC"]].values #Last year TD * CMP/ATT
>>>>>>> 625b08395ab173ce806b6b13962384a72e4b0fd4

CFB_2014to2017_prediction = CFB_training_tree.predict(test_features)
print(CFB_2014to2017_prediction)
