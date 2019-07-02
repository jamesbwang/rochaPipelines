#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sys
path = sys.argv[1]
sizes = sys.argv[2]
binSize= int(sys.argv[3])


# In[2]:


insulations = pd.read_csv(path, sep="\t", names=["chr", "RI", "start", "end", "insulation"])
sizes = pd.read_csv(sizes, sep="\t", names=["chr", "size"])


# In[3]:


insulations = insulations[insulations["RI"] >=.700]


# In[4]:


insulations["start"] = insulations["start"].multiply(binSize)
insulations["end"] = insulations["end"].multiply(binSize)


# In[ ]:





# In[5]:


chrom = insulations.iloc[0,0]
size = int(sizes[sizes["chr"] == chrom]["size"].astype(int))


# In[6]:


insulations["end"] = insulations["end"].apply(lambda x: size if size < x else x)


# In[7]:


insulations.sort_values(by=["chr", "start", "end"]).drop_duplicates(subset=["chr", "start", "end"],keep="first").to_csv(path + ".bed", sep="\t", header=False, index=False, columns=["chr", "start", "end"])






