#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from sqlalchemy import create_engine
db_file = r'/Users/sachiwairugalbandara/Desktop/Python Files/datasets/salesdata.db' 
engine = create_engine(r"sqlite:///{}".format(db_file)) 
sql = 'SELECT * from test where sales in (89,98,115)' 
grade_data_df = pd.read_sql(sql, engine) 
grade_data_df
sales_data_df.head()


# In[ ]:




