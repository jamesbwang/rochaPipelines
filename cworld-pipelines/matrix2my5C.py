#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import sys
import csv
import os

# In[2]:


matr_tsv=sys.argv[1]
sizes=sys.argv[2]
absbed =sys.argv[3]
binSize=int(sys.argv[4])


# In[3]:



with open(sizes, 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    chromsizes = {r[0]: r[1] for r in reader} 
chrom = os.path.basename(matr_tsv).split(".")[0]
print(chrom)
# In[4]:

index = pd.read_csv(absbed, sep="\t", names=["chrom", "start", "end", "binno"], index_col=False, usecols=["chrom", "start", "binno"])
index = index[index["chrom"] == str(chrom)]
binStart = index.iloc[0, 2]
index["\t"] = "bin" + index["binno"].astype(str) + "|" + sizes.split(".")[0] + "|"  + str(chrom) + ":" + (index["start"]+1).astype(str) + "-" + (index["start"].astype(int)+binSize).astype(str)
matr = np.zeros((index.shape[0],index.shape[0]))


# In[5]:


df = pd.read_csv(matr_tsv, sep="\t", names=["start", "end", "score"], index_col=False)


# In[6]:


for i in df.itertuples():
    matr[int(i[1]-binStart), int(i[2]-binStart)] = i[3]
    matr[int(i[2]-binStart), int(i[1])-binStart] = i[3]


df = pd.DataFrame(data=matr, index=index["\t"], columns=index["\t"])
df = df.fillna(0)
del df.index.name

# In[ ]:


df.to_csv(matr_tsv + ".my5c", sep="\t")

