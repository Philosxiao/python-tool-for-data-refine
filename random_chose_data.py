#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:49:16 2019

@author: philos
"""
from sklearn.model_selection import train_test_split
import os

#X:含label的数据集：分割成训练集和测试集
#test_size:测试集占整个数据集的比例


 
# 生成200个句子，前100个和后100个类别分别对应1和2


in_dir='/home/philos/Desktop/dataset/robot_catch_dateset/data_enhance/list/'


f = open(in_dir+'data.txt','r')
result = list()
for line in open(in_dir+'data.txt'):
    line = f.readline()
    line=line[:-1]
    #print line
    result.append(line)
print (result)
f.close()  

# 随机抽取20%的测试集
X_train, X_test, y_train, y_test = train_test_split(result, result, test_size=0.2)
print (len(X_train), len(X_test))
 

if  os.path.isfile(in_dir+"train.txt"):
    os.remove(in_dir+"train.txt")
os.mknod(in_dir+"train.txt")
out_train_txt=open(in_dir+"train.txt", 'w')
# 查看句子和标签是否仍然对应
for i in range(len(X_train)):
    out_train_txt.write(X_train[i]+ '\n')    

if  os.path.isfile(in_dir+"test.txt"):
    os.remove(in_dir+"test.txt")
os.mknod(in_dir+"test.txt")
out_test_txt=open(in_dir+"test.txt", 'w')     
    
for j in range(len(X_test)):
    out_test_txt.write(X_test[j]+ '\n')   
 

