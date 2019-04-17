import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
import xgboost as xgb
import graphviz
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

################### FUNCTIONS TO CALCULATE PRECISION, RECALL ################

def fp(pred, act):
    fp = 0
    for i in range(len(pred)):
        if pred[i]==1 and act[i]==0:
            fp = fp + 1
    return fp

def tp(pred, act):
    tp = 0
    for i in range(len(pred)):
        if pred[i] == 1 and act[i] == 1:
            tp = tp + 1
    return tp

def fn(pred, act):
    fn = 0
    for i in range(len(pred)):
        if pred[i] == 0 and act[i]==1:
            fn = fn + 1
    return fn

############################ FILE READING ##################################

cfb_drafted_2014to2017 = pd.read_excel("/Users/connorlevenson/Downloads/NFL-Draft-Model-master-3/CFB_Stats_New_04022019.xlsx", sheet_name="CFB 2014-2017")
cfb_drafted_2000to2013 = pd.read_excel("/Users/connorlevenson/Downloads/NFL-Draft-Model-master-3/CFB_Stats_New_04022019.xlsx", sheet_name="CFB 2000-2013")
cfb_drafted_2000to2017 = pd.read_excel("/Users/connorlevenson/Downloads/NFL-Draft-Model-master-3/CFB_Stats_New_04022019.xlsx", sheet_name="CFB Combined")
cfb_2019 = pd.read_excel("/Users/connorlevenson/Downloads/NFL-Draft-Model-master-3/CFB_Stats_New_04022019.xlsx", sheet_name="2019")


######################## Decision Tree #################################

y_train = cfb_drafted_2000to2013["Drafted?"]  ##Target Variable

y_test = np.array(cfb_drafted_2014to2017["Drafted?"])

x_train = cfb_drafted_2000to2013[["G", "Cmp", "Pct","Yds","TDC", "Rate","Att/INT","Yds/G"]].values  ##Which features will be used to train

x_test = cfb_drafted_2014to2017[["G", "Cmp", "Pct","Yds", "TDC", "Rate","Att/INT", "Yds/G"]].values

x_test_2019 = cfb_2019[["G", "Cmp", "Pct","Yds", "TDC", "Rate","Att/INT", "Yds/G"]].values

x_2000to2017 = cfb_drafted_2000to2017[["G", "Cmp", "Pct","Yds","TDC", "Rate","Att/INT","Yds/G"]].values

y_2000to2017 = np.array(cfb_drafted_2000to2017["Drafted?"])

########################################################################

CFB_tree = tree.DecisionTreeClassifier()
CFB_tree = CFB_tree.fit(x_train, y_train)
CFB_tree_prediction = CFB_tree.predict(x_test)
print('\nDecision Tree Report: \n', metrics.classification_report(y_test, CFB_tree_prediction))

################ AUC Value - Decision Tree ##################################

np_proba_DT = np.array(CFB_tree.predict_proba(x_test))
y_true = np.array(y_test)
prob_DT = np_proba_DT[:,1]
fpr_DT, tpr_DT, thresholds = metrics.roc_curve(y_true, prob_DT)
print("\nAUC for Decision tree: \n",metrics.auc(fpr_DT,tpr_DT))


######################### Scale Data for RF Classifier ######################

sc = StandardScaler()
x_train_scale = sc.fit_transform(x_train)
x_test_scale = sc.transform(x_test)

x_test_scale_2019 = sc.transform(x_test_2019) 

######################## RF Classifier ###########################

RF_classifier = RandomForestClassifier(n_estimators=100,random_state=0)
RF_classifier.fit(x_train_scale, y_train) 
CFB_RF_prediction = RF_classifier.predict(x_test_scale)

CFB_x = np.array(CFB_RF_prediction)
print('\nRandom Forest Report: \n', metrics.classification_report(y_test, CFB_RF_prediction))

################ AUC Value - RF ##################################

np_proba_RF = np.array(RF_classifier.predict_proba(x_test_scale))
y_true = np.array(y_test)
prob_RF = np_proba_RF[:,1]
fpr_RF, tpr_RF, thresholds = metrics.roc_curve(y_true, prob_RF)
print("\nAUC for Random forest: \n",metrics.auc(fpr_RF,tpr_RF))

################ K Nearest Neighbors ########################

KNN_clf = KNeighborsClassifier(n_neighbors=19)
KNN_clf.fit(x_train, y_train)
y_expect = y_test
y_pred = KNN_clf.predict(x_test)
print('\nKNN Report: \n', metrics.classification_report(y_expect, y_pred))

################ AUC Value - KNN ##################################

np_proba_KNN = np.array(KNN_clf.predict_proba(x_test))
y_true = np.array(y_test)
prob_KNN = np_proba_KNN[:,1]
fpr_KNN, tpr_KNN, thresholds = metrics.roc_curve(y_true, prob_KNN)
print("\nAUC for KNN: \n",metrics.auc(fpr_KNN,tpr_KNN),'\n')


################ XBG Boost Augmentation ###################################

data_dmatrix = xgb.DMatrix(data=x_train, label=y_train)

valid = [(x_test,y_test)]
xgb_clf= xgb.XGBClassifier()
xgb_clf.fit(x_train,y_train, early_stopping_rounds=2,eval_set=valid, eval_metric='error')
xgb_pred = xgb_clf.predict(x_test)
print('\nXGB Report: \n', metrics.classification_report(y_test, xgb_pred))

########################## AUC Value - XGBoost ######################################

np_proba_xgb = np.array(xgb_clf.predict_proba(x_test))
y_true = np.array(y_test)
prob_xgb = np_proba_xgb[:,1]
fpr_xgb, tpr_xgb, thresholds = metrics.roc_curve(y_true, prob_xgb)
print('\nXGBoost AUC Score: \n', np.round(metrics.auc(fpr_xgb,tpr_xgb),decimals=4), '\n')

################################################

DT_features = (["G", "Cmp", "Pct","Yds","TDC", "Rate","Att/INT","Yds/G"])
DT_target = ("D","UD")
dot_data = tree.export_graphviz(CFB_tree,out_file=None, 
                                feature_names=DT_features,
                                class_names=DT_target,
                                filled = True, rounded = True, 
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("College Quarterbacks")
#graph


#CFB_2019_prediction = RF_classifier.predict(x_test_scale_2019)
#print(CFB_2019_prediction)

for i in cfb_drafted_