#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import os


# ### run this cell as administrator

# In[ ]:


# powershell -c "mkdir $env:TEMP\AppLog ; Get-AppXPackage -AllUsers | Out-File $env:TEMP\AppLog\AllAppxPackage.csv"


# In[14]:


temp_dir = os.getenv('TEMP')
filepath = temp_dir+"\\AppLog\\AllAppxPackage.csv"


# ### Input data

# In[2]:


with open(filepath, 'r', encoding='utf-16') as file:
    data = file.read()
    # Split the data into lines
    lines = data.strip().split('\n')
    
    # Create a list to store the cleaned-up data
    cleaned_data = []
    data_dict = {}
    
    # Process each line
    for line in lines:
        # Remove leading/trailing whitespace
        line = line.strip()
    
        # Check if the line contains a colon (:)
        if ':' in line:
            key, value = line.split(':', 1)
          
            # Strip leading/trailing whitespace from both key and value
            key = key.strip()
            value = value.strip()
            
            # Add the cleaned-up data to the list
            
            data_dict[key] = value
            # check if the header is Status the last one 
            if (key == "Status"):
                cleaned_data.append(data_dict)
                data_dict = {}
            
    


# ### Create a DataFrame from the cleaned data

# In[3]:


df = pd.DataFrame(cleaned_data)
df.head()


# In[4]:


df.to_csv("./output.csv")


# In[ ]:





# In[ ]:





# In[ ]:




