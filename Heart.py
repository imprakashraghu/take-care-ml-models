# author imprakashraghu

import pandas as pd
import numpy as np
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def predictHeartDisease():    
    df = pd.read_csv('./dataset/heart.csv')
    df.head(20)
    df.info()
    df.corr().T

    # targeted input parameter and scaled down
    x = df[["thalach","trestbps","fbs"]]

    # targeted output parameter 
    y = df[["target"]]

    # splitting the dataset for training and testing
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    x_train.shape
    y_train.shape

    # model itself
    clf = MLPClassifier(hidden_layer_sizes=(51),solver="lbfgs",alpha=1e-5, activation="logistic")
    clf.fit(x, y)

    # training the data
    y_pred=clf.predict(x_train)

    # accuracy of the trained model
    print(accuracy_score(y_train, y_pred))

    return clf


