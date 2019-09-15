#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(a,b):
    out = a+b
    return out
    


# In[2]:


add(1,2)


# In[4]:


add(2,3)


# In[12]:


def isEven(a):
    out = 'hi'
    if(a%2 == 0):
        out = 'Number is even'
    else:
        out = 'Number is odd'
    return out


# In[13]:


isEven(23)


# In[14]:


isEven(464356)


# In[15]:


abs(10)


# In[16]:


abs(-10)


# In[17]:


abs(10.11)


# In[20]:


myresult = [True, True, True, True]


# In[21]:


all(myresult)


# In[22]:


ascii('This is from Edureka')


# In[23]:


ascii('This is from EdurekÅ')


# In[24]:


bool(1)


# In[25]:


bool(0)


# In[26]:


a = 1


# In[27]:


b = 2


# In[32]:


out = b-a


# In[33]:


bool(out)


# In[40]:


x = ("BMW","AUDI","MERC")


# In[41]:


x


# In[42]:


enumerate(x)


# In[43]:


y = enumerate(x)


# In[44]:


y


# In[45]:


x = format(.5, '%')


# In[46]:


x


# In[53]:


x = format(15, 'c')


# In[54]:


x


# In[55]:


x = format(15, 'b')


# In[56]:


x


# In[57]:


class Person:
    name="Keth"
    age = 34
    country = "England"


# In[58]:


Person


# In[59]:


type(Person)


# In[60]:


x = getattr(Person,'age')


# In[61]:


x


# In[62]:


id(x)


# In[66]:


name = " John "


# In[67]:


len(name)


# In[68]:


len(name)


# In[69]:


def getLen(n):
    return len(n)


# In[70]:


user = ('John', 'Keth', 'Eva', 'Emila')


# In[71]:


x = map(getLen, user)


# In[72]:


x


# In[73]:


[4,4,3,5]


# In[74]:


min(35,435,57,46,325)


# In[75]:


max(35,463454,6867345865,54547)


# In[76]:


pow(2,3)


# In[77]:


x = 10


# In[78]:


type(x)


# In[81]:


x = lambda a : a+10


# In[82]:


print(x(5))


# In[86]:


x = lambda a,b,c : a+b+c


# In[87]:


print(x(5,2,5))


# In[97]:


def myfunc(n):
    return lambda a: a*n


# In[101]:


double = myfunc(2)
tripple = double(3)


# In[99]:


print(tripple)


# In[89]:


first = double(2)


# In[91]:


print(first(3))


# In[92]:


second = first(3)


# In[93]:


print(second(4))


# In[ ]:




