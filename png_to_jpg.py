#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:35:20 2018

@author: captain
"""

import json
import os
from PIL import Image,ImageDraw
#import cv2
import numpy



base_dir='/home/philos/Desktop/dataset/robot_catch_dateset/all_color/'

out_dir='/home/philos/Desktop/dataset/robot_catch_dateset/handled_RGBD/'
need_filp_copy=1


def main():
    file_list = os.listdir(base_dir)
    count=0
    for file in file_list:
        #jpg_file=str(file).replace(".json",".jpg")
        if (file[-4:]==".png" ):
            #and os.path.exists()\
            im = Image.open(base_dir+file)
            file=file.replace(".png" ,".jpg")

            
            im.save(out_dir+file.replace(".png",".jpg"))   
            count=count+1
                        
                        
                        


if __name__ == '__main__':
    main()