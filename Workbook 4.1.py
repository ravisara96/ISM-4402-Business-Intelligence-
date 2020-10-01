#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
Location = "/Users/sachiwairugalbandara/Desktop/Python Files/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[43]:


bins = [0,50,80,100]
group_names = ['Non Qualified','Fail','Pass']


# In[44]:


df['Qualifying '] = pd.cut(df['grade'], bins, labels=group_names)
df


# In[ ]:





# In[ ]:




