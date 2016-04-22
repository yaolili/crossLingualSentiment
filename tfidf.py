#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     tfidf.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-04-14 16:53:32
# MODIFIED: 2016-04-14 16:58:35

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import numpy as np
from sklearn.feature_extraction.text import (TfidfVectorizer, CountVectorizer, TfidfTransformer)
 

class Tfidf:
    def tfidf(self, trCorpus, teCorpus):
        #vect = TfidfVectorizer(ngram_range=(1, 2), norm = "l2", min_df = 3)
        vect = TfidfVectorizer(norm = "l2", min_df = 3)
        trainMatrix = vect.fit_transform(trCorpus).toarray()
        testMatrix = vect.transform(teCorpus).toarray()
        print "Tfidf done!"
        return trainMatrix, testMatrix
