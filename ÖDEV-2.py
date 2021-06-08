#!/usr/bin/env python
# coding: utf-8

# ÖDEV-2

# In[28]:


a=1000
b=0.12
toplam=a*(1+b)**7
kazanc=a*(1+b)**7-1000


# In[29]:


print("Toplam Para:", toplam)
print("Kazandığımız Para:", kazanc)


# In[32]:


print("Hafta başında {} dolarlık bitcoin aldığımızda günde ortalama {} kazançla, bir hafta sonunda {:.2f} dolar kazanırdık".format(a,b,kazanc))

