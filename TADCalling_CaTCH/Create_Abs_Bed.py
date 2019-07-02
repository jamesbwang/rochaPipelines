#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sys
path = sys.argv[1]
sizes = sys.argv[2]
binSize = int(sys.argv[3])


# In[2]:


df = pd.read_csv(sizes, sep="\t", names=["chr", "sizes"])


# In[ ]:





# In[3]:


df = df[df["chr"].str.match("chr\d{0,2}$")]


# In[4]:


df = df.assign(sortkey=df.chr.str[3:].astype(int)).sort_values(by=['sortkey']).drop("sortkey", axis=1)


# In[5]:


li = []
for i in df.itertuples():
    li.append(pd.DataFrame({"chr": [i[1] for j in range(int(i[2]/binSize))], "start": [j*binSize for j in range(0,int(i[2]/binSize))], "end": [j*binSize+binSize for j in range(0, int(i[2]/binSize))]}))
    li[-1] = li[-1].append(pd.DataFrame({"chr": [i[1]], "start": int(i[2]/binSize)*binSize, "end": i[2]}))


# In[ ]:





# In[6]:


returnDf = pd.concat(li)
returnDf["index"] = [i+1 for i in range(returnDf.shape[0])]


# In[7]:


returnDf.to_csv(path + ".abs.bed", sep="\t", header=False, index=False)


# In[ ]:




