#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("/Users/sachiwairugalbandara/Desktop/Python Files/datasets/weekly_call_data/data*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[ ]:





# In[ ]:




