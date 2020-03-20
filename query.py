#!/usr/bin/env python
# coding: utf-8

# In[1]:


import rasa
from rasa.nlu.model import Interpreter


# In[2]:


interpreter=Interpreter.load('/users/sbagadhi/desktop/GIT/models/nlu/new')


# In[3]:


def ask_question(text):
    print(interpreter.parse(text))


# In[ ]:




