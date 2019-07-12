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
s = int(chromsizes["chr" + str(chrom)])
s = int(s/5000)


# In[4]:


matr = np.zeros((s+1,s+1))


# In[5]:


df = pd.read_csv(matr_tsv, sep="\t", names=["start", "end", "score"], index_col=False)


# In[6]:


for i in df.itertuples():
    matr[int(i[1]/binSize), int(i[2]/binSize)] = i[3]
    matr[int(i[2]/binSize), int(i[1]/binSize)] = i[3]


# In[7]:


index = pd.read_csv(absbed, sep="\t", names=["chrom", "start", "end", "binno"], index_col=False, usecols=["chrom", "start", "binno"])


# In[8]:


index = index[index["chrom"] == "chr" + str(chrom)]
index["head"] = "bin" + index["binno"].astype(str) + "|" + sizes.split(".")[0] + "|" + "chr" + str(chrom) + ":" + index["start"].astype(str) + "-" + (index["start"].astype(int)+binSize).astype(str)

# In[9]:


df = pd.DataFrame(data=matr, index=index["head"], columns=index["head"])


# In[ ]:


df.to_csv(matr_tsv + ".my5c", sep="\t")

