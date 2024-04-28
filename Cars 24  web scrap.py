#!/usr/bin/env python
# coding: utf-8

# In[9]:


from selenium import webdriver


# In[10]:


driver=webdriver.Edge()


# In[11]:


driver.get("https://www.cars24.com/buy-used-car?sort=bestmatch&serveWarrantyCount=true&gaId=1784657388.1707119603&storeCityId=6356&pinId=682001")


# In[12]:


import time


# In[13]:


from bs4 import BeautifulSoup


# In[14]:


brand_name=[]
price=[]
kilometer=[]
fuel_type=[]
transmission=[]


# In[15]:


time.sleep(15)


# In[17]:


driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")


# In[18]:


soup= BeautifulSoup(driver.page_source)


# In[19]:


sec=soup.find('div',class_="_2d2CZ")


# In[20]:


for i in sec.find_all('div',class_="_2YB7p"):
    brand_name.append(i.find('h3',class_="_11dVb").text)
    price.append(i.find('strong',class_="_3RL-I").text)
    sec1=i.find('ul',class_="_3J2G-")
    kilometer.append(sec1.find('li').text)
    fuel_type.append(sec1.find_all('li')[2].text)
    transmission.append(sec1.find_all('li')[4].text)
    


# In[21]:


import pandas as pd


# In[22]:


df=pd.DataFrame()
df["Brand name"]=brand_name
df["selling price"]=price
df["kilometer"]=kilometer
df["Fuel Type"]=fuel_type
df["Transmission"]=transmission


# In[23]:


df


# In[163]:


df.to_csv('cars24kochi.csv', index=False)


# In[ ]:





# In[ ]:




