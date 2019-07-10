#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 20:43:35 2018

@author: captain
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:50:52 2018

@author: captain
"""


import os
import shutil
import PIL.Image as Image
import cv2



base_dir='/home/philos/Desktop/dataset/robot_catch_dateset/cell_image/' 
out_dir= '/home/philos/Desktop/dataset/robot_catch_dateset/cell_image/data_labeled/'


def main():

    list = os.listdir(base_dir)    
    for file in list:
        if (file[-8:]=='.jpg.jpg'): #and os.path.exists(from_dir+file.replace('.png','.jpg'))):  
            json_file = file.replace(".jpg.jpg",".jpg.json")
            if os.path.exists(base_dir+json_file):
                shutil.copy(base_dir+file,out_dir+file)
                shutil.copy(base_dir+json_file,out_dir+json_file)
            #shutil.copy(from_dir+file,out_dir+file) 
        else: continue
             #path = os.path.join(path, list[i])
       
                    
if __name__ == '__main__':
    main()