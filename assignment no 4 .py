#!/usr/bin/env python
# coding: utf-8

# # Q1.How to import pandas and check the version?

# In[2]:


import pandas as pd


# In[3]:


print(pd.__version__)


# # Q2.How to create a series from a numpy array?

# In[17]:


import pandas as pd 
  
# import numpy as np 
import numpy as np 
  
# numpy array 
arr = arr = np.array( [1,'x',5,'y',4,'z','w',2,9] )
print(type(arr))
# forming series 
s = pd.Series(arr) 
print(type(s))
  
# output 
print(s)


# # Q3.How to convert the index of a series into a column of a dataframe?
# 

# In[53]:


import pandas as pd
scorecard_CSK = {
    "sam curran":38,
    "rutraj gaikwad":56,
    "faf du plesis":34,
    "ambati raydu":78,
    "m.s.dhoni":23,
}
print(scorecard_CSK)
scorecard=pd.Series(scorecard_CSK)
print(scorecard)
pd.DataFrame(scorecard,columns=['scorecard'])


# # Q4.Write the code to list all the datasets available in seaborn library.
# 

# In[70]:


import seaborn as sns
mpg = sns.load_dataset('mpg')
print(mpg)
print("\n\n\n\n\n\n DATASET IN LIST IS AS FOLLOW AS:-\n\n\n\n",mpg.values.tolist())


# # Q5.Which country origin cars are a part of this dataset?

# In[75]:


import seaborn as sns
# importing pandas with alias name
import pandas as pd

# loading the dataset from seaborn
mpg=sns.load_dataset('mpg')

# creating a dataframe
df = pd.DataFrame(mpg)

# Displaying the country origin from where cars belong
df.origin.unique().tolist()


# # Q6.Extract the part of the dataframe which contains cars belonging to 'usa'

# In[79]:


# importing seaborn
import seaborn as sns
# importing pandas with alias name
import pandas as pd

# loading the dataset from seaborn
mpg=sns.load_dataset('mpg')

# creating a dataframe
df = pd.DataFrame(mpg)

# Displaying the part from dataframe where cars belong to "usa"
df[df['origin'].str.contains("usa")]


# In[ ]:




