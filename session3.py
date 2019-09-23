#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 10


# In[3]:


y = 20


# In[4]:


x+y


# In[5]:


x*y


# In[6]:


x/y


# In[7]:


x-y


# In[8]:


10<<2


# In[9]:


10>>2


# In[12]:


x == 10 & y ==20


'''
docker run --rm -u root -p 8080:8080 -v jenkins-data:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -v "$HOME":/home jenkinsci/blueocean