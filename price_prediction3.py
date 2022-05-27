import pickle
import streamlit as st
from sklearn import metrics, svm
def get_svm_prediction(dt,options_to_choose2):
    x = dt[options_to_choose2]
    y = dt['price']

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)

    clf = svm.SVR()
    clf.fit(x_train,y_train)
    predictions = clf.predict(x_test)

    pickle.dump(clf, open('./model3.sav','wb'))
