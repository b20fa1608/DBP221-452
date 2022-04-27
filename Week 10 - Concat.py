#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[15]:


class display(object):
    """Олон үр дүнг нэг дор харах боломжтой болгож байгаа хэсэг"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
        self.args = args
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)
    
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)


# In[14]:


def make_df(cols, ind):
    """Датафрэйм үүсгэж буй функц"""
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)

make_df('ABC', range(3))


# In[9]:


x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
np.concatenate([x, y, z])


# In[10]:


x = [[1, 2],
     [3, 4]]
np.concatenate([x, x], axis=1)


# In[12]:


ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
pd.concat([ser1, ser2])


# In[24]:


df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
display('df1', 'df2', 'pd.concat([df1, df2])')


# In[23]:


df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
display('df3', 'df4', "pd.concat([df3, df4], axis=1)")


# In[25]:


x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])
y.index = x.index
display('x', 'y', 'pd.concat([x, y])')


# In[26]:


display('x', 'y', "pd.concat([x, y], keys=['x', 'y'])")


# In[27]:


df5 = make_df('ABC', [1, 2])
df6 = make_df('BCD', [3, 4])
display('df5', 'df6', 'pd.concat([df5, df6])')


# In[28]:


display('df5', 'df6',
        "pd.concat([df5, df6], join='inner')")


# In[29]:


display('df1', 'df2', 'df1.append(df2)')


# In[ ]:




