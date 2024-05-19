#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
characters="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_"
passlength=int(input("Specify the length of password: "))

def generate(): 
    pswd ="" 
    for i in range(passlength):
        pswd+= random.choice(characters)
    return pswd

pswder = generate()
print(f"This is your new password : {pswder} ")


# In[ ]:




