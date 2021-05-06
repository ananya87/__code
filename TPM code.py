#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd 
import numpy as np


# In[74]:


df=pd.read_csv("~/Desktop/new1.csv")


# In[75]:


print(df.head())


# In[98]:


a=df['Temp']
type(a)
a1=a.to_frame()
a1


# In[99]:


b=df['Temp']
b


# In[100]:


b=a.shift(-36)
type(b)
b1=b.to_frame()
b1


# In[101]:


t=df['bins']=pd.cut(x=a,bins=[0,3.6,7.2,10.8,14.4,18,21.6,25.2,28.8,32.4,36,39.6,43.2,46.8,50.4,54,57.6,61.2,64.8,68.4,72,75.6,79.2,82.8,86.4,90,93.6,97.2,100.8,104.4,108])
t=df['bins'].apply(lambda x:x.right)
type(t)
t1=t.to_frame()
t1


# In[102]:


T=df['bins']=pd.cut(x=b,bins=[0,3.6,7.2,10.8,14.4,18,21.6,25.2,28.8,32.4,36,39.6,43.2,46.8,50.4,54,57.6,61.2,64.8,68.4,72,75.6,79.2,82.8,86.4,90,93.6,97.2,100.8,104.4,108])
T=df['bins'].apply(lambda x:x.right)
type(T)
T1=T.to_frame()
T1


# In[106]:


horstack=pd.concat([a1,b1,t1,T1], axis=1)
horstack


# In[108]:


horstack.to_excel ("~/Desktop/python tpm.xlsx", index = False, header=True)


# In[109]:


z=np.array([0,3.6,7.2,10.8,14.4,18,21.6,25.2,28.8,32.4,36,39.6,43.2,46.8,50.4,54,57.6,61.2,64.8,68.4,72,75.6,79.2,82.8,86.4,90,93.6,97.2,100.8,104.4,108])
z


# In[111]:


f=pd.crosstab(t, T,dropna=True).reindex(columns=z, index=z, fill_value=0)
f


# In[33]:


df1=pd.DataFrame(f)
df1


# In[35]:


df1.to_excel ("~/Desktop/python tpm.xlsx", index = False, header=True)


# In[ ]:




