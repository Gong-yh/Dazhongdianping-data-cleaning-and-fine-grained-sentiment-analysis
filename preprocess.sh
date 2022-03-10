#!/bin/bash

# Modify the following values depend on your environment
# Path to the csv files
TRAIN_FILE=D:/Programfile/py-object/fsauor2018-master/scripts/data/sentiment_analysis_trainingset.csv
VALIDATION_FILE= D:/Programfile/py-object/fsauor2018-master/scripts/data/sentiment_analysis_validationset.csv
TESTA_FILE= D:/Programfile/py-object/fsauor2018-master/scripts/data/sentiment_analysis_testa.csv
#TESTB_FILE= D:/Programfile/py-object/fsauor2018-master/scripts/data/0911/sentiment_analysis_testb.csv

# Path to pretrained embedding file
EMBEDDING_FILE=D:/Programfile/py-object/fsauor2018-master/scripts/data/sgns.sogou.word
EMBEDDING_WORD_FILE=D:/Programfile/py-object/fsauor2018-master/scripts/data/all_content_no_punc_300_8_mc2_fnl.w2v
EMBEDDING_CHAR_FILE=D:/Programfile/py-object/fsauor2018-master/scripts/data/all_char_no_punc_300_15_mc2_fnl.w2v

OCAB_SIZE=50000

# Create a folder to save training files
#mkdir -p data
mkdir -p D:/Programfile/py-object/fsauor2018-master/scripts/

#echo 'Process training file ...'
#python data_preprocess.py \
#    --data_file=$TRAIN_FILE \
#    --output_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/train.json \
#    --vocab_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/vocab.txt \
#    --vocab_size=$VOCAB_SIZE
#
#echo 'Process validation file ...'
#python data_preprocess.py \
#    --data_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/sentiment_analysis_validationset.csv \
#    --output_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/validation.json
##
#echo 'Process testa file ...'
#python data_preprocess.py \
#    --data_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/sentiment_analysis_testa.csv \
#    --output_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/testa.json

## Uncomment following code to get testb file
## echo 'Process testb file ...'
## python data_preprocess.py \
##     --data_file=$TESTB_FILE \
##     --output_file=data/testb.json
#
#echo 'Get pretrained embedding ...'
#python data_preprocess.py \
#    --data_file=$EMBEDDING_FILE \
#    --output_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/embedding.txt \
#    --vocab_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/vocab.txt \
#    --embedding=True

# 想试试char
echo 'Get word pretrained embedding……'
python data_preprocess.py \
    --data_file=$EMBEDDING_WORD_FILE \
    --output_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/selfembedding.txt \
    --vocab_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/vocab.txt \
    --embedding=True


#如果要使用tencent，就直接是txt，但是要加入unk，parse和eos
#EMBEDDING_FILE 的encodeing有问题

#echo "Get label file ..."
#cp ../labels.txt data/labels.txt
##cp ../labels.txt data/labels.txt