#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[22]:


df=pd.read_csv('C:/Users/user1/Desktop/Data_Visualization/Mall_Customers.csv')


# In[6]:


pip install --upgrade pip


# In[23]:


df


# In[24]:


plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'])
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()


# In[20]:


fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111, projection='3d')

# plot the data points
ax.scatter(df['Age'],df['Annual Income (k$)'], df['Spending Score (1-100)'],s=50,alpha=0.6)

# set labels for each axis
ax.set_xlabel('Age')
ax.set_ylabel('Annual Income (k$)')
ax.set_zlabel('Spending Score (1-100)')

# set view angle and rotation
ax.view_init(elev=30, azim=45)

plt.show()


# In[11]:


plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'])
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()


# In[ ]:




