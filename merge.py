#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     merge.py
# ROLE:     TODO (some explanation)
# CREATED:  2016-04-21 20:03:37
# MODIFIED: 2016-04-21 20:03:39

import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "sys.argv[1]: input file1 (expected head info)"
        print "sys.argv[2]: input file2 & output merge file"
        exit()

    result = open(sys.argv[2], "a+")
    with open(sys.argv[1], "r")as fin:
        for i, line in enumerate(fin):
            if i == 0:
                continue
            result.write(line)
    result.close()