#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     sentiment.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-03-30 18:14:12
# MODIFIED: 2016-03-30 18:14:17

import numpy as np
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment 

class Sentiment:
    def VSPolarity(self, corpus):
        self.result = []
        for sentence in corpus:
            vs = vaderSentiment(sentence)
            aList = [vs["neg"], vs["neu"], vs["pos"]]
            self.result.append(aList)
        print "Sentiment VSPolarity done!"
        return np.array(self.result)
        