#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:09:17 2018

@author: captain
"""
import json
import os
from PIL import Image,ImageDraw
#import cv2
import numpy



base_dir='/home/captain/Desktop/change_jpg_test/'

out_dir='/home/captain/Desktop/change_jpg_test/after_change/'
need_filp_copy=1


def main():
    file_list = os.listdir(base_dir)
    count=0
    for file in file_list:
        #jpg_file=str(file).replace(".json",".jpg")
        if (file[-5:]==".json" ):
            #and os.path.exists()
            jpg_file= file.replace(".json",".jpg")
            jpg_file_path=str(base_dir+jpg_file)                
            if (file[-5:]==".json" and os.path.exists(jpg_file_path)):
                im = Image.open(jpg_file_path).convert("RGBA")
                imArray = numpy.asarray(im)
            with open(base_dir+file) as f:                            
                dic_info=json.load(f)
                for  i in range(len(dic_info["shapes"])):
                    label_name=dic_info["shapes"][i]["label"]
                    polygon=[]                    
                    for (x,y) in dic_info["shapes"][i]["points"]:                        
                        polygon.append((x,y))

                    # create mask (zeros + circle with ones)
                    maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
                    ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
                    mask = numpy.array(maskIm)
                        
                    # assemble new image (uint8: 0-255)
                    newImArray = numpy.empty(imArray.shape,dtype='uint8')
                    # colors (three first columns, RGB)
                    newImArray[:,:,:3] = imArray[:,:,:3]
                    # transparency (4th column)
                    newImArray[:,:,3] = mask*255          
                    # back to Image from numpy
                    newIm = Image.fromarray(newImArray, "RGBA")
                    newIm.save(out_dir+label_name+str(count)+".png") 
                    result = Image.new("RGB", newIm.size, (0, 0, 0))
                    result.paste(newIm, mask=newIm.split()[3]) # 3 is the alpha channel
                    result.save(out_dir+label_name+str(count)+".jpg")
                    count=count+1
                        

           
                             

if __name__ == '__main__':
    main()