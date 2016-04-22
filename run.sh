#!/usr/bin/env bash
# AUTHOR:   yaolili
# FILE:     run.sh
# ROLE:     TODO (some explanation)
# CREATED:  2016-04-12 13:11:20
# MODIFIED: 2016-04-12 13:11:31

#pre-processing Train_EN
python preprocess.py data/train/Train_EN/music/train.data  preResult/Train_EN/music.out
python preprocess.py data/train/Train_EN/dvd/train.data  preResult/Train_EN/dvd.out
python preprocess.py data/train/Train_EN/book/train.data  preResult/Train_EN/book.out

#pre-processing Train_CN
python preprocess.py data/train/Train_CN/music/sample.data  preResult/Train_CN/music.out
python preprocess.py data/train/Train_CN/dvd/sample.data  preResult/Train_CN/dvd.out
python preprocess.py data/train/Train_CN/book/sample.data  preResult/Train_CN/book.out

#pre-processing Test
python preprocess.py data/test/music.data   preResult/test/music.out
python preprocess.py data/test/dvd.data   preResult/test/dvd.out
python preprocess.py data/test/book.data   preResult/test/book.out

#translate training data
python translate.py preResult/Train_EN/book.out transResult/train/book.cn en zh-CN
python translate.py preResult/Train_EN/dvd.out transResult/train/dvd.cn en zh-CN
python translate.py preResult/Train_EN/music.out transResult/train/music.cn en zh-CN

python translate.py preResult/Train_CN/book.out transResult/train/book.en zh-CN en
python translate.py preResult/Train_CN/dvd.out transResult/train/dvd.en zh-CN en
python translate.py preResult/Train_CN/music.out transResult/train/music.en zh-CN en

#translate test data
python translate.py preResult/test/book.out transResult/test/book.en zh-CN en
python translate.py preResult/test/dvd.out transResult/test/dvd.en zh-CN en
python translate.py preResult/test/music.out transResult/test/music.en zh-CN en

#merge file
cp -r transResult/ mergeResult

python merge.py preResult/Train_EN/dvd.out mergeResult/train/dvd.en 
python merge.py preResult/Train_EN/book.out mergeResult/train/book.en
python merge.py preResult/Train_EN/music.out mergeResult/train/music.en

python merge.py preResult/Train_CN/dvd.out mergeResult/train/dvd.cn
python merge.py preResult/Train_CN/book.out mergeResult/train/book.cn
python merge.py preResult/Train_CN/music.out mergeResult/train/music.cn 

#train classifier & predict & write result
python main.py mergeResult/train/book.en transResult/test/book.en en >> book.txt
python main.py mergeResult/train/dvd.en transResult/test/dvd.en en >> dvd.txt
python main.py mergeResult/train/music.en transResult/test/music.en en >> music.txt

