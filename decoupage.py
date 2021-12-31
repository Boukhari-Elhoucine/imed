import os
import cv2
import matplotlib.pyplot as plt

def splitImage(imagePath="images/fig1.jpg",blocksH=2,blocksW=2,w=256,h=256):
    im =  cv2.imread(imagePath)
    im = cv2.resize(im,(w,h))

    imgheight=im.shape[0]
    imgwidth=im.shape[1]

    M = imgheight//blocksH
    N = imgwidth//blocksW
    images=[]
    for y in range(0,imgheight,M):
        for x in range(0, imgwidth, N):
            images.append(im[y:y+M,x:x+N])

    return images

def splitAll(folder_path,blockH,blockW):
    for filename in os.listdir(folder_path):
        images = splitImage(os.path.join(folder_path,filename),blockH,blockW)
        print(images)
        for i in range(blockH*blockW):
            cv2.imwrite("G10_filterd_images/splitted/"+filename + str(i) + ".jpg",images[i])




folder_path = "G10_filterd_images"
#path_imgNo="covid19-mini-dataset/normal/person989_virus_1667.jpeg"#NORMAL2-IM-0315-0001.jpeg"
#path_imgYes="covid19-mini-dataset/covid/1-s2.0-S0140673620303706-fx1_lrg.jpg"

blocksH=2
blocksW=2
splitAll(folder_path,blocksH,blocksW)
