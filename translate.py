#!/usr/bin/env python
# -*- coding: latin-1 -*-

import urllib, urllib2,re
import sys, os


def translate(text, f, t):
    values = {'text':text,'langpair':"%s|%s"%(f, t)}
    url = 'http://translate.google.cn/'
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    req.add_header('User-Agent', "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)")
    response = urllib2.urlopen(req)
    MySentence = response.read()
    mm = re.compile('TRANSLATED_TEXT=\'(.*)\';INPUT_TOOL_PATH=').findall(MySentence)[0]
    return mm

def tranlateForIgnorException(text, lang1, lang2):
    excpCnt = 0
    while 1:
        try:
            aStr = translate(text, lang1, lang2)
            break
        except:
            excpCnt = excpCnt + 1                    
            if excpCnt > 100:
                break
    return aStr

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print "sys.argv[1]: input file for translation"
        print "sys.argv[2]: output file"
        print "sys.argv[3]: original language"
        print "sys.argv[4]: target language"
        print "Notice, 'en' for English and 'zh-CN' for Chinese"
        exit()

    output = open(sys.argv[2], "a+")
    with open(sys.argv[1], "r")as fin:
        for i, line in enumerate(fin):
            print i
            if i == 0:
                continue
            aList = line.strip().split("\t")
            if len(aList) != 5:
                print "line split error!"
                print "line No. " + str(i)
                exit()
            id = aList[0]
            #train/book.cn should use following code for its summary is a URL.
            # if i == 2035:
                # summary = "在现在Valder毕比展"
            # else:
                # summary = translate(aList[1], sys.argv[3], sys.argv[4])
            summary = translate(aList[1], sys.argv[3], sys.argv[4])
            polarity = aList[2]
            text = translate(aList[3], sys.argv[3], sys.argv[4])
            category = aList[4]
            output.write(id + "\t" + summary + "\t" + polarity + "\t" + text + "\t" + category + "\n")
    output.close()


