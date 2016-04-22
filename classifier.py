#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     classifier.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-04-14 16:51:08
# MODIFIED: 2016-04-14 16:53:27

import numpy as np
from sklearn.preprocessing import Imputer
from sklearn import svm, metrics
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score)
from sklearn.linear_model import Ridge

class Classifier:
    def __init__(self, trainMatrix, trainLabels, testMatrix, testLabels):
        self.X_train = trainMatrix 
        self.y_train = trainLabels
        self.X_test = testMatrix
        
        #fit transform if there exit NAN or INFINITE
        #otherwise you'll get error when clf.predict()
        self.X_test = Imputer().fit_transform(self.X_test) 
        if np.isnan(self.X_test).any():
            print "nan in X_test!"
            exit()
            
        self.y_test = testLabels
        #clf = svm.SVC(kernel='rbf', gamma = 0.001, C = 100, probability=True)
        clf = svm.LinearSVC()
        clf.fit(self.X_train, self.y_train) 
        self.y_pred = clf.predict(self.X_test)
        
        '''
        print self.y_pred
        print clf.classes_
        print clf.predict_proba(self.X_test)
        print zip(clf.classes_, clf.predict_proba(self.X_test)[0])
        '''
        
        print("SVM report %s\n" % (metrics.classification_report(testLabels, self.y_pred)))
        
        

