#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:54:35 2019

@author: philos
"""
import json
import os
import shutil
from PIL import Image, ImageDraw
import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import numpy as np

import cv2
            
base_dir='/home/philos/Desktop/image_make/wrong_case/'




file_list = os.listdir(base_dir)
for file in file_list:
        #jpg_file=str(file).replace(".json",".jpg")
    if (file[-5:]==".jpeg" ):
        jpg_dic=base_dir+file
        json_file= jpg_dic.replace(".jpeg",".json")            
        image = cv2.imread(jpg_dic)
        with open(json_file) as f:                                         
            dic_info=json.load(f)
            dic_now=jpg_dic.replace(".jpeg","_mask.jpg") 
            for  i in range(len(dic_info["shapes"])): 
                im = np.zeros(image.shape[:2], dtype = "uint8")
                b  = []
                for (x,y) in dic_info["shapes"][i]["points"]:                        
                    b.append([x,y])        
                pts=np.zeros([len(b),2], dtype = np.int32)
                pts=np.array(b)
                pts = pts.reshape((-1,1,2))
                cv2.polylines(im, [pts], 1, 255)
                cv2.fillPoly(im, [pts], 255)
                cv2.imwrite(dic_now , im)   
                dic_now=dic_now.replace(".jpg","_mask.jpg")
# =============================================================================
# mask = im
# #cv2.imshow("Mask", mask)
# masked = cv2.bitwise_and(image, image, mask=mask)
# =============================================================================
