#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
columns=['Names', 'Grades'])
df


# In[52]:


df.loc[df['Grades'] <= 0]


# In[53]:


df.loc[(df['Grades'] >= -2,'Grades')] = 0
df.head()


# In[ ]:





# In[ ]:




