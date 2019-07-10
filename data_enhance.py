#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:23:38 2018

@author: captain
"""

#encoding:utf-8
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import numpy as np
import os


base_dir='/home/captain/Desktop/change_jpg_test/after_change/'
out_dir='/home/captain/Desktop/change_jpg_test/after_enhance/'
file_list = os.listdir(base_dir)
for file in file_list:
# 加载图像，并转化为numpy的array
    if (file[-4:]==".jpg" ):
        print('[INFO] loading example image...')
        image = load_img(base_dir+file)
        image = img_to_array(image)
#增加一个维度
        image = np.expand_dims(image,axis = 0) #在0位置增加数据，主要是batch size

        aug = ImageDataGenerator(
                rotation_range=30,       # 旋转角度
                width_shift_range=0.1,   # 水平平移幅度
                height_shift_range= 0.1, # 上下平移幅度
                shear_range=0.2,         # 逆时针方向的剪切变黄角度
                zoom_range=0.2,          # 随机缩放的角度
                horizontal_flip=True,    # 水平翻转
                fill_mode='nearest'      # 变换超出边界的处理
                )
# 初始化目前为止的图片产生数量
        total = 0

        print("[INFO] generating images...")
        imageGen = aug.flow(image,batch_size=1,save_to_dir=out_dir,save_prefix=file.replace(".jpg",""),save_format='jpg')
        for image in imageGen:
            total += 1
            # 只输出10个案例样本
            if total == 10:
                break