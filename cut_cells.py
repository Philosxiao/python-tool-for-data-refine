#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:50:58 2019

@author: philos
"""

import json
import os
import shutil
from PIL import Image

base_dir='/home/philos/Desktop/dataset/robot_catch_dateset/all_color/'
out_dir= '/home/philos/Desktop/dataset/robot_catch_dateset/cell_image/'
#"package","box",
labels=["t"]




def crop_image(input_image, output_image, start_x, start_y, width, height):
    input_img = Image.open(input_image)
    box = (start_x, start_y, start_x + width, start_y + height)
    output_img = input_img.crop(box)
    output_img.save(output_image +".jpg")






def convert(size, box):
    dw = 1./size[0]#pic's dw
    dh = 1./size[1]
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
    file_list = os.listdir(base_dir)
    image_num=0
    for file in file_list:
        #jpg_file=str(file).replace(".json",".jpg")
        if (file[-5:]==".json" ):
            json_file=file
            #and os.path.exists()
            jpg_file= file.replace(".json",".jpg")
            if not os.path.exists(base_dir+jpg_file):
                jpg_file=file.replace(".json",".png")
                if not os.path.exists(base_dir+jpg_file):
                    print("warnning! one json has no jpg or png file associated!!")
                    print (jpg_file)
                    break
            jpg_file_path=str(base_dir+jpg_file)        
            text_file_path=str(out_dir+str(json_file).replace(".json",".txt"))
            
            if (os.path.exists(text_file_path)):
                os.remove(text_file_path)
                 
            img=Image.open(jpg_file_path)
            size=img.size
            image_num=image_num+1
            j=0
            with open(base_dir+file) as f:                            
                dic_info=json.load(f)
                for  i in range(len(dic_info["shapes"])):                    
                    min_x=5000
                    min_y=5000
                    max_y=0
                    max_x=0    
                    for (x,y) in dic_info["shapes"][i]["points"]:                        
                        if (x<min_x):   min_x=x
                        if (y<min_y):   min_y=y
                        if (x>max_x):   max_x=x
                        if (y>max_y):   max_y=y
                    box=[min_x,max_x,min_y,max_y]
                    print(dic_info["shapes"][i]["label"])
                    label=dic_info["shapes"][i]["label"]
                    crop_image(base_dir+jpg_file,out_dir+jpg_file[:-5]+"_"+str(i)+"_"+str(j)+".jpg", min_x,min_y,max_x-min_x,max_y-min_y)


if __name__ == '__main__':
    main()