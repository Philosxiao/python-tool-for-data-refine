o#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:59:15 2018

@author: captain
"""

import json
import os
import shutil
import PIL.Image as Image
import random 

in_dir='/home/philos/Desktop/dataset/SANYI_count/data_enhance/'
out_dir='/home/philos/Desktop/dataset/SANYI_count/'

train_test_data_ratio=0.8

def main():
    filelist = os.listdir(in_dir) 
    random.shuffle(filelist)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)      
    if  os.path.isfile(out_dir+"train_data.txt"):
        os.remove(out_dir+"train_data.txt")
    os.mknod(out_dir+"train_data.txt")
    out_train_txt=open(out_dir+"train_data.txt", 'w')
    
    if  os.path.isfile(out_dir+"test_data.txt"):
        os.remove(out_dir+"test_data.txt")
    os.mknod(out_dir+"test_data.txt")
    out_test_txt=open(out_dir+"test_data.txt", 'w')
    
    for i in range(len(filelist)):
        if(filelist[i][-4:]=='.txt'): continue
        base_name=os.path.splitext(os.path.basename(filelist[i]))[0]
        if(i<train_test_data_ratio*len(filelist)):
            out_train_txt.write(in_dir+base_name+".jpg" + '\n')
        else:
            out_test_txt.write(in_dir+base_name +".jpg" + '\n')



    
    
    
# =============================================================================
#     for file in filelist:
#         if (file[-4:]=='.jpg' ):#and (os.path.exists(in_dir+file.replace(".jpg",".txt")) or os.path.exists(in_dir+file.replace(".bmp",".txt"))): 
#             picname=str(file)
#         else: continue
#              #path = os.path.join(path, list[i])
#         out_train_txt.write(in_dir+picname + '\n')    
#         print (in_dir+picname)
#                     
# =============================================================================
if __name__ == '__main__':
    main()
