#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import pandas as pd
path = sys.argv[1]
import csv

# In[2]:

print("reading merged matrices...")

df = pd.read_csv(path, sep="\t", names=["bin1","bin2","score"])
# In[4]:

print("aggregating matrices...")
df = df.groupby(['bin1', 'bin2']).sum()


# In[5]:

print("reformatting matrices...")
df = df.reset_index(drop=False)


# In[7]:

print("saving new matrix...")
df.to_csv(path + ".merged.txt", sep="\t", header=False, index=False)


# In[ ]:




