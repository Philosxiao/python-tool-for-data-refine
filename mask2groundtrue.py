#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:55:57 2018

@author: captain

"""
import json
import os
import shutil
from PIL import Image
import cv2

base_dir='/home/captain/Desktop/big_paper_work/dataset/1d_barcode_extended_plain/Original/' 
mask_dir='/home/captain/Desktop/big_paper_work/dataset/1d_barcode_extended_plain/Detection/' 
labels=["package","box","code"]

def convert(size, box):
    dw = 1./size[1]#pic's dw
    dh = 1./size[0]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    y = y*dh
    w = w*dw
    h = h*dh
    return (x,y,w,h)

def main():
    file_list = os.listdir(mask_dir)
    for file in file_list:
        if (file[-4:]==".png" ):
            
            jpg_file= file.replace(".png",".jpg")
            jpg_file_path=str(base_dir+jpg_file)
            if not(os.path.exists(jpg_file_path)):
                continue

            img = cv2.imread(mask_dir+file,cv2.IMREAD_GRAYSCALE)

            text_file_path=str(base_dir+str(file).replace(".png",".txt"))
            if (os.path.exists(text_file_path)):
                os.remove(text_file_path)
            saveFile = open(text_file_path, 'w')  
            
            size=img.shape

            (_, cnts, _) = cv2.findContours(img.copy(), 
                 cv2.RETR_LIST, 
                 cv2.CHAIN_APPROX_SIMPLE)
           # print(cnts)
            for mask_single in cnts:
                min_x=5000
                min_y=5000
                max_y=0
                max_x=0
                for points in mask_single:    
                    for(x,y) in points:    
                        if(x>480 ): print(x,y)
                        if (x<min_x):   min_x=x
                        if (y<min_y):   min_y=y
                        if (x>max_x):   max_x=x
                        if (y>max_y):   max_y=y
                box=[min_x,max_x,min_y,max_y]
                label="code"
                tar_size=convert(size, box)
                num=int(labels.index(label))
                saveFile.write(str(num) + " " +str(tar_size[0])+" "+str(tar_size[1])+" "+str(tar_size[2])+" "+str(tar_size[3])+" "+ '\n')
            saveFile.close()  # 操作完文件后一定要记得关闭，释放内存资源            
           
                             

if __name__ == '__main__':
    main()