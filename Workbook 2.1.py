#!/usr/bin/env python
# coding: utf-8

# In[14]:


import os
os.chdir('/Users/sachiwairugalbandara/Desktop')


# In[32]:


import pandas as pd
from sqlalchemy import create_engine
db_file = r'datasets/gradedata.db'
engine = create_engine(r"sqlite:///{}".format(db_file))
sql = 'SELECT * from test where sales in (2625,2700,3100)'
grade_data_df = pd.read_sql(sql, engine)
grade_data_df


# In[ ]:





# In[13]:





# In[ ]:




