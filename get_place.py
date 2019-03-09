import os
from PIL import Image
import cv2
import numpy as np
import final_match as recognizer
import list_images as li
import training
def place_in(path):
    img=li.img_asarray(path)
    imgm=training.mean_img(img)
    imgv=training.var_img(img)
    list_req=training.training_algo(imgm,imgv)
    print(list_req)
    iar,iar_name=li.list_images(list_req)
    best=-1
    name=[]
    print(iar_name)
    for i in range(len(iar)):
        ssim=recognizer.match(img,iar[i])
        print("ssim...",ssim,"...name...",name)
        if(ssim>best):
            best=ssim
            name=iar_name[i]
    print("best....",best)
    
    if(recognizer.similar(best)):
        return training.get_lable(name)
    else:
        return False



#print(place_in(r"C:\Users\01rag\Desktop\ \ULTIMATE MINOR 2\test\a2z.jpg"))
