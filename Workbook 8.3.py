#!/usr/bin/env python
# coding: utf-8

# In[54]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "/Users/sachiwairugalbandara/Desktop/Python Files/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.plot.scatter(x = 'hours', y = 'grade' )
plt.xlabel('Hours')
plt.ylabel('Grade')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




