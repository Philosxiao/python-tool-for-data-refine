#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:29:32 2019

@author: philos
"""

import numpy as np
import os, os.path
import cv2

 
rgb_dic="/home/philos/Desktop/dataset/robot_catch_dateset/all_color/"
depth_dic="/home/philos/Desktop/dataset/robot_catch_dateset/handled_depth/"
result_dic="/home/philos/Desktop/dataset/robot_catch_dateset/handled_RGBD/"

rgb_file_list = os.listdir(rgb_dic)
for rgb_file in rgb_file_list:
	#去掉末尾的换行符，name = input_data_train[i]
    if not (rgb_file[-4:]==".jpg" or rgb_file[-4:]==".png"):
        continue
    depth_path=rgb_file.replace(".png",".jpg")
    rgb_file_path=rgb_dic+rgb_file
    depth_file_path=(depth_dic+depth_path).replace("color","dep")
    if not os.path.exists(depth_file_path):
        depth_file_path=(depth_dic+depth_path).replace("color","depth")
        if not os.path.exists(depth_file_path):
            print("no depth exist!")
            continue
	#用opencv读取图片
    rgb = cv2.imread(rgb_file_path)
    disp = cv2.imread(depth_file_path,0)
    #(B, G, R) = cv2.split(rgb)
    #rgbd=[rgb,disp]
    rgbd=cv2.merge([rgb, disp])
	
    result_path=str(result_dic+rgb_file.replace(".png",".jpg"))
	#保存的RGBD图片文件名为RGB图片的文件名
    cv2.imwrite(result_path,rgbd)
print ("success")