#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


ds = pd.read_csv("bottle.csv",low_memory=False)
ds.head()


# In[3]:


ds_s = ds[['Salnty','T_degC']]
ds_s.isnull().sum()


# In[4]:


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "most_frequent")
imputer.fit(ds_s)
ds_n = imputer.transform(ds_s)
ds_n


# In[5]:


x = ds_n[:,0].reshape(-1,1)
y = ds_n[:,1]


# In[6]:


from sklearn.model_selection import train_test_split


# In[7]:


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)


# In[9]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)


# In[10]:


y_pred = model.predict(X_test)
y_pred


# In[11]:


model.predict([[33.437]])


# In[12]:


import joblib


# In[13]:


joblib.dump(model,"california_water_temp_from_salinity.pkl")


# In[ ]:




