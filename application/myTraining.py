import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

if __name__ == "__main__":
    data = pd.read_csv('data.csv')
    x = data.iloc[:,:-1]
    y = data.iloc[:,-1]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    clf = LogisticRegression()
    clf.fit(x_train, y_train)

    file = open('model.pkl', 'wb')
    pickle.dump(clf, file)

    file.close()

    # infProb = clf.predict_proba(x_test)[0][1]
