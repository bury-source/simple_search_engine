#!/usr/bin/python
# -*- coding:utf-8 -*-

"""倒排索引

对所有的文档简历这样的字典: {单词: [包含这个单词的文档id]}
"""


import pprint

documents = [] #所有文档的列表
words = set() #所有单词的集合
inverted_file = dict()

def load_file(filename):
    """ 导入文档到文档列表中
    """
    global documents
    with open(filename, 'r') as f:
        for c in f.readlines():
            documents.append(c)

def get_words():
    """ 得到所有单词的集合
    """
    for d in documents:
        dlist = d.split(' ')
        for k in dlist:
            if k.strip() != '':
                words.add(k.strip())

def build_inverted_file():
    for c in words:
        inverted_file[c] = []
    
    for w, d in inverted_file.items():
        for i in range(len(documents)):
            if w in documents[i]:
                d.append(i)





def main():
    load_file('dataset.txt')
    get_words()
    build_inverted_file()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(inverted_file)


if __name__ == '__main__':
    main()


