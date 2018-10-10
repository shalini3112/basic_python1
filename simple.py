
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame({'distance':[2,4,6,8,10],'time':[1,2,3,4,5]})
plt.plot(df)
plt.ylabel('distance(km)')
plt.title("Simple plot with multilple lines on same graph")

