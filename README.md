# - 大众点评
对自己完成下来大众点评的文本数据进行清晰的分析后，主要对文本细粒度属性的内容进行评估，根据大众点评的三个（情况、环境、服务）分类，不同下的情结果，用于论文中的进一步分析
暂时将数据分为数据分析和细个粒度分析部分，将大众点评的爬取补上来，感觉还是学会了挺多东西的，做先做学习记录吧

## - 数据清洗：
运行preprocess.sh   

python 版本3.6
主要包有argparse,re等


## - 细粒度情感分析：
训练运行elmo_tain.sh
测试运行elmo_inference.sh

python 版本3.6
主要包有tensorflow，numpy，codecs，gensim等

主要用到的模型在img中展示，Elmo+Cnn+Attention来加强每个属性下的准确性
此外使用LightGBM在不同的属性下提取出7个关键词，以增强每个属性下的准确性，再通过Cnn得到该维度下的综合向量表示，在准确性上比单使用Elmo的要提升不少
数据集使用的是2018年美团的细粒度情感分析赛道的数据集（训练模型），以及自己爬取的大众点评的数据集（被标注）
词向量使用的是300d的W2v的搜狗预训练模型，比自己训练的稍微提升了一点


之前尝试了用BERT，不知道为什么跑不下来，之后再试试叭！

