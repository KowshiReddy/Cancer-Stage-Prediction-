import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

def prediction(input_variables):
    data=pd.read_csv("Cancer_data_num.csv")
    data.drop(['Patient Id'],axis=1,inplace=True)
    data.drop(['Gender'],axis=1,inplace=True)
    data.drop(['Age'],axis=1,inplace=True)
    #data['level'].replace('high','2',inplace=True)
    #data['level'].replace('medium','1',inplace=True)
    #data['level'].replace('low','0',inplace=True)
    X = data.drop('level',axis = 1)
    y = data['level']
    model=RandomForestClassifier()
    model.fit(X,y)

    X_test=input_variables
    y_pred_randomF = model.predict(X_test)
    return y_pred_randomF


