#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

import pandas as pd
import sys
import os

# In[2]:


catch = sys.argv[1]
finalPath = sys.argv[2]


# In[3]:


df = pd.read_csv(catch, sep="\t", names=["chr","ris", "sbin", "ebin", "is"], usecols=["ris"])


# In[10]:


fig = plt.figure()
plt.hist(df["ris"], bins=200)
plt.xlabel("reciprocal insulation score")
plt.ylabel("# TADS")


# In[ ]:


fig.savefig(os.path.join(finalPath, catch.split("/")[-1] + "_strengths.png"))

