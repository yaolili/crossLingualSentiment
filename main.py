#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     main.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-04-14 16:57:14
# MODIFIED: 2016-04-14 16:57:22

import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from nltk import stem
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import numpy as np
from tfidf import Tfidf
from sentiment import Sentiment
from classifier import Classifier
from sklearn.feature_selection import SelectKBest, chi2


def featureSelection(trainMatrix, trainLables, testMatrix, testLables):
    for k in range(8000, 0, -1000):
        ch2 = SelectKBest(chi2, k)
        X_train = ch2.fit_transform(trainMatrix, trainLables)
        X_test = ch2.transform(testMatrix)
        print k
        classifierInstance = Classifier(X_train, trainLables, X_test, testLables)
    return X_train, X_test

def combineFeature(matrix1, matrix2, matrix3 = None):
    allMatrix = np.concatenate((matrix1, matrix2), axis=1)
    if isinstance(matrix3, np.ndarray):
        allMatrix = np.concatenate((allMatrix, matrix3), axis=1)
    return allMatrix


def nltkProcess(text, type):
    if not text:
        print "Empty text in nltkProcess()!"
        exit()
        
    tokenizer = RegexpTokenizer(r'\w+') 
    tokens = tokenizer.tokenize(text) 
    #type =0, remove stopwords
    if type == 0:
        noStopwords = [w.lower() for w in tokens if not w.lower() in stopwords.words('english')]
    elif type == 1:
        noStopwords = [w.lower() for w in tokens]
    else:
        print "nltkProcess type error, expected 0 or 1"
        exit()
    lmtzr = ""
    for w in noStopwords:
        lmtzr += WordNetLemmatizer().lemmatize(w) + " "
    return lmtzr
    
    
def readData(inputFile, lang):
    polarities = []
    tfidfText = []
    vsText = []
    categories = []
    with open(inputFile, "r") as fin:
        for i, line in enumerate(fin):
            id, summary, polarity, text, category = line.strip().split("\t")
            polarities.append(polarity)
            categories.append(category)
            if lang == "en":
                #tokenize & lemmatize
                text1 = nltkProcess(summary + " " + text, 0)
                text2 = nltkProcess(summary + " " + text, 1)
            elif lang == "zh-CN":
                #segmentation
                print "zh-CN segmentation remain to do"
                exit()
            else:
                print "language error!"
                exit()
            tfidfText.append(text1)
            vsText.append(text2)
    return tfidfText, vsText, np.array(polarities), categories
    
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "sys.argv[1]: input train corpus"
        print "sys.argv[2]: input test corpus"
        print "sys.argv[3]: corpus language, 'en' for English and 'zh-CN' for Chinese"
        exit()
    
    tfidfInstance = Tfidf()
    sentimentInstance = Sentiment()
    
    trCorpus1, trCorpus2, trPolarity, trCategory = readData(sys.argv[1], sys.argv[3])
    teCorpus1, teCorpus2, tePolarity, teCategory = readData(sys.argv[2], sys.argv[3])

    trainTfidf, testTfidf = tfidfInstance.tfidf(trCorpus1, teCorpus1)
    trainVS = sentimentInstance.VSPolarity(trCorpus2)
    testVS = sentimentInstance.VSPolarity(teCorpus2)
    trainMatrix = combineFeature(trainTfidf, trainVS)
    testMatrix = combineFeature(testTfidf, testVS)
    
    print sys.argv[2]
    trainMatrix, testMatrix = featureSelection(trainMatrix, trPolarity, testMatrix, tePolarity)
    # classifierInstance = Classifier(trainMatrix, trPolarity, testMatrix, tePolarity)

