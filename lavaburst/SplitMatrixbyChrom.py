#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sys
import os
# In[2]:


absFile=sys.argv[2]
mergedData=sys.argv[1]

# In[3]:

dir_path = os.path.dirname(os.path.realpath(mergedData))

absDf = pd.read_csv(absFile, sep="\t", names=["chr", "start", "end", "binno"], usecols=["chr", "binno"])


# In[4]:


mergedDf = pd.read_csv(mergedData, sep="\t", names=["bin1", "bin2", "count"])


# In[5]:


maxVals = absDf.groupby("chr").max()
minVals = absDf.groupby("chr").min()
maxVals = maxVals.T.to_dict()
minVals = minVals.T.to_dict()


# In[6]:


for i in maxVals:
    chrDf = mergedDf[(mergedDf["bin1"] >= minVals[i]["binno"]) & (mergedDf["bin1"] <= maxVals[i]["binno"]) & (mergedDf["bin2"] >= minVals[i]["binno"]) & (mergedDf["bin2"] <= maxVals[i]["binno"])]
    chrDf.to_csv(os.path.join(dir_path,i + '.matrix'), sep="\t", header=False, index=False)

# In[8]:





# In[ ]:




