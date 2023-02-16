#!/usr/bin/env python
# coding: utf-8

# In[7]:


try:
    f= open("does.text")

except Exception as e:
    print(e)
    
finally:
    print("Run this anyway")
    
print("important stuff")


# In[8]:


try:
    f= open("code")

except Exception as e:
    print(e)
print("import")


# In[ ]:




