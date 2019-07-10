#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:19:48 2019

@author: philos
"""

import os
import shutil
import PIL.Image as Image
import cv2

base_dir='/home/philos/Desktop/dataset/robot_catch_dateset/cell_image/' 
refine_dic='/home/philos/Desktop/dataset/robot_catch_dateset/cell_image/image_after_refine/'
out_dir= '/home/philos/Desktop/dataset/robot_catch_dateset/cell_image/data_final/'


def main():    
    num=0
    for i in range(270):
        list = os.listdir(refine_dic+str(i)+"/output/")    
        for file in list:
            if file[0]!='_':
                #print("find original "+file)
                mask_name=file.replace(str(i)+'_original_'+str(i),"_groundtruth_(1)_"+str(i)+'_'+str(i))
                print(mask_name)
                img=cv2.imread(refine_dic+str(i)+"/output/"+mask_name,cv2.IMREAD_GRAYSCALE)
                #img.setTo(1,img=255)
                ret1,th1 = cv2.threshold(img,188,255,cv2.THRESH_BINARY)
                th1[th1>188]=1
               # th1.setTo(1,th1=255)
                shutil.copyfile(refine_dic+str(i)+"/output/"+file,out_dir+"data_refined"+str(num)+".jpg")
                cv2.imwrite(out_dir+"data_refined"+str(num)+".png", th1)
                num=num+1
            

               
                

                
                
                #print(mask_name)
# =============================================================================
#                 if(os.path.exists(refine_dic+str(i)+"/output/"+mask_name)):
#                     print("right")
# =============================================================================
# =============================================================================
#             if (file[-8:]=='.jpg.jpg'): #and os.path.exists(from_dir+file.replace('.png','.jpg'))):  
#                 json_file = file.replace(".jpg.jpg",".jpg.json")
#                 if os.path.exists(base_dir+json_file):
#                     shutil.copy(base_dir+file,out_dir+file)
#                     shutil.copy(base_dir+json_file,out_dir+json_file)
#                     #shutil.copy(from_dir+file,out_dir+file) 
#                     else: continue
#                 #path = os.path.join(path, list[i])
# =============================================================================
       
                    
if __name__ == '__main__':
    main()