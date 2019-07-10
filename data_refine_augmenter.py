import json
import glob
import os
import skimage
import imgaug as ia
from imgaug import augmenters as iaa
import random 
#created by jiazhao

def convert(height,width, x1,x2,y1,y2):
    dw = 1./width
    dh = 1./height
    x = (x1 + x2)/2.0
    y = (y1 + y2)/2.0
    w = x2 - x1
    h = y2 - y1
    x = x*dw
    y = y*dh
    w = w*dw
    h = h*dh
    return x,y,w,h

def drwa_rectangle(image,x,y,w,h):
    image_height=image.shape[0]
    image_width= image.shape[1]
    center_x=image_width*x
    center_y=image_height*y
    height=image_height*h
    width=image_width*w
    x1=int(center_x-width/2)
    x2=int(center_x+width/2)
    y1=int(center_y-height/2)
    y2=int(center_y+height/2)
    rr,cc=skimage.draw.rectangle(start=(x1,y1),end=(x2,y2),shape=[int(height),int(width)])
    print("point",x1," ",y1," ",x2," ",y2," ")
    image[rr, cc] = [255,0,0]
    skimage.io.imshow(image)
    skimage.io.show()
    #return image

def decide_class(label):
    if label=="defect":
        return 0
    elif label=="gudinglianjjiejian":
        return 1
    elif label=="mifengxianquan":
        return 2
    elif label=="chuangganqi":
        return 3
    elif label=="chuanganqi":
        return 3
    elif label=="xinpian":
        return 4
    elif label=="kaiguananniu":
        return 5



all_pics=glob.glob('/home/philos/Desktop/surface_defect/*.jpg')
output_dir="/home/philos/Desktop/surface_defect/enhance/"

count=0
class_num=0

for pic_path in all_pics:
    
    
    dir_file_name=os.path.splitext(pic_path)[0]
    base_name=os.path.splitext(os.path.basename(pic_path))[0]
    json_path=dir_file_name+".json"
    
    #read json file
    with open(json_path,'r',encoding='utf-8') as json_data:
        
        cur_json_anno = json.load(json_data)
        
        polygons = [r['points'] for r in cur_json_anno['shapes']]
        #polygon or rectangle
        types = [r['shape_type'] for r in cur_json_anno['shapes']]
        labels= [r['label'] for r in cur_json_anno['shapes'] ]
        print(labels)
        image=skimage.io.imread(pic_path)
        
        #original image and json
        box_json_file = open(output_dir+base_name+".txt",'w')#new json file
        
        
        #only write the original bouinding box label
        for i in range(len(polygons)):
            min_x=5000
            min_y=5000
            max_y=0
            max_x=0    
            for (x,y) in polygons[i]:                        
                if (x<min_x):   min_x=x
                if (y<min_y):   min_y=y
                if (x>max_x):   max_x=x
                if (y>max_y):   max_y=y
            x,y,w,h=convert(image.shape[0],image.shape[1],x1=min_x, 
                            y1=min_y,
                            x2=max_x,
                            y2=max_y)
            box_json_file.write(str(decide_class(labels[i]))+" "+str(x)+" "+str(y)+" "+str(w)+" "+str(h)+" "+'\n')
        
        box_json_file.close()
        skimage.io.imsave(output_dir+base_name+".jpg",image)

#target bounding box in the image
        
        #for image enhancement
        iabox=[]#get the orginal bbox
        for i in range(len(polygons)):
            min_x=5000
            min_y=5000
            max_y=0
            max_x=0    
            for (x,y) in polygons[i]:                        
                if (x<min_x):   min_x=x
                if (y<min_y):   min_y=y
                if (x>max_x):   max_x=x
                if (y>max_y):   max_y=y
            
            iabox.append(ia.BoundingBox(x1=min_x, 
            y1=min_y,
            x2=max_x,
            y2=max_y))
            
        bbs=ia.BoundingBoxesOnImage(iabox,shape=image.shape)
        seq = iaa.SomeOf(3,[
            iaa.Crop(px=(0, 100)), # crop images from each side by 0 to 16px (randomly chosen)
            iaa.Flipud(0.5),
            #iaa.AdditiveGaussianNoise(scale=0.1*255),
            #iaa.Sharpen(alpha=0.5),
	        iaa.Affine(scale={"x": (1.3, 1.8), "y": (1.3, 1.8)},translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},rotate=(-45,45)),
            iaa.Fliplr(0.5), # horizontally flip 50% of the images
            #iaa.GaussianBlur(sigma=(0, 3.0))
            ],
            random_order=True
        ) # blur images with a sigma of 0 to 3.0
        #get more enhance image
        
        
        repeate=18
        for i in range(repeate):
            seq_det = seq.to_deterministic()
            image_aug = seq_det.augment_images([image])[0]
            bbs_aug = seq_det.augment_bounding_boxes([bbs])[0]
            box_json_file = open(output_dir+base_name+str(count)+".txt",'w')#new json file
            for i in range(len(bbs_aug.remove_out_of_image().clip_out_of_image().bounding_boxes)):
                print(len(bbs.bounding_boxes))
                after = bbs_aug.remove_out_of_image().clip_out_of_image().bounding_boxes[i]
                x,y,w,h = convert(image.shape[0],
                image.shape[1],
                after.x1,
                after.x2,
                after.y1,
                after.y2)
                #print("point1",image.shape[0],"  ",image.shape[1],"  ",after.x1,"  ",after.x2,"  ",after.y1,"  ",after.y2)
                #print("point2",x,"  ",y,"  ",w,"  ",h)
                #drwa_rectangle(image_aug,x,y,w,h)
                #skimage.io.imshow(image_test)
                #skimage.io.show()
                box_json_file.write(str(decide_class(labels[i]))+" "+str(x)+" "+str(y)+" "+str(w)+" "+str(h)+" "+'\n')
            box_json_file.close()
            skimage.io.imsave(output_dir+base_name+str(count)+".jpg",image_aug)
            count=count+1

        #image_before = bbs.draw_on_image(image, thickness=2)
        #image_after = bbs_aug.draw_on_image(image_aug, thickness=2, color=[0, 0, 255])
        #skimage.io.imshow_collection([image_before,image_after])
        #skimage.io.show()