#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 17:49:13 2018

@author: captain
"""

import json
import os
import shutil
from PIL import Image

base_dir='/home/captain/Desktop/darknet_from_lin/data/box/images/001/color/'

labels=["package","box"]


def main():
    file_list = os.listdir(base_dir)
    for file in file_list:
        #jpg_file=str(file).replace(".json",".jpg")
        if (file[-4:]==".txt" ):
            data=''
            with open(base_dir+file,'r') as f:
                                
                for line in f.readlines():
                    line.lstrip()
                    every=line.split(" ")                    
                    #print(every)
                    print("end")
                    print(every[0])
                    if (every[0]==str(2)):   
                        every[0]=str(1)
                        
                    for i in range(len(every)):
                        data+=str(every[i])+" "
                    data+="\n"
                    #str(" ".join(str(a)for  a in every))
                print(data)
            with open(base_dir+file,'w') as f:   
                f.write(data)
                    
                
                             

if __name__ == '__main__':
    main()