#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
Location = "/Users/sachiwairugalbandara/Desktop/Python Files/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[ ]:





# In[12]:


df = df.sort_values(by=['lname', 'age', 'grade'],ascending=[True, True, True])
df.head()


# In[ ]:




