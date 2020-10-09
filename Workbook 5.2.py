#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data=GradeList,columns=['Names','Grades'])
df


# In[2]:


(/, This, describes, how, many, values, in, the, gradelist)
df['Grades'].count() 


# In[3]:


(/, This, is, the, average, of, the, grades)
df['Grades'].mean() 


# In[5]:


(/, This, is, the, standard, variation, of, the, grades)
df['Grades'].std() 


# In[6]:


(/, This, is, the, minimum, value, of, the, gradeslist)
df['Grades'].min() 


# In[7]:


(/, This, is, the, maximum, value, of, the, gradelist)
df['Grades'].max() 


# In[8]:


(/, This, is, the, first, quantile, set)
df['Grades'].quantile(.25) 


# In[9]:


(/, This, is, the, second, quantile, set)
df['Grades'].quantile(.5) 


# In[10]:


(/, This, is, the, third, quantile, set)
df['Grades'].quantile(.75) 


# In[15]:


(/, This, exlains, the, median, of, the, gradelist)
df['Grades'].median()


# In[16]:


(/, This, explains, the, mode, of, the, grdelist)
df['Grades'].mode()


# In[17]:


(/, This, explains, the, values, in, the, columns)
df['Grades'].var()


# In[22]:


df.var()


# In[ ]:





# In[23]:


# This is bsdegrees data summary computing stastics
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
bsdegrees = [1,1,0,0,1]
DegreeList = zip(names,bsdegrees)
df = pd.DataFrame(data=DegreeList,columns=['Names','bsdegrees'])
df


# In[24]:


df['bsdegrees'].count()


# In[25]:


df['bsdegrees'].mean()


# In[26]:


df['bsdegrees'].std()


# In[27]:


df['bsdegrees'].min()


# In[28]:


df['bsdegrees'].max()


# In[29]:


df['bsdegrees'].quantile (.25)


# In[30]:


df['bsdegrees'].quantile(.5)


# In[31]:


df['bsdegrees'].quantile(.75)


# In[32]:


df['bsdegrees'].median()


# In[33]:


df['bsdegrees'].mode()


# In[34]:


df['bsdegrees'].var()


# In[35]:


df.var()


# In[36]:


# This is msdegrees data summary computing stastics
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
msdegrees = [2,1,0,0,0]
DegreeList = zip(names,msdegrees)
df = pd.DataFrame(data=DegreeList,columns=['Names','msdegrees'])
df


# In[37]:


df['msdegrees'].count()


# In[38]:


df['msdegrees'].mean()


# In[39]:


df['msdegrees'].std()


# In[40]:


df['msdegrees'].min()


# In[41]:


df['msdegrees'].max()


# In[42]:


df['msdegrees'].quantile(.25)


# In[43]:


df['msdegrees'].quantile(.5)


# In[44]:


df['msdegrees'].quantile(.75)


# In[46]:


df['msdegrees'].median()


# In[47]:


df['msdegrees'].mode()


# In[48]:


df['msdegrees'].var()


# In[49]:


df.var()


# In[50]:


# This is phddegrees data summary computing stastics
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
phddegrees = [0,1,0,0,0]
DegreeList = zip(names,phddegrees)
df = pd.DataFrame(data=DegreeList,columns=['Names','phddegrees'])
df


# In[51]:


df['phddegrees'].count()


# In[52]:


df['phddegrees'].mean()


# In[53]:


df['phddegrees'].std()


# In[54]:


df['phddegrees'].min()


# In[55]:


df['phddegrees'].max()


# In[56]:


df['phddegrees'].quantile(.25)


# In[57]:


df['phddegrees'].quantile(.5)


# In[58]:


df['phddegrees'].quantile(.75)


# In[59]:


df['phddegrees'].median()


# In[61]:


df['phddegrees'].mode()


# In[62]:


df['phddegrees'].var()


# In[63]:


df.var()


# In[ ]:




