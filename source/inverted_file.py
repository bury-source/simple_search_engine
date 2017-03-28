#!/usr/bin/python
# -*- coding:utf-8 -*-

"""倒排索引

对所有的文档信息都在inverted_file字中: {单词: [包含这个单词的文档id]}

"""



import logging
import pprint

try:
    import cPickle as pickle
except ImportError:
    import pickle

#日志输出配置
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)



documents = [] #所有文档的列表
words = set() #所有单词的集合
inverted_file = dict()

def load_file(filename):
    """ 导入文档到文档列表中
    """
    global documents
    with open(filename, 'r') as f:
        cnt = 0
        for c in f.readlines():
            cnt += 1
            documents.append(c)
        logging.info("已经加载了{0}个文档!".format(cnt))

def get_words():
    """ 得到所有单词的集合
    """
    for d in documents:
        dlist = d.split(' ')
        for k in dlist:
            if k.strip() != '':
                words.add(k.strip())

def build_inverted_file():
    """建立倒叙索引
    
    * 存储该索引的数据结构为python字典
    * 格式类似:
       {
            'I': [0, 1, 3, 8],
            'a': [1, 3, 7],
            'boy': [2]
       }
       表示单词和包含单词id的文档id
    """
    for c in words:
        inverted_file[c] = []
    
    for w, d in inverted_file.items():
        for i in range(len(documents)):
            if w in documents[i]:
                d.append(i)

def save_it():
    """保存文档和倒排索引
    """
    with open('tmp/documents.list', 'w') as f:
        pickle.dump(documents, f)
    with open('tmp/inverted_file.dict', 'w') as f:
        pickle.dump(inverted_file, f)


def main():
    load_file('dataset.txt')
    get_words()
    build_inverted_file()
    pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(inverted_file)
    save_it()


if __name__ == '__main__':
    main()


