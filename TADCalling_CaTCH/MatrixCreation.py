#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import glob, os
import sys

curDirectory=sys.argv[1]
name=sys.argv[2]
binsize=int(sys.argv[3])


# In[ ]:


li = []
os.chdir(curDirectory)
for file in glob.glob("*.matrix"):
    li.append(pd.read_csv(file, sep="\t", names=["bin1", "bin2", "counts"]))
pd.concat(li).sort(["bin1", "bin2"], ascending=[True, True]).to_csv(name + ".matrix", sep="\t", header=False, index=False)

