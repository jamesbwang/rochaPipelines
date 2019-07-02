#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sys
nodup_file = sys.argv[1]


# In[2]:


nodups = pd.read_csv(nodup_file, sep=" ", names="<str1> <chr1> <pos1> <frag1> <str2> <chr2> <pos2> <frag2> <mapq1> <cigar1> <sequence1> <mapq2> <cigar2> <sequence2> <readname1> <readname2>".split(), index_col=False)


# In[3]:


nodups= nodups.reindex(columns=["<readname1>", "<chr1>", "<pos1>", "<str1>", "<chr2>", "<pos2>", "<str2>"])


# In[ ]:





# In[4]:


nodups.to_csv(nodup_file[:-4] + ".validpairs")


# In[ ]:




