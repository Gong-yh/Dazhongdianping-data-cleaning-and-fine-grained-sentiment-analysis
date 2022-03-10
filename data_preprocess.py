# ======================================== 
# Author: Xueyou Luo 
# Email: xueyou.luo@aidigger.com 
# Copyright: Eigen Tech @ 2018 
# ========================================

import argparse
import csv
import json
import re
from collections import Counter
import jieba
import zhconv
from zhconv import convert

self_dict = r'D:\Programfile\py-object\fsauor2018-master\scripts\data\expand70000-dict.txt'
jieba.load_userdict(self_dict)

# 对于vocab有问题
def add_arguments(parser):
    """Build ArgumentParser."""
    parser.register("type", "bool", lambda v: v.lower() == "true")

    parser.add_argument("--data_file", type=str, default=None, required=True, help="data file to process")
    parser.add_argument("--output_file", type=str, default=None, required=True, help="data file to process")
    parser.add_argument("--vocab_file", type=str, default=None, help="vocab file, needed when data file is training file")
    parser.add_argument("--vocab_size", type=int, default=50000, help='vocab size')
    parser.add_argument("--embedding", type='bool', nargs="?", const=True, default=False, help='whether process embedding file')
    
def replace_dish(content):
    if 'test' in flags.data_file:
        pass
    if 'train' or 'validation' in flags.data_file:
        return re.sub("【.{5,20}】","<dish>",content)

def normalize_num(words):
    '''Normalize numbers
    for example: 123 -> 100,  3934 -> 3000
    '''
    tokens = []
    for w in words:
        try:
            ww = w
            num = int(float(ww))
            if len(ww) < 2:
                tokens.append(ww)
            else:
                num = int(ww[0]) * (10**(len(str(num))-1))
                tokens.append(str(num))
        except:
            tokens.append(w)
    return tokens

def tokenize(content,stopwords):
    # print(content)
    content = content.replace("\u0006",'').replace("\u0005",'').replace("\u0007",'')# 我的不要
    content = convert(content, 'zh-cn')
    # print(3,content)
    tokens = []
    content = content.lower()
    # 去除重复字符
    content = re.sub('~+','~',content)# 我的不要
    content = re.sub('～+','～',content)# 我的不要
    content = re.sub('(\n)+','\n',content)# 我的不要
    r = "[A-Za-z0-9_.!+-=——,$%^，。？、~@#￥%……&…*《》<>{}【】()/]"
    content = re.sub(r, ' ', content)  # 我加的
    # content = str(re.findall('[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\u4e00-\u9fa5,！:《》.「」。]',str(content)))
    if 'test' in flags.data_file:# 我自己加的
        content = re.sub("</div><!商家回应>.*?</div></div>", "",content)
        content = re.sub("<.*?.jpg</a>", "", content)
        content = re.sub("< pclass=.*?", "", content)
        content = re.sub("<.*?<!查看更多点评></div>", "", content)
        content = re.sub("<.*?</div></div>", "", content)
        content = re.sub("<divclass=.+", "", content)
        content = re.sub("<.*?查看更多点评>", "", content)
        content = re.sub("<.+", "", content)

    for para in content.split('\n'):
    # 我的
    # for words in content.split(' '):
    #     para_tokens = []
    #     # jieba.load_userdict(self_dict)
    #     # words = list(jieba.cut(para))
    #     # words = [ ' '.join(i) for i in words.split(' ')]
    #     # words =
    #     words = normalize_num(words)
    # 他的
        para_tokens = []
        words = list(jieba.cut(para))
        words = normalize_num(words)
        outstr = ''
        for word in words:
            if word not in stopwords:
                if word != '\t':
                    outstr += word
                    outstr += " "
        para_tokens.append(outstr)
        # para_tokens.extend(words)
        para_tokens.append('<para>')
        tokens.append(' '.join(para_tokens))
    content = " ".join(tokens)
    content = re.sub('\s+',' ',content)
    content = re.sub('(<para> )+','<para> ',content)
    content = re.sub('(- )+','- ',content)    
    content = re.sub('(= )+','= ',content)
    content = re.sub('(\. )+','. ',content)#.strip()
    content = replace_dish(content)

    # print(2,content)
    if content.endswith("<para>"):
        content = content[:-7]
        # print(1,content)
    # print(content)
    return content

def create_vocab(data, vocab_file, vocab_size):
    print("# Start to create vocab ...")
    words = Counter()
    for item in data:
        words.update(item['content'].split())
    special_tokens = ['<unk>','<sos>','<eos>']
    with open(vocab_file,'w', encoding='utf-8') as f:
        for w in special_tokens:
            f.write(w + '\n')
        for w,_ in words.most_common(vocab_size-len(special_tokens)):
            f.write(w + '\n')
    print("# Created vocab file {0} with vocab size {1}".format(vocab_file,vocab_size))

# def process_data(output_file, data_file):
#     data = []
#     with open(output_file,'w', encoding='utf-8') as f:
#         with open(data_file,encoding='utf-8-sig') as csvfile:
#             reader = csv.DictReader(csvfile)
#             for i,item in enumerate(reader):
#                 content = tokenize(item['content'].strip()[1:-1])#[1:-1]，要在有cls和eos的情况下加
#                 item['content'] = content
#                 f.write(json.dumps(item,ensure_ascii=False)+'\n')
#                 data.append(item)
#                 if (i+1) % 10000 == 0:
#                     print("# processed -- %d --"%(i+1))
#     return data
def process_data(output_file, data_file,csstopwords):
    data = []
    with open(output_file, 'w', encoding='utf-8') as f:
        with open(data_file, encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for i, item in enumerate(reader):
                content = tokenize(item['content'].strip()[1:-1],csstopwords)  # [1:-1]，要在有cls和eos的情况下加
                item['content'] = content
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
                data.append(item)
                if (i + 1) % 10000 == 0:
                    print("# processed -- %d --" % (i + 1))
    return data

def process_embedding(embedding_file, vocab_file, out_embedding_file):
    words = set([line.strip() for line in open(vocab_file,encoding='utf-8')])#, encoding='utf-8'
    with open(out_embedding_file,'w',encoding='utf-8') as f:# 他没加,encoding='utf-8'
        for line in open(embedding_file,'r',encoding='utf-8'):# 他没加,encoding='utf-8',encoding='utf-8' 没加'r'
            tokens = line.split()
            # skip the first line
            if len(tokens) == 2:
                continue
            word = tokens[0].lower()
            if word in words:
                f.write(word + ' ' + ' '.join(tokens[1:]) + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    add_arguments(parser)
    flags, unparsed = parser.parse_known_args()
    # print(flags)
    # print('----------------------')
    # print(flags.data_file)
    if flags.embedding:
        print('process_embedding')
        process_embedding(flags.data_file, flags.vocab_file, flags.output_file)
        # exit(0)

    else:
        ltpstopword_path = r'D:\Programfile\py-object\fsauor2018-master\scripts\data\hit_stopwords.txt'
        csstopwords = [line.strip() for line in open(ltpstopword_path, 'r', encoding='utf-8').readlines()]
        if 'train' in flags.data_file:
            if flags.vocab_file is None:
                raise ValueError("Must provided a vocab file to save vocab")
            data = process_data(flags.output_file, flags.data_file,csstopwords)
            create_vocab(data,flags.vocab_file,flags.vocab_size)#flags.vocab_size
        else:
            process_data(flags.output_file, flags.data_file,csstopwords)

# data_file = "D:/Programfile/py-object/fsauor2018-master/scripts/data/sgns.sogou.word"
# vocab_file ="D:/Programfile/py-object/fsauor2018-master/scripts/data/feature_vocab.txt"
# output_file ="D:/Programfile/py-object/fsauor2018-master/scripts/data/feature_embedding.txt"
# process_embedding(data_file, vocab_file, output_file)
