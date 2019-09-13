#!/usr/bin/env python
# coding: utf-8

# In[1]:


city = ["London","Amsterdam", "Helsinki"]


# In[2]:


city


# In[3]:


city[1]


# In[4]:


city[0]


# In[5]:


city[-1]


# In[6]:


city.append('Boston')


# In[7]:


city


# In[8]:


city.append('London')


# In[9]:


city


# In[10]:


city.insert(2,'Venice')


# In[11]:


city


# In[12]:


city.pop()


# In[13]:


city


# In[14]:


city.pop(1)


# In[15]:


cars = ('Audi','BMW','Merc')


# In[23]:


cars = ('Audi','BMW','Merc','Audi')


# In[24]:


cars


# In[16]:


cars


# In[19]:


cars[1]


# In[21]:


cars[1]="KIA"


# In[20]:


cars.append('BMW')


# In[17]:


city[1]="Sydeny"


# In[18]:


city


# In[26]:


languages = {"JavaScript","Python","Node","JavaScript"}


# In[ ]:





# In[27]:


languages


# In[28]:


languages.add('Ruby')


# In[29]:


languages


# In[30]:


languages.add('Ruby')


# In[31]:


languages


# In[32]:


languages.discard('Node')


# In[33]:


languages


# In[34]:


seta = {1,2,3}


# In[35]:


setb = {"x","y","z"}


# In[36]:


setc = seta.union(setb)


# In[ ]:





# In[37]:


setc


# In[38]:


setb = {"x","y","z",3,4}


# In[39]:


setc = seta.union(setb)


# In[40]:


setc


# In[41]:


country = {
    "city":"London",
    "language":"English",
    "country":"England"
}


# In[42]:


country


# In[43]:


country['city']


# In[44]:


country['pop']= 388387


# In[45]:


country


# In[46]:


country['pop']=9879797897


# In[47]:


country

