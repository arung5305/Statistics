import numpy as np
import glob
import shutil
import os
from PIL import Image
import math
import scipy.misc
import cv2

src_dir = "C:\\Users\\bhuiy\\Desktop\\TEMP"
#dst_dir = "C:\\Users\\bhuiy\\Desktop\\Full AREDS data for Comp4\\Cropped\\2014\\"
imgArr = []
for jpgfile in glob.iglob(os.path.join(src_dir,"*.jpg")):
    img = Image.open(jpgfile)
    img = np.array(img[...,1])
    imgArr.append(img)
    



n=0
for jpgfile in glob.iglob(os.path.join(src_dir,"*.jpg")):
    #print(os.path.basename(jpgfile))
    n=n+1
    #img = cv2.imread(jpgfile)
    img = Image.open(jpgfile)
    img = np.array(img)
    img1 = cv2.Laplacian(img[...,1],cv2.CV_64F)
    img2 = cv2.Sobel(img[...,1],cv2.CV_64F,1,0,ksize=5)
    img3 = cv2.Canny(img,10,100)
    imgO = img
    img = []
    img.append(imgO[...,1])
    img.append(img2)
    img.append(img1)
    img = np.array(img)
    #img = img.reshape(350,350,3)
    img = img.transpose(1,2,0)
    print(img.shape)
    scipy.misc.imsave('outfile002.jpg', img)