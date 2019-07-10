#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 12:09:50 2018

@author: captain
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:59:15 2018

@author: captain
"""
import json
import os
import shutil
from PIL import Image

base_dir='/home/philos/Desktop/dataset/robot_catch_dateset/all_color/'
out_dir= '/home/philos/Desktop/dataset/robot_catch_dateset/handled_RGBD/'
#"package","box",
labels=["t"]

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
                    print(jpg_file)                    
                    break
            jpg_file_path=str(base_dir+jpg_file)        
            text_file_path=str(out_dir+str(json_file).replace(".json",".txt"))
            
            if (os.path.exists(text_file_path)):
                os.remove(text_file_path)
            
            saveFile = open(text_file_path, 'w')  
            
            print(os.path.exists(jpg_file_path))
            print(str(jpg_file_path))
            img=Image.open(jpg_file_path)
            size=img.size
            
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
                    print (box)           
                    print(jpg_file)
                    tar_size=convert(size, box)
                    num=int(labels.index(label))
                    saveFile.write(str(num) + " " +str(tar_size[0])+" "+str(tar_size[1])+" "+str(tar_size[2])+" "+str(tar_size[3])+" "+ '\n')
            saveFile.close()  # 操作完文件后一定要记得关闭，释放内存资源            

if __name__ == '__main__':
    main()