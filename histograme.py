import os
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
fig, axs = plt.subplots(ncols=4)
for i,path in enumerate(["region1","region2","region3","region4"]):
    df= pd.read_csv("data/"+path+".csv")
    sns.histplot(data=df['features'], kde=True, ax=axs[i])
    #sns.displot(df['Region1'], kind="kde", fill=True)
plt.grid(True)
plt.show()