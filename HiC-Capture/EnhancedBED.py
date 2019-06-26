#!/usr/bin/env python
# coding: utf-8

# In[1]:


interPickle = "data/pickled_targetedInteractions.pkl"
oligoPickle = "data/oligo_sequences"
path = "data/territory.bed"


# In[2]:


import pandas as pd
interactions = pd.read_pickle(interPickle)
bounds = pd.read_pickle(oligoPickle)


# In[3]:


i = 0
territoryInteractions = {}
for territory in bounds.itertuples():
    territoryInteractions[i] = interactions.query("(X1 == 'chr8' & X2 <= @territory[2] & (X2 + 51) >= @territory[1]) | (X5 == 'chr8' & X6 <= @territory[2] & (X6 + 51) >= @territory[1])")
    i += 1


# In[4]:


import numpy as np
for i in territoryInteractions:
    territory = bounds.iloc[i]
    df1 = territoryInteractions[i].iloc[:,:2]
    df2 = territoryInteractions[i].iloc[:,2:]
    df1 = df1.loc[(df1["X1"] != "chr8") | (df1["X2"] > territory[1]) | (df1["X2"]+51 < territory[0])]
    df2 = df2.loc[(df2["X5"] != "chr8") | (df2["X6"] > territory[1]) | (df2["X6"]+51 < territory[0])]
    df2.columns = ['X1', 'X2']
    territoryInteractions[i] = pd.concat([df1, df2], sort=False)
    territoryInteractions[i]["end"] = territoryInteractions[i]["X2"] + 51


# In[5]:


for i in territoryInteractions:
    territoryInteractions[i].to_csv(path_or_buf=path[:-4] + "_" + str(i) + "_" + path[-4:], sep='\t', na_rep='', float_format="%.f", columns=None, header=False, index=False, index_label=None, mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, tupleize_cols=None, date_format=None, doublequote=True, escapechar=None, decimal='.')


# In[ ]:




