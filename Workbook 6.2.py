#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
Location = "/Users/sachiwairugalbandara/Desktop/Python Files/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[6]:


def score_to_numeric(x):
    if x=='female':
        return 1
    if x=='male':
        return 0


# In[7]:


df['gender_val'] = df['gender'].apply(score_to_numeric)
df.tail()


# In[8]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ exercise + hours + gender_val', data=df).fit()
result.summary()


# In[ ]:




