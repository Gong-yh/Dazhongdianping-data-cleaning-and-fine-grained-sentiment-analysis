# # path = r'D:\Programfile\py-object\fsauor2018-master\scripts\data\vocab.txt'
# # file = open(path, encoding='gbk')
# # print(file.read())
# embedding_file = r'D:\Programfile\py-object\fsauor2018-master\scripts\data\sentiment_analysis_testa.csv'
# import argparse
# import csv
# import json
# import re
#
# def replace_dish(content):
#     return re.sub("【.{5,20}】","<dish>",content)
#
# def normalize_num(words):
#     '''Normalize numbers
#     for example: 123 -> 100,  3934 -> 3000
#     '''
#     tokens = []
#     for w in words:
#         try:
#             ww = w
#             num = int(float(ww))
#             if len(ww) < 2:
#                 tokens.append(ww)
#             else:
#                 num = int(ww[0]) * (10**(len(str(num))-1))
#                 tokens.append(str(num))
#         except:
#             tokens.append(w)
#     return tokens
#
# def tokenize(content):
#     # content = content.replace("\u0006",'').replace("\u0005",'').replace("\u0007",'')
#     tokens = []
#     content = content.lower()
#     # 去除重复字符
#     # content = re.sub('~+','~',content)
#     # content = re.sub('～+','～',content)
#     # content = re.sub('(\n)+','\n',content)
#     # content = re.sub("</div><!商家回应>.*?</div></div>", "",content)
#     # content = re.sub("<.*?.jpg</a>", "", content)
#     # content = re.sub("< pclass=.*?", "", content)
#     # content = re.sub("<.*?<!查看更多点评></div>", "", content)
#     # content = re.sub("<.*?</div></div>", "", content)
#     # content = re.sub("<divclass=.+", "", content)
#     # content = re.sub("<.*?查看更多点评>", "", content)
#     # content = re.sub("<.+", "", content)
#     # for para in content.split('\n'):
#     for words in content.split(' '):
#         para_tokens = []
#         # jieba.load_userdict(self_dict)
#         # words = list(jieba.cut(para))
#         # words = [ ' '.join(i) for i in words.split(' ')]
#         # words =
#         words = normalize_num(words)
#         para_tokens.extend(words)
#         para_tokens.append('<para>')
#         tokens.append(' '.join(para_tokens))
#     # content = " ".join(tokens)
#     content = re.sub('\s+',' ',content)
#     content = re.sub('(<para> )+','<para> ',content)
#     content = re.sub('(- )+','- ',content)
#     content = re.sub('(= )+','= ',content)
#     content = re.sub('(\. )+','. ',content).strip()
#     content = replace_dish(content)
#     if content.endswith("<para>"):
#         content = content[:-7]
#     print(content)
#     return content
#
# def process_data(output_file, data_file):
#     data = []
#     with open(output_file,'w', encoding='utf-8') as f:
#         with open(data_file,encoding='utf-8-sig') as csvfile:
#             reader = csv.DictReader(csvfile)
#             for i,item in enumerate(reader):
#                 content = tokenize(item['content'].strip()[1:-1])
#                 item['content'] = content
#                 f.write(json.dumps(item,ensure_ascii=False)+'\n')
#                 data.append(item)
#                 if (i+1) % 10000 == 0:
#                     print("# processed -- %d --"%(i+1))
#     return data
#
# a = process_data('D:/Programfile/py-object/fsauor2018-master/scripts/data/testa.json', 'D:/Programfile/py-object/fsauor2018-master/scripts/data/seg/sentiment_analysis_testa.csv')

# for i in a:
#     print(i)
#
import json
import numpy as np
fname = 'D:/Programfile/py-object/fsauor2018-master/scripts/data/validation.json'
def gettoken(fname):
    a = 0
    aa = []
    for line in open(fname, encoding='utf-8'):
        item = json.loads(line.strip())
        content = item['content']
        tokens = content.strip().split()#加了' '
        tok_len = len(tokens)
        aa.append(tok_len)
        a += tok_len
    return a,aa

a,aa = gettoken(fname)
num_tokens =aa
num_tokens = np.array(num_tokens)
mean = a/len(aa)

max_tokens = np.mean(num_tokens) + 2 * np.std(num_tokens)
max_tokens = int(max_tokens)
print(max_tokens)
print(np.sum( num_tokens < 232 ) / len(num_tokens))
print('long',len(aa))
print(aa[:50])
print('average',mean)
print('min',min(aa))
print('max',max(aa))

    # a = content.strip().split()
    # print('a',a)
        # ids = []
        # for t in tokens:
        #     if t in w2i:
        #         ids.append(w2i[t])
        #     else:
        #         for c in t:
        #             ids.append(w2i.get(c,UNK_ID))
    #     return ids
    # if split:
    #     ids = get_tokens(content)
    # else:
    #     ids = [w2i.get(t,UNK_ID) for t in content.strip().split()]
    # if reverse:
    #     ids = list(reversed(ids))
    # tokens = [SOS_ID] + ids[:max_tokens] + [EOS_ID]
    # return tokens