#!/usr/bin/env python
# coding: utf-8

# In[9]:


def makeMatrix():
    matrix = []
    file = open("avocado.csv", "r")
    count = 0
    for line in file:
        if count == 0:
            print(line)
        else:
            line = line.strip()
            row = line.split(",")
            matrix.append(row)
        count += 1
    print("Read ", count, "lines.\n")
    file.close()
    return matrix


# In[10]:


mat = makeMatrix()
for row in mat:
    print(row,"\n")
    


# In[12]:


import pandas as pd
data = pd.read_csv("avocado.csv")
data.head()
#data.tail()


# In[13]:


data["Date"][1]


# In[17]:


data["AveragePrice"]


# In[14]:


data["Total Volume"]


# In[16]:


data["AveragePrice"][15]


# In[25]:


data.describe()


# In[ ]:





# In[ ]:





# In[18]:


import matplotlib.pyplot as plt 
import numpy as np 
np.random.seed(10) 
col1 = data["Small Bags"]
col2 = data["Large Bags"]
col3 = data["XLarge Bags"]
myData = [col1, col2, col3]
fig = plt.figure(figsize =(10, 7))
ax = fig.add_axes([0, 0, 1, 1])
bp = ax.boxplot(myData)
plt.show()


# In[20]:


plt.hist(myData)
plt.show()


# In[21]:


import pandas as pd 
df = pd.read_csv("avocado.csv") 
df[:20] 


# In[22]:


df.corr(method ='pearson') 


# In[24]:


import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set_theme()
uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(uniform_data)


# In[28]:


file = open("covid19_tweets.csv", "r")


# In[29]:


import pandas as pd
data = pd.read_csv("covid19_tweets.csv")
data.head()
#data.tail()


# In[31]:


import numpy as np
data.describe(include=np.object).transpose()


# In[37]:


data.describe()


# In[ ]:




