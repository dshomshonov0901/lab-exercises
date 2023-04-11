#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import csv
import seaborn as sns
df = pd.read_csv("Airbnb.csv")
df
#uses for this dataset: airbnb can use this data to keep track of the rooms in nyc being listed and to anaylze trends about their hosts. They can determine which room types are most popular in which neighbourhoods, the average price of rooms in nyc and how that correlates with the amount of reviews the host recieves. 


# In[30]:


df.describe()


# In[31]:


df.head()


# In[32]:


df.dtypes


# In[33]:


cols = df.columns
sns.heatmap(df[cols].isnull())#seaborn map of all NaN values


# In[34]:


df_2=df.copy()
df_2.dropna()


# In[35]:


df["last_review"] = df["last_review"].fillna("No Review Specified")
cols=df.columns
sns.heatmap(df[cols].isnull())


# In[36]:


df["reviews_per_month"] = df["reviews_per_month"].fillna("0")
cols=df.columns
sns.heatmap(df[cols].isnull())#replaces NaN with no review specified for last review and replaces 0 for number of reviews columns


# In[38]:


df_3=df.copy()
df_3.drop(labels = ["host_id", "host_name", "neighbourhood_group", "longitude", "latitude", "price", "minimum_nights"], axis=1, inplace=True)
df_3


# In[18]:


df_3.last_review = df_3.last_review.str[0:4] 
df_3.last_review  ## isolates just the year from last_review


# In[39]:


#checks how many rooms are available on Airbnb in each neighbourhood

rooms = df_3["neighbourhood"]
room_dict = {}

for i in rooms:
  if i not in room_dict:
    room_dict[i] =1
  else:
    room_dict[i] += 1

print(room_dict)

