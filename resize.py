#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 23:31:36 2018

@author: captain
"""

#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-

import os
from os import walk, getcwd
from PIL import Image
import cv2

classes = ['_','_',"box"]

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
    
    
"""-------------------------------------------------------------------""" 

""" Configure Paths"""   
mypath = "Labels/001/"
outpath = "Labels/converted/"

cls = "box"
if cls not in classes:
    exit(0)
cls_id = classes.index(cls)

wd = getcwd()
list_file = open('%s/%s_list.txt'%(wd, cls), 'w')

""" Get input text file list """
txt_name_list = []
for (dirpath, dirnames, filenames) in walk(mypath):
    txt_name_list.extend(filenames)
    break
txt_name_list.sort()
print(txt_name_list)

""" Process """
for txt_name in txt_name_list:
    # txt_file =  open("Labels/stop_sign/001.txt", "r")
    
    """ Open input text files """
    txt_path = mypath + txt_name
    print("Input:" + txt_path)
    txt_file = open(txt_path, "r")
    lines = txt_file.read().split('\n')   #for ubuntu, use "\r\n" instead of "\n"
    
    """ Open output text files """
    txt_outpath = outpath + txt_name
    print("Output:" + txt_outpath)
    txt_outfile = open(txt_outpath, "w")
    
    
    fp = open('/home/captain/dataset_box/pic_cap/box1_train/box1_train 001.jpg')
    tarim = Image.open('/home/captain/dataset_box/pic_cap/box1_train/box1_train 001.jpg')
    fp.close()
    tar_size = tarim.size
    
    out_train_txt=open('/home/captain/dataset_box/pic_cap/'+"train_box2.txt", 'w')
    """ Convert the data to YOLO format """
    ct = 0
    for line in lines:
        #print('lenth of line is: ')
        #print(len(line))
        #print('\n')
        if(len(line) >= 4):
            ct = ct + 1
            print(line + "\n")
            elems = line.split(' ')
            print(elems)
            xmin = elems[0]
            xmax = elems[2]
            ymin = elems[1]
            ymax = elems[3]          
            
            #
            img_path = str('%s/Images/001/color/%s.jpg'%(wd,os.path.splitext(txt_name)[0]))
            #t = magic.from_file(img_path)
            #wh= re.search('(\d+) x (\d+)', t).groups()
            im=cv2.imread(img_path)
            show=im.shape
            w= int(im.shape[0])
            h= int(im.shape[1])
            
            tar = cv2.resize(im, tar_size, interpolation=cv2.INTER_AREA)  
            savepath='/home/captain/dataset_box/pic_cap/box2_train/'
            #cv2.imwrite(savepath+txt_name.replace('.txt','.jpg'),tar)
            out_train_txt.write(savepath+txt_name + '\n')
            
            
            
            
          
         

# =============================================================================
#     """ Save those images with bb into list"""
#     if(ct != 0):
#         list_file.write('%s/images/001/color/%s.jpg\n'%(wd, os.path.splitext(txt_name)[0]))
# =============================================================================
                
list_file.close()       

