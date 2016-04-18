#!/usr/bin/env python
#coding:utf-8

import itertools
import random

ftxt = open('result.txt','w')

class Apriori:
    def __init__(self,min_sup=2,data={}):
        self.data = data
        self.min_sup = min_sup

    #初始化，扫描对每个项集进行支持度计数
    def find_frequent_itemsets(self):
        FreqDic = {}    #遍历建立字典FreqDic，键为商品类型，值为商品数量
        for event in self.data:
            for item in self.data[event]:
                if item in FreqDic:
                    FreqDic[item] += 1
                else:
                    FreqDic[item] = 1
        L1 = []
        # print FreqDic
        for itemset in FreqDic:
            if itemset >= self.min_sup:
                L1.append([itemset])
        return L1

    #剪枝，判断是否是非频繁子集
    def has_infrequent_subset(self,c,L_first,k):
        subsets = list(itertools.combinations(c,k-1))
        for each in subsets:
            each = list(each)
            if each not in L_first:
                return True
        return False

    def apriori_gen(self,L_first):
        k = len(L_first[0]) + 1
        Ck = []
        #连接
        for itemset1 in L_first:
            for itemset2 in L_first:
                flag = 0
                for i in range(k-2):
                    if itemset1[i] != itemset2[i]:
                        flag = 1
                        break
                if flag == 1:
                    continue
                if itemset1[k-2] < itemset2[k-2]:
                    c = itemset1 + [itemset2[k-2]]
                else:
                    continue

                if self.has_infrequent_subset(c,L_first,k):
                    continue
                else:
                    Ck.append(c)
        return Ck

    def do(self):
        L_first = self.find_frequent_itemsets()
        #迭代
        while L_first != []:
            Ck = self.apriori_gen(L_first)
            FreqDic = {}
            # print FreqDic
            for event in self.data:
                for c in Ck:
                    if set(c) <= set(self.data[event]):
                        if tuple(c) in FreqDic:
                            FreqDic[tuple(c)]+=1
                        else:
                            FreqDic[tuple(c)]=1
            Lk = []
            # for event in FreqDic:
            #     if FreqDic[event] >= self.min_sup:
            #         print event,FreqDic[event]
            for c in FreqDic:
                if FreqDic[c] >= self.min_sup:
                    Lk.append(list(c))
            L_first = Lk
            u = 0
            while(u<len(L_first)):
                if L_first != []:
                    print L_first[u]
                u += 1
        return 'complete!'


Data = {'T100':['I1','I2','I5'],
        'T200':['I2','I4'],
        'T300':['I2','I3'],
        'T400':['I1','I2','I4'],
        'T500':['I1','I3'],
        'T600':['I2','I3'],
        'T700':['I1','I3'],
        'T800':['I1','I2','I3','I5'],
        'T900':['I1','I2','I3']}

#随机产生10组不同数量的数据作为商店的事务数据
Data2 = {}
Data2['T100'] = random.sample(range(10,20),random.randrange(1,10))
Data2['T200'] = random.sample(range(10,20),random.randrange(1,10))
Data2['T300'] = random.sample(range(10,20),random.randrange(1,10))
Data2['T400'] = random.sample(range(10,20),random.randrange(1,10))
Data2['T500'] = random.sample(range(10,20),random.randrange(1,10))
Data2['T600'] = random.sample(range(10,20),random.randrange(1,10))
Data2['T700'] = random.sample(range(10,20),random.randrange(1,10))
Data2['T800'] = random.sample(range(10,20),random.randrange(1,10))
Data2['T900'] = random.sample(range(10,20),random.randrange(1,10))
Data2['T1000'] = random.sample(range(10,20),random.randrange(1,10))

print '书上的范例：'
a=Apriori(data=Data)
print a.do()
print '='*50
print '随机数：'
b = Apriori(data=Data2)
print b.do()