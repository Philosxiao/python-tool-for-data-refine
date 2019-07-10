#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:19:03 2019

@author: philos
"""

import json
import glob
import random 
import os,sys,shutil

import cv2 
import numpy as np 


source_image_label_dic=glob.glob('/home/philos/Desktop/dataset/SANYI_count/color/*.jpg')
backfround_pics=glob.glob('/home/philos/Desktop/background_image/*.jpg')
output_dir="/home/philos/Desktop/dataset/SANYI_count/background_changed/"


#background time to chose
change_time=2

if(len(backfround_pics)<change_time): change_time=len(backfround_pics)


for source_pic_path in source_image_label_dic:    
    dir_file_name=os.path.splitext(source_pic_path)[0]
    base_name=os.path.splitext(os.path.basename(source_pic_path))[0]
    json_path=dir_file_name+".json"
    
    if(os.path.exists(json_path)==False): continue
    
    with open(json_path,'r',encoding='utf-8') as json_data:
        
        cur_json_anno = json.load(json_data)
        polygons = [r['points'] for r in cur_json_anno['shapes']]
        labels=[r['label'] for r in cur_json_anno['shapes']]
        types = [r['shape_type'] for r in cur_json_anno['shapes']]       
        src = cv2.imread(source_pic_path) 
        image_shape=src.shape[:-1]
        maks_roi = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY) 
        maks_roi.fill(0) 
        
        for i in range(len(polygons)):        
            if(types[i] == "polygon"):
                array=np.array([polygons[i]])
                cv2.fillPoly(maks_roi, array,255)
            if(types[i] == "rectangle"):
                rec_polygon=[[polygons[i][0][0],polygons[i][0][1]],[polygons[i][0][0],polygons[i][1][1]],
                            [polygons[i][1][0],polygons[i][1][1]],[polygons[i][1][0],polygons[i][0][1]]]
                array=np.array([rec_polygon[i]])
                cv2.fillPoly(maks_roi, array,255)
                
        mask_inv = cv2.bitwise_not(maks_roi)
        
        random.shuffle(backfround_pics)

        for i in range(change_time):
            temp_background_image_path=backfround_pics[i]
            temp_back_ground = cv2.imread(temp_background_image_path)
            temp_back_ground_resize = cv2.resize(temp_back_ground,(image_shape[1],image_shape[0]),interpolation=cv2.INTER_NEAREST)
            
            img_bg = cv2.bitwise_and(temp_back_ground_resize,temp_back_ground_resize,mask = mask_inv) 
            img_fg = cv2.bitwise_and(src,src,mask = maks_roi) 
            dst = cv2.add(img_bg,img_fg)
            cv2.imwrite(output_dir+base_name+"_background_extend_"+str(i)+".jpg",dst)
            newjson_path=output_dir+base_name+"_background_extend_"+str(i)+".json"
            shutil.copyfile(json_path,newjson_path)