import os

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#####################################################################
def SURF(img):
    surf = cv2.xfeatures2d.SURF_create()
    keypoints_surf, descriptors = surf.detectAndCompute(img, None)
    #keypoints_surf, descriptors = surf.detectAndCompute(img, None)
    print("Features : ",len(keypoints_surf))
    imgKP = cv2.drawKeypoints(img, keypoints_surf, None)
    return imgKP

#####################################################################
def SIFT(img,Filter=False):
    if Filter: img = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
    sift = cv2.SIFT_create()
    keypoints_sift, descriptors = sift.detectAndCompute(img, None)
    print("Features : ",len(keypoints_sift))
    imgKP = cv2.drawKeypoints(img, keypoints_sift, None)
    return imgKP,len(keypoints_orb)
#####################################################################
def ORB(img,Filter=False):
    if Filter : img = cv2.detailEnhance(img,  sigma_s=10, sigma_r=0.15)
    orb = cv2.ORB_create(nfeatures=1500)
    keypoints_orb, descriptors = orb.detectAndCompute(img, None)
    print("Features : ",len(keypoints_orb))
    imgKP = cv2.drawKeypoints(img, keypoints_orb, None)
    return imgKP,len(keypoints_orb)
##def moveBasedOnregion(src,dst):
  ##  for file in os.listdir(src):
    ##    if file.split(".")[-2] == "png3":
      ##      src_path=os.path.join(src,file)
        ##    dst_path = os.path.join(dst,file)
          ##  os.replace(src_path,dst_path)

path_imgYes="G10_filterd_images/splitted"
dst_path = "G10_filterd_images/splitted/region4"


normal=None
abnormal=None
blocksH=2
blocksW=2
rows=[]
for file in os.listdir(dst_path):
    img = cv2.imread(os.path.join(dst_path,file))
    res,features = ORB(img)
    rows.append([file,features])

df = pd.DataFrame(rows,columns=['name','features'])
df.to_csv("data/region4.csv",index=False)