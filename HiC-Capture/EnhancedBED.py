#!/usr/bin/env python
# coding: utf-8

# In[2]:

import sys
import pandas as pd

interPickle = sys.argv[1]
oligoPickle = sys.argv[2]
path = sys.argv[3]
reader_output = sys.argv[4]

with open(reader_output, "r") as f:
    fullTotal = int(f.read()[34:])
    
# read pickles to save computation time
interactions = pd.read_pickle(interPickle)
bounds = pd.read_pickle(oligoPickle)

# In[4]:


## separate interactor/interactee pairs and filter out territory regions. 
## subsequent concatenation and generation of ends from "start" of oligos yields easy conversion to .bed files
territoryInteractions = []
total = 0
for i in range(bounds.shape[0]):
    territory = bounds.iloc[i]
    t1 = territory[0]
    t2 = territory[1]
    i = territory.index
    df = interactions[((interactions["X1"] == 'chr8') & (interactions["X2"] <= t2) & (t1 <= (interactions["X2"] + 51))) | ((interactions["X5"] == 'chr8') & (interactions["X6"] <= t2) & (t1<=(interactions["X6"] + 51)))]
    #separation
    df1 = df.iloc[:,:2]
    df2 = df.iloc[:,2:]
    #filtering
    df2.columns = ['X1', 'X2']
    df1 = df1[(df1["X1"] != "chr8") | (df1["X2"] > t2) | (df1["X2"]+51 < t1)]
    df2 = df2[(df2["X1"] != "chr8") | (df2["X2"] > t2) | (df2["X2"]+51 < t1)]
    #concatenation
    df = pd.concat([df1, df2], sort=False)
    total += df.shape[0]
    #end generation
    df["X2"] = (df["X2"]/5).round(decimals=-3)*5
    df["end"] = df["X2"] + 5000
    territoryInteractions.append(df)
with open(reader_output, "a") as f:
    f.write("Enriched Target Interactions: " + str(total))
    f.write("Enrichment Fraction: " + str(total/fullTotal))

# In[5]:

#generation of bed files
for i in range(len(territoryInteractions)):
    territoryInteractions[i].to_csv(path_or_buf=path[:-4] + "_" + str(i) + "_" + path[-4:], sep='\t', na_rep='', float_format="%.f", columns=None, header=False, index=False, index_label=None, mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, tupleize_cols=None, date_format=None, doublequote=True, escapechar=None, decimal='.')
