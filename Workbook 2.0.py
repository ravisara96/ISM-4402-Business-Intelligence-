#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.chdir('/Users/sachiwairugalbandara/Desktop')


# In[2]:


import pandas as pd
import glob
all_data = pd.DataFrame()
for f in glob.glob("/Users/sachiwairugalbandara/Desktop/Python Files/datasets/data*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True) 
all_data.describe()


# In[ ]:




