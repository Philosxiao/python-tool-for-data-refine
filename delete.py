#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:50:52 2018

@author: captain
"""

import json
import os
import shutil
import PIL.Image as Image




classes = ["package","box","code"]
in_dir='/home/philos/Desktop/dataset/robot_catch_dateset/cell_image/data_final/'
out_dir='/home/captain/Desktop/data_from_jindong/11.16/'




#Warnning!!!!!!  run only in copy date!!!!!!
def main():

    list = os.listdir(in_dir)    
    for i in range(0, len(list)):
        if list[i][-5:]=='.json': 
            os.remove(in_dir+list[i])
        else: continue
             #path = os.path.join(path, list[i])
       
                    
if __name__ == '__main__':
    main()