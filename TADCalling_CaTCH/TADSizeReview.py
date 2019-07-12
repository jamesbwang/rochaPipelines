#!/usr/bin/env python
# coding: utf-8

# In[28]:


import matplotlib.pyplot as plt

import pandas as pd
import sys
import os

# In[40]:


bedpe = sys.argv[1]
finalPath = sys.argv[2]


# In[41]:


df = pd.read_csv(bedpe, names=["chr1", "start1", "end1", "chr2", "start2", "end2"], index_col=False, sep="\t", usecols=["chr1", "start1", "end1"])


# In[42]:


df["sizes"] = df["end1"] - df["start1"]


# In[43]:


fig = plt.figure()
plt.hist(df["sizes"], bins=200)
plt.xlabel("region size")
plt.ylabel("# TADS")


# In[39]:


fig.savefig(os.path.join(finalPath, bedpe.split("/")[-1] + "_sizes.png"))
