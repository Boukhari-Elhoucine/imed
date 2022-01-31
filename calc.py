from scipy import stats
import pandas as pd
import numpy as np

df = pd.read_csv("data/region1.csv")
arr = np.array(df['features'])
mean,sigma = np.mean(arr),np.std(arr)
conf_int = stats.norm.interval(0.68,loc=mean,scale=sigma/np.sqrt(len(arr)))
print(conf_int,"interval de confiance")
print(sigma ,"l'ecart type")