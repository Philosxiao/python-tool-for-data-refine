#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 18:01:46 2018

@author: captain
"""
import os
from PIL import Image
import numpy as np
import shutil


import numpy as np
import cv2

base_dir='/home/captain/MVViewer/pictures/'
dest_dir='/home/captain/Desktop/trainning_date_from_dowmroom/'


def main():
    file_list = os.listdir(base_dir)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)   
    for file in file_list:
        #jpg_file=str(file).replace(".json",".jpg")
        if (file[-4:]==".jpg" or file[-4:]==".bmp"):
            print("tracking "+file)
            
            # 首先以灰色读取一张照片
            src = cv2.imread(base_dir+file, 0)
            # 然后用ctvcolor（）函数，进行图像变换。
            src_RGB = cv2.cvtColor(src, cv2.COLOR_GRAY2RGB)
            #print(src_RGB.shape)
            if(file[-4:]==".bmp"):
                file=file.replace(".bmp" ,".jpg")
            cv2.imwrite(dest_dir+file,src_RGB)
            
            
            
# =============================================================================
#             #and os.path.exists()
#             im=Image.open(base_dir+file)
#             L = im.convert('P')   #转化为灰度图
#             if(file[-4:]==".bmp"):
#                 file=file.replace(".bmp" ,".jpg")
#             L.save(dest_dir+file)
# =============================================================================
            txt_file=file.replace(".jpg",".txt")
            
            if(os.path.exists(base_dir+txt_file)):
                shutil.copyfile( base_dir+txt_file, dest_dir+txt_file) 
            
            else:
                print("some image lost txt")
               
                

if __name__ == '__main__':
    main()
