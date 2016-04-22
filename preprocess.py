#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     preprocess.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-03-28 15:08:31
# MODIFIED: 2016-04-13 10:34:41

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
from bs4 import BeautifulSoup as BS

def writeFile(sampleSets, writeFile):
    result = open(writeFile, "w+")
    result.write("id\tsummary\tpolarity\ttext\tcategory\n")
    for i in range(len(sampleSets)):
        if len(sampleSets[i]) < 5:
            print "sampleSets length error!"
            exit()
        id = sampleSets[i][0]
        summary = sampleSets[i][1].replace('\n', ' ').replace('\t', ' ')
        polarity = sampleSets[i][2]
        text = sampleSets[i][3].replace('\n', ' ').replace('\t', ' ')
        category = sampleSets[i][4]
        result.write(id + "\t" + summary + "\t" + polarity + "\t" + text+ "\t" + category + "\n") 
        #result.write(text + "\n")
    print "preprocess.py writeFile() done!"
    result.close()

def getSample(items):
    sampleSets = []
    for each in items:
        if each.review_id:
            id = each.review_id.get_text()
        else:
            id = "None"
        #summary = nltkProcess(each.summary.get_text(), type)
        summary = each.summary.get_text()
        if each.polarity:
            polarity = each.polarity.get_text()
        else:
            polarity = "Unknow"
        category = each.category.get_text()
        #Here cannot use each.text, which will return all text from tags in each
        text = each.find("text").get_text()
        aList = [id, summary, polarity, text, category]
        sampleSets.append(aList)
    return sampleSets

def readData(inputFile):
    with open(inputFile, "r") as fin:
        content = BS(fin.read(), "lxml")
        items = [a for a in content.find_all('item')]
        sampleSets = getSample(items)
        print "preprocess.py readData() done!"
        return sampleSets

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "sys.argv[1]: input raw dataSet!"
        print "sys.argv[2]: output preResult filePath!"
        exit()
        
    sampleSets = readData(sys.argv[1])
    writeFile(sampleSets, sys.argv[2])
        
    
