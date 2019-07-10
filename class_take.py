#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 23:43:34 2018

@author: captain
"""

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

base_dir='/home/captain/Desktop/classify_data/'

labels=["package","box"]



def main():
    file_list = os.listdir(base_dir)
    num=0
    for file in file_list:
        #jpg_file=str(file).replace(".json",".jpg")
        new_name=str(file)
        if (file[-4:]==".jpg" ):
            #and os.path.exists()
            json_file= file.replace(".jpg",".json")     
            txt_file=file.replace(".jpg",".txt")
            
            if (os.path.exists(base_dir+json_file)):
                with open(base_dir+json_file) as f:                            
                    dic_info=json.load(f)
                    for  i in range(len(dic_info["shapes"])):                    
                        label=dic_info["shapes"][i]["label"]
                        if (label=="box"):
                            new_name="box_"+str(num)+".jpg"
                        if (label=="package"):
                            new_name="package_"+str(num)+".jpg"
            else :
                if(os.path.exists(base_dir+txt_file)):
                    with open(base_dir+txt_file,'r') as f:
                        for line in f.readlines():
                            line.lstrip()
                            every=line.split(" ")                    
                            if (every[0]==str(2)):
                                new_name="box_"+str(num)+".jpg"
                            if (every[0]==str(0)):
                                new_name="package_"+str(num)+".jpg"

                                
            os.rename(base_dir+file,base_dir+new_name)
            if(os.path.exists(base_dir+txt_file)):
                os.remove(base_dir+txt_file)
            if(os.path.exists(base_dir+json_file)):
                os.remove(base_dir+json_file)
            num=num+1
            
               
           
                             

if __name__ == '__main__':
    main()