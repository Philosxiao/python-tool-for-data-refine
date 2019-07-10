#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:40:13 2019

@author: philos
"""

#!/usr/bin/env python

#import argparse
import json
import numpy as np
import cv2
import os


from labelme import utils


def gen_mask(json_file):

    data = json.load(open(json_file))
    
    #img = utils.img_b64_to_array(data['imageData'])

    shape=[data['imageHeight'],data['imageWidth']]
    lbl, lbl_names = utils.labelme_shapes_to_label(shape, data['shapes'])

    mask=[]
    class_id=[]
    
    for i in range(len(lbl_names)): # 跳过第一个class（默认为背景）
        mask.append((lbl==i).astype(np.uint8)) # 解析出像素值为1的对应，对应第一个对象 mask 为0、1组成的（0为背景，1为对象）
        class_id.append(i) # mask与clas 一一对应

    mask=np.transpose(np.asarray(mask,np.uint8),[1,2,0]) # 转成[h,w,instance count]
    class_id=np.asarray(class_id,np.uint8) # [instance count,]
   # class_name=lbl_names[1:] # 不需要包含背景
    
    retval, im_at_fixed = cv2.threshold(mask[:,:,0], 0, 255, cv2.THRESH_BINARY)
    #im_at_fixed.setTo(1,im_at_fixed=255)
    return mask[:,:,0]
    
    
in_dir='/home/philos/Desktop/image_make/example/'
out_dir='/home/philos/Desktop/image_make/example/'


if __name__ == '__main__':
    filelist = os.listdir(in_dir)    
# =============================================================================
#     if not os.path.exists(out_dir):
#         os.makedirs(out_dir)      
#     if  os.path.isfile(out_dir+"data.txt"):
#         os.remove(out_dir+"data.txt")
# =============================================================================
    for file in filelist:
        if (file[-5:]=='.json'):#and (os.path.exists(in_dir+file.replace(".jpg",".txt")) or os.path.exists(in_dir+file.replace(".bmp",".txt"))): 
            json_name=str(in_dir+file)
            mask=gen_mask(json_name)
            png_file= json_name.replace(".json",".png")
            cv2.imwrite(png_file, mask)
    
    
   