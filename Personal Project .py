#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
data=pd.read_csv("/Users/sachiwairugalbandara/Desktop/Python Files/datasets/axisdata.csv")
data.head()


# In[2]:


#1
car_sold=data["Cars Sold"]
avg_car_sold=np.mean(car_sold)
print("Average cars sold per month are",avg_car_sold)


# In[3]:


#2
max_car=max(car_sold)
print("Maximum cars sold per month are",max_car)


# In[4]:


#3
min_car=min(car_sold)
print("Minimum cars sold per month are",min_car)


# In[5]:


#4
male_car_sold=data[data["Gender"]=="M"]["Cars Sold"]
avg=np.mean(male_car_sold)
print("Average cars sold by gender = male is",avg)
female_car_sold=data[data["Gender"]=="F"]["Cars Sold"]
avg1=np.mean(female_car_sold)
print("Average cars sold by gender = female is",avg1)


# In[6]:


#5
hours_worked=data[data["Cars Sold"]>3]["Hours Worked"]
avg_hours_worked=np.mean(hours_worked)
print("Average hours worked by people selling more than 3 cars per month",avg_hours_worked)


# In[7]:


#6
exp=data["Years Experience"]
avg_exp=np.mean(exp)
print("Average years of experience is",avg_exp)


# In[8]:


#7
exp=data[data["Cars Sold"]>3]["Years Experience"]
avg_exp=np.mean(exp)
print("Average hours worked by people selling more than 3 cars per month",avg_exp)


# In[9]:


#8
cars=data[data["SalesTraining"]=="N"]["Cars Sold"]
avg_cars=np.mean(cars)
print("Average cars sold per month when they do not have training",avg_cars)
cars1=data[data["SalesTraining"]=="Y"]["Cars Sold"]
avg_cars_yes=np.mean(cars1)
print("Average cars sold per month when they have training",avg_cars_yes)


# In[10]:


# when someone has training of sale then there is good number of sales of cars. hence, training of a 
#perso is a good indicator of car sales.


# In[11]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5),dpi=100)
x=data["Gender"]
y=data["Cars Sold"]
plt.bar(x,y,color="red")
plt.xlabel("Gender")
plt.ylabel("Cars sold")
plt.title("Bar plot")
plt.show()


# In[12]:


plt.figure(figsize=(5,5),dpi=100)
x=data["SalesTraining"]
y=data["Cars Sold"]
plt.bar(x,y,color="green")
plt.xlabel("Sales Training")
plt.ylabel("Cars sold")
plt.title("Bar plot")
plt.show()


# In[13]:


plt.figure(figsize=(5,5),dpi=100)
y=data["Cars Sold"]
plt.hist(y,color="yellow")
plt.ylabel("Cars sold")
plt.title("Histogram")
plt.show()


# In[14]:


plt.figure(figsize=(5,5),dpi=100)
x=data["Hours Worked"]
y=data["Cars Sold"]
plt.scatter(y,x,color="purple")
plt.xlabel("cars sold")
plt.ylabel("Hours worked")
plt.title("scatter plot")
plt.show()


# In[ ]:




