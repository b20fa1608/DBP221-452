#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import os
# os.chdir(r"C:\Users\DELL\Downloads\APF221-main.zip\APF221-main")

import pandas as pnd

# Working with excel
xl = pnd.read_excel('temp.xlsx')
xl
#xl = pnd.read_excel('temp.xlsx', sheet_name='TRY')
#xl = pnd.read_excel('temp.xlsx', sheet_name = 2)
#xl = pnd.read_excel('temp.xlsx', sheet_name= 0, index_col = 3)
#xl = pnd.read_excel('temp.xlsx', sheet_name=3, index_col=0, header=2)
#xl = pnd.read_excel('temp.xlsx', sheet_name=0, usecols = "B,C:E")
#xl = pnd.read_excel('temp.xlsx', sheet_name=0, skiprows= 3, index_col=0)
#xl = pnd.read_excel('temp.xlsx', sheet_name=0, header=[0,1,2])

#NAN
# xl.dropna(how='any', axis=1)
#xl.dropna(how='any', axis=0, inplace = False)
# # xl.dropna(axis=0, how = 'any')
#xl.fillna(0)
# # xl.fillna(method='bfill')
# # xl.fillna(method='ffill')
# # xl.fillna(method='ffill', axis=0)
# xl


# In[2]:


xl.fillna(0)


# In[3]:


xl.dropna(axis=0, how = 'any')
xl


# In[4]:


xl.dropna(how='all', axis=0)


# In[ ]:




