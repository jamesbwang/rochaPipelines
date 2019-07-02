#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sys
from pathlib import Path
import numpy as np
binMap = sys.argv[1]
matrix = sys.argv[2]
chroms = ["chr" + str(int(s)) for s in Path(matrix).name.split(".") if s.isdigit()]


# In[2]:


binMapDf = pd.read_csv(binMap, sep="\t", names=["chr", "start", "end", "binNo"], usecols=["chr", "start", "binNo"], index_col=False)
matrixDf = pd.read_csv(matrix, sep="\t", names=["start1", "start2", "score"], index_col=False)


# In[3]:


binMapDf["key"] = binMapDf["chr"] + "_" + binMapDf["start"].astype(str)
bins = binMapDf.set_index(["key"]).to_dict()["binNo"]


# In[4]:


matrixDf["bin1"] = matrixDf["start1"].apply(lambda x: bins.get(chroms[0]+ "_" + str(x)))
matrixDf["bin2"] = matrixDf["start2"].apply(lambda x: bins.get(chroms[1] + "_" + str(x)))


# In[10]:




matrixDf[(matrixDf != 0).all(1)].dropna().sort_values(by=["bin1", "bin2"]).groupby(['bin1','bin2'], as_index=False)['score'].sum().to_csv(matrix + ".sorted.matrix", sep="\t", columns=["bin1", "bin2", "score"], header=False, index=False)

                                                
                                                
                                                
                                                


# In[ ]:




