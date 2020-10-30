#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "/Users/sachiwairugalbandara/Desktop/Python Files/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


df.hist()


# In[4]:


df.hist(column="age")


# In[5]:


df.hist(column="age", by="gender")


# In[ ]:




